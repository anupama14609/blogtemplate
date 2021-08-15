from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'script/home.html')

def AnalyzeUrl(request):
    return render(request, 'script/analyzeurl.html')

def GeneratePassword(request):
    return render(request, 'script/generatepassword.html')

def GenerateMeta(request):
    return render(request, 'script/generatemeta.html')

def LocationFinder(request):
    return render(request, 'script/locationfinder.html')