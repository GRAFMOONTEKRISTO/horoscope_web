from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

week_days_dict = {

    'monday': 'Это понедельник',
    'tuesday': 'Это вторник',
    'wednesday': 'Это среда',
    'thursday': 'Это четверг',
    'friday': 'Это пятница',
    'saturday': 'Это суббота',
    'sunday': 'Это воскресенье',

}


def get_info_about_days(request, days: str):
    return render(request, 'week_days/greeting.html')

    # description = week_days_dict.get(days)
    #
    # if description:
    #     return HttpResponse(description)
    #
    # else:
    #     return HttpResponse(f'Я не знаю, что это за день недели {days}')


"""Перенаправляем - если в URL цифра - то она перенаправится и превратится в название дня
Можно запутаться, но ты не путайся"""


def get_info_about_days_number(request, days: int):
    all_days = list(week_days_dict)

    if days > len(week_days_dict):
        return HttpResponse(f'Неверный номер дня - {days}')

    name_day_redirect = all_days[days - 1]

    redirect_url = reverse('days_name', args=(name_day_redirect,))
    return HttpResponseRedirect(redirect_url)


people = [
    'Жукова Анна Константиновна',
    'Юлия Степановна Потапова',
    'Гущин Аполлинарий Тимурович',
    'Дорофей Ярославович Третьяков',
    'Селезнева Анна Тарасовна',
    'Федотов Симон Харлампьевич',
    'Красильникова Вера Борисовна',
    'Бажен Тихонович Костин',
    'Веселова Анжелика Тимофеевна',
    'Щербаков Самсон Феодосьевич'
]


def get_info_about_peple(request):
    info_people = list(people)

    context = {
        'info_people':info_people

    }
    return render(request, 'week_days/people.html', context=context)
