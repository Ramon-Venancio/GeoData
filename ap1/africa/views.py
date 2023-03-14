from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request,'africa/index.html')

def angola(request):
    return render(request,'africa/angola.html')

def madagascar(request):
    return render(request,'africa/madagascar.html')
