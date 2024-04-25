from django.shortcuts import render, redirect
from base.models import UserProfile
E = "Ecommerce"

def dash(request):
    return render(request, 'baseindex/index.html')
def prescription(request):
    return render(request, 'Ecommerce/prescription.html')
def report(request):
    return render(request, 'Ecommerce/report.html')
def viewprescription(request):
    return render(request,'Ecommerce/viewprescription.html')
def viewreport(request):
    return render(request,'Ecommerce/viewreport.html')
def Addprescription(request):
    return render(request,'Ecommerce/Add-prescription.html')
def Addreport(request):
    return render(request,'Ecommerce/Add-report.html')
def calendar(request):
    return render(request,'Ecommerce/calendar.html')

  # Note: csrf_exempt is used here for simplification, be sure to handle CSRF protection appropriately in production.
def create_or_update_user_profile(request):
    if request.method == 'POST':
        # Attempt to fetch existing profile or create a new one
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)

        # Update fields from form data
        user_profile.firstname = request.POST.get('firstname')
        user_profile.lastname = request.POST.get('lastname')
        user_profile.email = request.POST.get('email')
        user_profile.username = request.POST.get('username')
        user_profile.biography = request.POST.get('biography')
        user_profile.address_street = request.POST.get('address_street')
        user_profile.address_city = request.POST.get('address_city')
        user_profile.address_state = request.POST.get('address_state')
        
        # Handling files
        user_profile.change_profile = request.FILES.get('change_profile', user_profile.change_profile)
        user_profile.background_image = request.FILES.get('background_image', user_profile.background_image)
        user_profile.experience = request.POST.get('experience', user_profile.experience)

        user_profile.save()
        return redirect('profile')  # Ensure this URL name is correct

    # For GET or other methods, show the form or profile
    return render(request, 'Ecommerce/profile.html', {"user_data": request.user.profile})

def profile(request):
    try:
        user_profile = request.user.profile
    except UserProfile.DoesNotExist:
        user_profile = None
        print("UserProfile does not exist for the user:", request.user)

    return render(request, 'Ecommerce/profile.html', {"user_data": user_profile})