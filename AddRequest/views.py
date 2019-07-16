from django.shortcuts import render
from .forms import *
import random
from django.core.files.storage import FileSystemStorage


def add_page(request):
    form_not_valid = False

    form_img = RequestImageForm()
    form = RequestForm()

    if request.method == "POST":
        # сохранение текстовой инфы
        form = RequestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)   # save(commit=False) возвращает объект Модели с данными,
            # находящимися в форме, но не сохраняет его в БД

            try:
                Request.objects.get(Address=req.Address, Name=req.Name, TypeOfDefect=req.TypeOfDefect,
                                    AdministrativeDistrict=req.AdministrativeDistrict,
                                    Description=req.Description)  # защита от повторной отправки формы,
                # происходящей при перезагрузке страницы

            except Request.DoesNotExist:
                # генерация номера заявки:
                while True:
                    gen_number = random.randint(10_000_000, 99_999_999)
                    try:
                        Request.objects.get(Number=gen_number)
                    except Request.DoesNotExist:
                        break

                req.Number = gen_number
                req.save()  # сохраняем данные из модели в БД

                # Сохранение фото
                for img in request.FILES.getlist("Image"):
                    img_model = RequestImage(request=req, Image=img, IsActive=True)
                    img_model.save()

            form = RequestForm()  # очищаем форму

        else:
            form_not_valid = True

    response = {"form": form, "FormNotValid": form_not_valid, "form_img": form_img}
    return render(request, 'AddRequest.html', response)
