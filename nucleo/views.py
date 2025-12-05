from django.shortcuts import render
import requests #type: ignore


def inicio(request):
    return render(request, 'inicio2.html')
