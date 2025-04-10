from django.db import models

# Create your models here.

class Subdivision(models.Model):
    name = models.CharField('Подразделение', max_length=150)
    parent = models.ForeignKey('Subdivision', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

class Building(models.Model):
    name = models.CharField('Корпус', max_length=30, unique=True)
    address = models.CharField('Адрес корпуса', max_length=50)
    cabinet = models.CharField('Кабинет', max_length=10)

    def __str__(self):
        return f"{self.name}" + ", " + f"{self.address}" + ", " + f"к.{self.cabinet}"

    class Meta:
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпусы'

class Employee(models.Model):
    displayName = models.CharField('ФИО', max_length=150)
    mail = models.EmailField('Почта', max_length=100)
    position = models.CharField('Должность', max_length=150)
    employeeId = models.CharField('Идентификатор 1С', max_length=20)
    inter_phone = models.CharField('Внутренный телефон', max_length=30)
    ext_phone = models.CharField('Внешний телефон', max_length=20)
    building = models.ForeignKey(Building, on_delete = models.PROTECT)
    subdivision = models.ForeignKey(Subdivision, on_delete = models.PROTECT)
    visible = models.BooleanField('Видимость')

    def __str__(self):
        return f"{self.displayName}"

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'