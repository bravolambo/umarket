from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Verification
from django.core.files.base import ContentFile
import base64

def verification_view(request):
    """
    Handle the verification form submission and render the verification page.
    """
    if request.method == 'POST':
        # Retrieve form data directly from POST and FILES
        registration_number = request.POST.get('registration_number')
        id_front = request.FILES.get('id_front')
        id_back = request.FILES.get('id_back')
        real_time_photo_data = request.POST.get('real_time_photo')  # Base64 encoded photo

        if registration_number and id_front and id_back:
            # Save data to the Verification model
            verification = Verification.objects.create(
                registration_number=registration_number,
                id_front=id_front,
                id_back=id_back,
            )

            # Handle real-time photo if provided
            if real_time_photo_data:
                try:
                    # Decode the base64 string and save as an image file
                    format, imgstr = real_time_photo_data.split(';base64,')
                    ext = format.split('/')[-1]  # Extract image extension (e.g., png)
                    photo_data = ContentFile(base64.b64decode(imgstr), name=f'real_time_photo.{ext}')

                    # Save the decoded image to the model's field
                    verification.real_time_photo.save(f'real_time_photo.{ext}', photo_data)
                except Exception as e:
                    return HttpResponse(f"Error processing real-time photo: {str(e)}")

            return redirect('home')
        else:
            return HttpResponse("All fields are required. Please check the form.")
    else:
        # Render the verification form template
        return render(request, 'verification/verification.html')


def index(request):
    """
    Render the success page after successful form submission.
    """
    return render(request, 'umarket/index.html')
