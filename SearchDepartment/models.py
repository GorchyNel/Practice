from django.db import models


# Проставить максимкальные длины текстовых полей для ВСЕХ форм!
class Request(models.Model):
    Number = models.PositiveIntegerField()
    Address = models.CharField(max_length=40)
    Name = models.CharField(max_length=40)
    TypeOfDefect = models.CharField(max_length=68)
    AdministrativeDistrict = models.CharField(max_length=17)
    Description = models.TextField()

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    # Функция для вывода подписи к созданным в базе данных объектам
    def __str__(self):
         return "Заявка №{0}".format(self.Number)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Department(models.Model):
    Name = models.CharField(max_length=40)
    TypeOfDefect = models.CharField(max_length=68)
    AdministrativeDistrict = models.CharField(max_length=17)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    # Функция для вывода подписи к созданным в базе данных объектам
    def __str__(self):
         return "Отдел {0}".format(self.Name)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class RequestImage(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, default=None)
    Image = models.FileField(upload_to='request_images')
    IsActive = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    # Функция для вывода подписи к созданным в базе данных объектам
    def __str__(self):
         return "{0}".format(self.id)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
