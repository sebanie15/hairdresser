from django.db import models

from django.utils.translation import gettext as _

# Create your models here.


class Employee(models.Model):
    """
    A class to represents employee model.
    """

    first_name = models.CharField(max_length=30, verbose_name=_('First name'))
    last_name = models.CharField(max_length=30, verbose_name=_('Last name'))
    email_address = models.EmailField(unique=True, verbose_name=_('email address'))
    phone_number = models.CharField(max_length=12, verbose_name=_('phone number'))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:

        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')


class Salon(models.Model):
    """
    A class to represents salon model.
    """

    name = models.CharField(max_length=50, verbose_name=_('Salon name'))
    address = models.CharField(max_length=50, verbose_name=_('Address'))
    phone_number = models.CharField(max_length=12, verbose_name=_('Phone number'))
    open_from = models.TimeField(verbose_name=_('Open from'))
    open_to = models.TimeField(verbose_name=_('Open to'))
    employees = models.ManyToManyField(Employee, verbose_name=_('Assigned employees'))

    def __str__(self):
        return f'{self.name}'

    class Meta:

        verbose_name = _('Salon')
        verbose_name_plural = _('Salons')


# class SalonEmployee(models.Model):
#     """
#     A class to represents employee and salon models relationships.
#     """
#     employee = models.ManyToManyField(Employee)
#     salon = models.ManyToManyField(Salon)


class Service(models.Model):
    """
    A class to represents service model.
    """

    name = models.CharField(max_length=50, verbose_name=_('Service name'))
    time = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('Executing time'))
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('Price'))

    def __str__(self):
        return f'{self.name}'

    class Meta:

        verbose_name = _('Service')
        verbose_name_plural = _('Services')


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
    client_phone_number = models.CharField(max_length=12)

    discount = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Wizyta"
        verbose_name_plural = "Wizyty"
