from django.shortcuts import render
from .forms import SearchForm
from .models import *


def search_page(request):
    # параметр request к другим реквестам отношения не имеет!
    search_form = SearchForm()  # очищение формы

    response = {
        "search_form": search_form, "searched_request": None,
        "department": None, "photos": None, "IsNotFirstResponse": False
    }  # это словарь,
    # в который впоследствии будут помещены передаваемые в шаблон данные

    if request.method == "POST":
        data = request.POST

        if SearchForm(data).is_valid():
            response["IsNotFirstResponse"] = True
            req_number = int(request.POST.get("RequestNumber"))

            searched_request = None
            list_of_requests = list(Request.objects.all())
            for req in list_of_requests:
                if req.Number == req_number:
                    searched_request = req
                    break

            if searched_request is not None:
                response["searched_request"] = searched_request  # добавление заявки в словарь

                list_of_photos = list(RequestImage.objects.filter(request__Number=searched_request.Number))
                response["photos"] = list_of_photos

                list_of_departments = list(Department.objects.all())  # берем из БД список всех Отделов

                department = list(filter(lambda d: d.TypeOfDefect == searched_request.TypeOfDefect and
                                                   d.AdministrativeDistrict == searched_request.AdministrativeDistrict,
                                         list_of_departments))
                if len(department) == 1:
                    response["department"] = department[0]

    return render(request, 'Search.html', response)
