from django.shortcuts import render, redirect, get_object_or_404
from base.models import UserDocuments
import requests


def add_document(request):
    if request.method == 'POST':
        document_name = request.POST.get('document_name')
        document_file = request.FILES.get('document')

        files = {"filePath": (document_name, document_file.read(), "application/octet-stream")}
        url = "https://api.verbwire.com/v1/nft/store/file"
        headers = {
            "accept": "application/json",
            "X-API-Key": "sk_live_fdd243a1-07c3-4c90-a976-c133c47f1b3a"
        }
        response = requests.post(url, files=files, headers=headers)
        response_data = response.json()
        print(response_data.get('ipfs_storage').get('ipfs_url'))
        if document_name and document_file:
            try:
                ipfs_id = response_data.get('ipfs_storage').get('ipfs_url')
            except:
                ipfs_id = ''  # Calculate or generate IPFS ID
            user_document = UserDocuments(document_name=document_name, document=document_file, ipfs_id=ipfs_id)
            user_document.save()
            return redirect('document_list')  # Redirect to a view that lists all documents
        

    return render(request, 'Documents/add_document.html')

def document_list(request):
    documents = UserDocuments.objects.all()
    return render(request, 'Documents/document_list.html', {'documents': documents})


def edit_document(request, document_id):
    document = get_object_or_404(UserDocuments, id=document_id)
    if request.method == 'POST':
        # Get data from POST request
        document_name = request.POST.get('document_name')
        # Handle file upload manually
        if 'document' in request.FILES:
            document.document = request.FILES['document']
        ipfs_id = request.POST.get('ipfs_id')
        # Update document fields
        document.document_name = document_name
        document.ipfs_id = ipfs_id
        # Save changes
        document.save()
        # Redirect to document list
        return redirect('document_list')
    return render(request, 'Documents/edit_document.html', {'document': document})


def delete_document(request, document_id):
    document = get_object_or_404(UserDocuments, id=document_id)
    if request.method == 'GET':
        # Delete the document
        document.delete()
        # Redirect to document list
        return redirect('document_list')
    return redirect('document_list')

