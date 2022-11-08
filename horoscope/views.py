from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

"""Находим зодиаки"""

zodiac_dict = {

    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',

}


def index(request):
    zodiacs = list(zodiac_dict)

    context = {
        'zodiacs': zodiacs,
        'zodiac_dict': zodiac_dict,
    }

    return render(request, 'horoscope/index.html', context=context)


"""Информация о знаках через HTML"""


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    zodiacs = list(zodiac_dict)
    data = {
        'description_zodiac': description,
        'sing': sign_zodiac.title(),
        'sing_name': description.split()[0],
        'zodiacs': zodiacs,
    }

    return render(request, 'horoscope/info_zodiac.html', context=data)


"""Информация о актере через HTML"""


def get_info_about_actor(request):
    data = {
        'year_born': 2000,
        'city_born': 'Злынка',
        'movie_name': 'Злынковчане',
    }

    return render(request, 'actor/info_actor.html', context=data)


"""Информация о гекордах гинета HTML"""


def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'guinness/guinnessworldrecords.html', context=context)


"""Находим знак зодиака по цифре и, перенаправляя цифру, меняем ее на наименование знака"""


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)

    if sign_zodiac > len(zodiacs):
        return HttpResponse(f'Передан неправильный порядковый номер знака зодиака {sign_zodiac}')

    name_zodiac = zodiacs[sign_zodiac - 1]

    redirect_url = reverse('horoscope_name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)


"""Находим стихии (не доделал)"""

four_elements_dict = {

    'fire': ['aries', 'taurus', 'gemini'],
    'earth': ['leo', 'virgo', 'libra'],
    'air': ['sagittarius', 'capricorn', 'aquarius'],
    'water': ['pisces', 'scorpio', 'cancer'],

}


def html_about_four_elements(request):
    elements = list(four_elements_dict)

    li_elements = ''
    for element in elements:
        redirect_path = reverse('elements_name', args=(element,))
        li_elements += f'<li><a href={redirect_path}>{element.title()}</a></li>'

    response = f"""
            <ol>
                {li_elements}
            </ol>
            """
    return HttpResponse(response)


def get_info_about_four_elements(request, sign_element: str):
    description = four_elements_dict.get(sign_element)

    if description:
        return HttpResponse(description)

    else:
        return HttpResponse(f'Я не знаю, что это за стихия {sign_element}')


"""Первым параметром она (reverse) принимает название нашего URL из urlsHoroscope
  И функция reverse патается воссоздать URL, она отыскивает, где используется наш path
  И в этот path(<str:sign_zodiac>/) мы попадем ,когда сработает этот наш URL(path('horoscope/') в главном urls"""
"""Функция reverse она конструирует, т.е. начало будет /horoscope и потом мы должны добавить название знака зодиака
через args"""
