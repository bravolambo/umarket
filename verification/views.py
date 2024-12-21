from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Verification

def verification_success(request):
    """Renders the success page after a successful verification."""
    return render(request, 'verification/success.html', {})

def verification_view(request):
    """Handles the verification process."""
    if request.method == "POST":
        registration_number = request.POST.get('registration_number', '').strip()
        scanned_data = request.POST.get('scanned_data', '').strip()
        print(request.POST)
        # Validate the input manually
        if not registration_number:
            messages.error(request, "Registration number is required.")
        else:
            # Save the data to the model
            verification = Verification(
                registration_number=registration_number,
                scanned_data=scanned_data,
            )
            try:
                verification.save()
                messages.success(request, "Verification successful!")
                return redirect('verification-success')  # Redirect to a success page
            except Exception as e:
                messages.error(request, f"Error saving data: {e}")

    return render(request, 'verification/verification.html')
