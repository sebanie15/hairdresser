from __future__ import annotations

from django.db import models


# Create your models here.


class Employee(models.Model):
    """
    A class to represents employee model.
    """
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, verbose_name='imię')
    last_name = models.CharField(max_length=30, verbose_name='nazwisko')
    email_address = models.EmailField(verbose_name='email')
    phone_number = models.CharField(max_length=12, verbose_name='numer telefonu')
    is_employed = models.BooleanField(default=True, verbose_name='zatrudniony')

    class Meta:
        ordering = ('first_name', 'last_name')
        verbose_name = 'Pracownik'
        verbose_name_plural = 'Pracownicy'
        unique_together = ('user', 'email_address')


class Salon(models.Model):
    """
    A class to represents salon model.
    """
    name = models.CharField(max_length=50, verbose_name='nazwa')
    address = models.CharField(max_length=50, verbose_name='adres')
    phone_number = models.CharField(max_length=12, verbose_name='numer telefonu')
    open_from = models.TimeField(verbose_name='otwarcie')
    open_to = models.TimeField(verbose_name='zamknięcie')
    employees = models.ManyToManyField(Employee)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Salony'


class Service(models.Model):
    """
    A class to represents service model.
    """
    name = models.CharField(max_length=50, verbose_name='nazwa usługi')
    service_length = models.IntegerField(default=30, verbose_name='czas trwania [min]')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='cena')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('name', 'service_length', 'price')
        verbose_name = 'Usługa'
        verbose_name_plural = 'Usługi'


class Visit(models.Model):
    """
    A class to represents visit model.
    """
    employee = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
    start = models.DateTimeField()
    stop = models.DateTimeField()
    client_name = models.CharField(max_length=50, verbose_name='imię i nazwisko')
    client_phone_number = models.CharField(max_length=9, verbose_name='numer kontaktowy')
    discount = models.CharField(max_length=20, verbose_name='rabat')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='cena')

    class Meta:
        verbose_name = 'Wizyta'
        verbose_name_plural = 'Wizyty'
