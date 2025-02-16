from django.shortcuts import render, redirect
from .forms import ChirpForm

# Create your views here.
def chirp_view(request):
    """
    The view to display the chirpForm to users.
    """
    
    # Process the form data if it's a POST request
    if request.method == 'POST':
        # Create a form instance and fill in data gained from the request
        form = ChirpForm(request.POST)
        
        # Save and redirect to success page if from is valid
        if form.is_valid():
            form.save()
            return redirect('success')

    # Create blank form if a GET (or any other method)
    else:
        form = ChirpForm()

    return render(request, 'chirper/chirp_form.html', {'form': form})