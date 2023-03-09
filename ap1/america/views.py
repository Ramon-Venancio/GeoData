from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'index.html')

def brasil(request):
    return render(request, 'brasil.html')

def mexico(request):
    return render(request,'mexico.html')

def argentina(request):
    return render(request,'argentina.html')