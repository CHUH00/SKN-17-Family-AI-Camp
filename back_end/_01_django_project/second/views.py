from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request)
    # return HttpResponse('<hl>This is Second Index Page🐿️</hl>')
    return render(request, 'second/index.html')
