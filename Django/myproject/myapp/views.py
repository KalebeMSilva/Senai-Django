from django.shortcuts import render

# Create your views here.
def my_project(request):
    return render(request, 'index.html')