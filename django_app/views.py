from django.shortcuts import render

def home(request):
    """View for the homepage displaying the HelloWorld message."""
    return render(request, 'home.html')
