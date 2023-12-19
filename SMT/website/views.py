from django.shortcuts import render



# Create home page view
def home(request):
    return render(request, "home.html", {})
