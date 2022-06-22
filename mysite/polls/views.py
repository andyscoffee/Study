from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, World! You're at poll index.")
    # http리퀘스트가 오면 response로 위의 메세지 반환
