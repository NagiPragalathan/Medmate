import cv2
import pyaudio
import wave
import numpy as np
import os
import glob
from .yolo_utils import *
from django.http import StreamingHttpResponse
import time
import datetime
import threading
from django.conf import settings
import speech_recognition as sr
from .Emotion import classify_emotion_efficient, find_unwanted_words, find_unwanted_words_bool
from django.views.decorators import gzip

from django.shortcuts import render

def record_audio(stream, filename):
    chunk = 4096  # Larger chunk size for faster recording
    sample_format = pyaudio.paInt16
    channels = 2
    fs = 16000  # Lower sample rate for faster processing
    seconds = 10
    frames = []

    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

def convert_audio(i):
    if i >= 0:
        sound = 'record.wav'
        r = sr.Recognizer()

        while not os.path.exists(sound):
            pass  # Wait until the recording is complete

        with sr.AudioFile(sound) as source:
            r.adjust_for_ambient_noise(source)
            print(f"Converting Audio To Text and saving to file...")
            audio = r.listen(source)
        try:
            value = r.recognize_google(audio)
            try:
                os.remove(sound)
            except:
                print("Error from 'os' trying to remove the created Audio file")
            print("writing...")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current timestamp
            Text_file = os.path.join(settings.BASE_DIR, 'base', 'generated_files', 'converted_text.txt')
            print(Text_file)
            with open(Text_file, "a") as f:
                if value and value != " " and value != "":
                    f.write(f"[{timestamp}], {find_unwanted_words(value)}, {classify_emotion_efficient(value)}, {find_unwanted_words_bool(value)}\n")  # Write timestamp and value to file
                    print(value)
                else:
                    f.write(f"[{timestamp}] \n") 
        except sr.UnknownValueError:
            print("unknown..!")
        except sr.RequestError as e:
            print(e)


time_limit = 10 
last_screenshot_time = 0
audio_process = True
old_image = None
create_folder = True
local_person_folder = None
def gen(camera):
    global audio_process
    global old_image
    global create_folder
    def audio_fun():
        p = pyaudio.PyAudio()
        chunk = 4096 
        sample_format = pyaudio.paInt16
        channels = 2
        fs = 16000
        stream = p.open(format=sample_format, channels=channels, rate=fs,
                    frames_per_buffer=chunk, input=True)
        filename = 'record.wav'
        record_audio(stream, filename)
        convert_audio(0)
    def get_image_count(directory):
        files = glob.glob(os.path.join(directory, 'detected_*.jpg'))
        return len(files)
    
    def cap_cam(camera,ret,image):
        global create_folder
        global last_screenshot_time, create_folder
        global local_person_folder
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (320, 320))
        img = img.astype(np.float32)
        img = np.expand_dims(img, 0)
        img = img / 255
        classes_file_path = os.path.join(settings.BASE_DIR,'base','Views', 'resources', 'classes.TXT')
        # print(classes_file_path)
        class_names = [c.strip() for c in open(classes_file_path,'r').readlines()]
        boxes, scores, classes, nums = yolo(img)
        count=0
        should_save_image = False  # Flag to check if the image should be saved

        for i in range(nums[0]):
            if int(classes[0][i] == 0):
                count +=1
            if int(classes[0][i] == 67):
                should_save_image = True
                print('Mobile Phone detected')
        if count == 0:
            should_save_image = True
            print('No person detected')
        elif count > 1: 
            should_save_image = True
            print('More than one person detected')
            
        image = draw_outputs(image, (boxes, scores, classes, nums), class_names)

        # Initialize base save path
        base_save_path = os.path.join(settings.BASE_DIR, 'base', 'saved_images')
        current_time = time.time()
        # Save the image if any condition is met
        if should_save_image and current_time - last_screenshot_time >= time_limit:
            try:
                # Create base directory if it doesn't exist
                last_screenshot_time = current_time
                if not os.path.exists(base_save_path):
                    os.makedirs(base_save_path)
                # Create or identify person folder
                if create_folder:
                    person_folder = f'Person_{len(os.listdir(base_save_path))}'
                    create_folder=False
                    local_person_folder = person_folder
                person_save_path = os.path.join(base_save_path, local_person_folder)
                
                # Create person directory if it doesn't exist
                if not os.path.exists(person_save_path):
                    os.mkdir(person_save_path)

                # Count existing images and determine new save path
                # image_count = get_image_count(person_save_path)
                save_path = os.path.join(person_save_path, f'detected_{len(os.listdir(person_save_path))}.jpg')
                print(save_path)
                # Save the image
                cv2.imwrite(save_path, image)
                print(f"Image saved at {save_path}")
                
            except Exception as e:
                print(f"Can't take the screenshot. Error: {e}")
        
        # Encode image as JPEG
        _, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        return (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    while True:
        ret, image = camera.read()
        # YOLO prediction logic here
        if ret == False:
            break
        
        if audio_process:
            audio_process = False
            audio_thread = threading.Thread(target=audio_fun)
            audio_thread.start()
            audio_process = True
        try:
            picture_image = cap_cam(camera, ret, image)
        except:
            picture_image=old_image
        old_image = cap_cam(camera, ret, image)
        yield picture_image


@gzip.gzip_page
def video_feed(request):
    cap = cv2.VideoCapture(0)
    return StreamingHttpResponse(gen(cap), content_type="multipart/x-mixed-replace;boundary=frame")


def MeetRoom(request):
    return render(request, 'VideoConf/MeetRoom.html')