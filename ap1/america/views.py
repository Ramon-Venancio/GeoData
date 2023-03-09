from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'america/index.html')

def brasil(request):
    return render(request, 'america/brasil.html')

def mexico(request):
    return render(request,'america/mexico.html')

def argentina(request):
    return render(request,'america/argentina.html')