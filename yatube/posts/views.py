from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse('<h1>Index</h1>')


def group_posts(request, slug):
    return HttpResponse(f'<h1>{slug}</h1>')
