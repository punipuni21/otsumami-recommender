from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')

def submit(request):
    return render(request, 'frontend/submit.html')

def quiz(request):
    return render(request, 'frontend/quiz.html')

def photo(request):
    return render(request, 'frontend/photo.html')

def result(request):
    return render(request, 'frontend/result.html')