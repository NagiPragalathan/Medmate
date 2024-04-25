from django.shortcuts import render
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
        # Fetching data from the form
        user_id = request.user.id  # Assumes there's an ID field to distinguish new vs. existing records
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        biography = request.POST.get('biography')
        address_street = request.POST.get('address_street')
        address_city = request.POST.get('address_city')
        address_state = request.POST.get('address_state')

        # Handling files
        change_profile = request.FILES.get('change_profile', None)
        background_image = request.FILES.get('background_image', None)
        experience = request.FILES.get('experience', None)

        # Basic validation for required fields
      

        # Determine if this is an update or create operation
        if user_id:
            # Update existing UserProfile
            try:
                user_profile = UserProfile.objects.get(id=user_id)
                user_profile.firstname = firstname
                user_profile.lastname = lastname
                user_profile.username = username
                user_profile.biography = biography
                user_profile.address_street = address_street
                user_profile.address_city = address_city
                user_profile.address_state = address_state
                # Update files if new files have been provided
                if change_profile:
                    user_profile.change_profile = change_profile
                if background_image:
                    user_profile.background_image = background_image
                if experience:
                    user_profile.experience = experience
                user_profile.save()
                return render(request, 'Ecommerce/profile.html')

            except UserProfile.DoesNotExist:
                    return render(request, 'Ecommerce/profile.html')

        else:
            # Create new UserProfile
            user_profile = UserProfile(
                firstname=firstname,
                lastname=lastname,
                email=email,
                username=username,
                biography=biography,
                address_street=address_street,
                address_city=address_city,
                address_state=address_state,
                change_profile=change_profile,
                background_image=background_image,
                experience=experience
            )
            user_profile.save()
            return render(request, 'Ecommerce/profile.html')


    else:
        try:
            user_profile = UserProfile.objects.get(id=user_id)
        except:
            user_profile = ""

        return render(request, 'Ecommerce/profile.html',{"user_data":user_profile})


 


def profile(request):
    obj = UserProfile.objects.all()
    # obj.delete()
    for i in obj:
        print(i.address_city, i.address_state)
    return render(request,'Ecommerce/profile.html')

