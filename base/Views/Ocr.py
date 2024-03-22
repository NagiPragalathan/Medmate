from django.shortcuts import render
from django.http import JsonResponse
import pytesseract
from PIL import Image as PILImage
from io import BytesIO

def extract_text(request):
    if request.method == 'POST' and request.FILES.get('image'):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        # Get the uploaded image file
        image_file = request.FILES['image']
        
        # Read image data into BytesIO object
        with BytesIO(image_file.read()) as image_buffer:
            # Open image using PIL
            image = PILImage.open(image_buffer)
            
            # Extract text using OCR
            text = pytesseract.image_to_string(image)
            
            # Return the extracted text as a JSON response
            return JsonResponse({'text': text})

    return render(request, 'Ocr/upload_image.html')

