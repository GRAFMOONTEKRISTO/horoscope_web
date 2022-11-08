from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def get_rectangle_area(request, width: int, height: int):
    # return HttpResponse(f'Площадь прямоугольника размером {width} на {height} равна {width * height}')
    return render(request, 'geometry/rectangle.html')


def get_square_area(request, width: int):
    # return HttpResponse(f'Площадь квадрата размером {width} на {width} равна {width * width}')
    return render(request, 'geometry/square.html')


def get_circle_area(request, radius: int):
    # return HttpResponse(f'Площадь круга радиуса {radius} равна {3.14 * radius ** 2}')
    return render(request, 'geometry/circle.html')


""""""


def get_rectangle(request, width: int, height: int):
    redirect_url = reverse('path_rectangle', args=(width, height))
    return HttpResponseRedirect(redirect_url)


def get_square(request, width: int):
    redirect_url = reverse('path_square', args=(width,))
    return HttpResponseRedirect(redirect_url)


def get_circle(request, radius: int):
    redirect_url = reverse('path_circle', args=(radius,))
    return HttpResponseRedirect(redirect_url)
