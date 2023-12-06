from django.shortcuts import render

def sname(request):
    return render(request, 'hello.html')

def sno(request):
    return render(request, 'main.html')