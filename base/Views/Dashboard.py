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
def Ambulance(request):
    return render(request,'Ecommerce/home.html')

  # Note: csrf_exempt is used here for simplification, be sure to handle CSRF protection appropriately in production.

def create_or_update_user_profile(request):
    if request.method == 'POST':
        # Fetch the user's existing profile or create a new one
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)

        # Mandatory fields
        mandatory_fields = ['firstname', 'lastname', 'email', 'username', 'change_profile', 'background_image', 'experience']
        missing_fields = [field for field in mandatory_fields if not request.POST.get(field) and not request.FILES.get(field)]

        if missing_fields:
            # Return an error message if any mandatory fields are missing
            error_message = "Please fill in all required fields."
            return render(request, 'profile_form.html', {'error_message': error_message, 'user_data': user_profile})

        # If all fields are present, proceed to update the user profile
        user_profile.firstname = request.POST['firstname']
        user_profile.lastname = request.POST['lastname']
        user_profile.email = request.POST['email']
        user_profile.username = request.POST['username']
        user_profile.biography = request.POST.get('biography', '')

        user_profile.change_profile = request.FILES.get('change_profile', user_profile.change_profile)
        user_profile.background_image = request.FILES.get('background_image', user_profile.background_image)
        user_profile.experience = request.POST.get('experience', user_profile.experience)

        user_profile.save()
        return redirect('profile')  # Redirect to a profile page or other appropriate URL

    else:
        # Handle GET request
        return render(request, 'Ecommerce/profile.html', {"user_data": request.user.profile})

def profile(request):
    try:
        user_profile = request.user.profile
    except UserProfile.DoesNotExist:
        user_profile = None
        print("UserProfile does not exist for the user:", request.user)

    return render(request, 'Ecommerce/profile.html', {"user_data": user_profile})