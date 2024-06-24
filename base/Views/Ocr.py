from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from pymongo import MongoClient
from gridfs import GridFS
from bson import ObjectId  # Import ObjectId from bson
from io import BytesIO
import fitz  # PyMuPDF
from base.models import PatientDocument
from g4f.client import Client

@login_required
def extract_text(request):
    if request.method == 'POST' and request.FILES.get('pdf'):
        # Get the uploaded PDF file
        pdf_file = request.FILES['pdf']
        
        # Initialize MongoDB client and GridFS
        client = MongoClient('mongodb+srv://nagi:nagi@cluster0.ohv5gsc.mongodb.net/')  # Use your MongoDB connection string
        db = client['MedMate']
        fs = GridFS(db)
        
        # Save the uploaded file to GridFS
        file_id = fs.put(pdf_file.read(), filename=pdf_file.name)
        
        # Save the document with the GridFS file ID
        document = PatientDocument.objects.create(user=request.user, file_gridfs_id=str(file_id))
        
        # Read PDF data from GridFS
        grid_fs_file = fs.get(file_id)
        pdf_buffer = BytesIO(grid_fs_file.read())
        
        # Open the PDF file with PyMuPDF
        pdf_document = fitz.open(stream=pdf_buffer, filetype="pdf")
        
        # Extract text from each page and combine
        extracted_text = ""
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text = page.get_text()
            extracted_text += text + "\n"
        
        # Generate summary of the extracted text
        summary = generate_summary(extracted_text)
        
        # Save the extracted text and summary to the model
        document.file_content = extracted_text
        document.summary = summary
        document.save()
    
    # Retrieve all documents for the current user
    documents = PatientDocument.objects.filter(user=request.user)
    
    return render(request, 'Ocr/upload_image.html', {'documents': documents})

@login_required
def download_file(request, document_id):
    # Get the document from the database
    document = get_object_or_404(PatientDocument, id=document_id, user=request.user)
    
    # Initialize MongoDB client and GridFS
    client = MongoClient('mongodb+srv://nagi:nagi@cluster0.ohv5gsc.mongodb.net/')  # Use your MongoDB connection string
    db = client['MedMate']
    fs = GridFS(db)
    
    # Retrieve the file from GridFS using the stored file ID
    grid_fs_file = fs.get(ObjectId(document.file_gridfs_id))
    
    # Create a response with the file content
    response = HttpResponse(grid_fs_file.read(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{grid_fs_file.filename}"'
    
    return response

@login_required
def delete_file(request, document_id):
    # Get the document from the database
    document = get_object_or_404(PatientDocument, id=document_id, user=request.user)
    
    # Initialize MongoDB client and GridFS
    client = MongoClient('mongodb+srv://nagi:nagi@cluster0.ohv5gsc.mongodb.net/')  # Use your MongoDB connection string
    db = client['MedMate']
    fs = GridFS(db)
    
    # Delete the file from GridFS
    fs.delete(ObjectId(document.file_gridfs_id))
    
    # Delete the document from the database
    document.delete()
    
    return redirect('ocr')

def generate_summary(text):
    client = Client()
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a useful AI to provide the summary of the given content in English."},
            {"role": "user", "content": f"Give me the summary of the following content: '''{text}'''."}
        ]
    )
    ai_response = chat_completion.choices[0].message.content or ""
    return ai_response
