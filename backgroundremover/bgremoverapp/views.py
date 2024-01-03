from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. This is my Background remover app.")

def about(request):
    return HttpResponse("This is the about page")

def bgremover(request):
    import requests

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

    return HttpResponse(response.status_code)