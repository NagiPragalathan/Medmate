# Refactoring the classify_emotion function for more efficient emotion classification\

import random    
from textblob import TextBlob

def classify_emotion_efficient(text: str):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    # Define a dictionary to hold the conditions and corresponding emotions
    conditions = {
        (0.5, 1, 0.5, 1): random.choice(['Joyful', 'Excited', 'Elated']),
        (0.5, 1, 0, 0.5): random.choice(['Happy', 'Pleased']),
        (0, 0.5, 0.5, 1): random.choice(['Content', 'Satisfied']),
        (0, 0.5, 0, 0.5): random.choice(['Relieved', 'Optimistic', 'Hopeful']),
        (0, 0, 0.5, 1): random.choice(['Uncertain', 'Confused']),
        (0, 0, 0, 0.5): random.choice(['Neutral', 'Indifferent']),
        (-0.5, 0, 0.5, 1): random.choice(['Sad', 'Disappointed', 'Discouraged']),
        (-0.5, 0, 0, 0.5): random.choice(['Unhappy', 'Pessimistic']),
        (-1, -0.5, 0.5, 1): random.choice(['Angry', 'Frustrated', 'Annoyed']),
        (-1, -0.5, 0, 0.5): random.choice(['Upset', 'Furious'])
    }

    # Loop through the conditions and return the corresponding emotions
    for (p_low, p_high, s_low, s_high), emotion_list in conditions.items():
        if p_low < polarity <= p_high and s_low < subjectivity <= s_high:
            return emotion_list

    return 'Normal'  # Return 'Unknown' if no conditions are met

def find_unwanted_words(text):
    unwanted_words = [
        "fuck", "bitch", "shit", "faker", "pussy",
        ]
    found_unwanted_words = []
    # Split the text into words
    words = text.split()
    full_word = ""
    # Check each word in the text
    for word in words:
        full_word = full_word+" "+word
        if word in unwanted_words:
            full_word = full_word+" " + word[0]+"*"*int(len(word)-2)+word[-1]
            found_unwanted_words.append(word)
    return full_word

def find_unwanted_words_bool(text):
    bool_word = False
    unwanted_words = [
        "fuck", "bitch", "shit", "faker", "pussy",
        ]
    found_unwanted_words = []
    # Split the text into words
    words = text.split()
    full_word = ""
    # Check each word in the text
    for word in words:
        full_word = full_word+" "+word
        if word in unwanted_words:
            bool_word = True
            found_unwanted_words.append(word)
    return bool_word
