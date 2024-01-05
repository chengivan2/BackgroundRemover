from django.shortcuts import render
import requests
from django.http import HttpResponseRedirect
import os


def bgremover(request):
    return render(request, "bgremoverapp/bgremoved.html")

def about(request):
    return render(request, "bgremoverapp/about.html")



def home(request):
    if request.method == 'POST':
        file = request.FILES['file'] if 'file' in request.FILES else None

    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(file, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'YOUR-API-KEY'},
    )
    if response.status_code == requests.codes.ok:
        with open('no-bg.png', 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)
    return render(request, 'bgremoverapp/home.html')
