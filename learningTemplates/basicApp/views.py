from django.shortcuts import render

# Create your views here.

def index(request):
    contextDict = {'text':"Hello world", "number": 100}
    return render(request, 'basicApp/index.html', context = contextDict)

def other(request):
    return render(request, 'basicApp/other.html')

def relative(request):
    return render(request, 'basicApp/relativeUrlTemplate.html')