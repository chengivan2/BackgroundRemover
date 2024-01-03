from django.shortcuts import render
import requests


def home(request):
    return render(request, "bgremoverapp/home.html")

def about(request):
    return render(request, "bgremoverapp/about.html")

def bgremover(request):

    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        data={
            'image_url': 'https://www.remove.bg/example.jpg',
            'size': 'auto'
        },
        headers={'X-Api-Key': 'YOUR-API-KEY'},
    )
    if response.status_code == requests.codes.ok:
        with open('no-bg1.png', 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)

    return render(request, "bgremoverapp/bgremoved.html")