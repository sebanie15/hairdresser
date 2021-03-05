from django.db import models

# Create your models here.


class Employee(models.Model):
    """
    A class to represents employee model.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=9)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Pracownik"
        verbose_name_plural = "Pracownicy"


class Salon(models.Model):
    """
    A class to represents salon model.
    """
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=9)
    open_from = models.TimeField()
    open_to = models.TimeField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Salony"


class SalonEmployee(models.Model):
    """
    A class to represents employee and salon models relationships.
    """
    employee = models.ManyToManyField(Employee)
    salon = models.ManyToManyField(Salon)


class Service(models.Model):
    """
    A class to represents service model.
    """
    name = models.CharField(max_length=50)
    time = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Usługa"
        verbose_name_plural = "Usługi"


class Visit(models.Model):
    """
    A class to represents visit model.
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
    start = models.DateTimeField()
    stop = models.DateTimeField()
    client_name = models.CharField(max_length=50)
    client_phone_number = models.CharField(max_length=9)
    discount = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Wizyta"
        verbose_name_plural = "Wizyty"
