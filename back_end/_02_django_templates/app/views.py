from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, 'app/index.html')

def basics(request):
    context = {
        "name": "코난",
        "job": "탐정",
        "height": 150,
        "hobby": ["추리하기", "사건 쫓아다니기", "탐정님 재우기"],
        "today": datetime.now(),
        "users": [
            {"id": 1, "name": "뭉치", "study": False},
            {"id": 2, "name": "세모", "study": True},
            {"id": 3, "name": "아름", "study": True},
        ],
        "users": [],
        "eng_name": "conan",
        "price": 12345.6789
    }
    return render(request, 'app/01_basics.html', context)