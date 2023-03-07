from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'index.html')

def brasil(request):
    return render(request, 'brasil.html')
