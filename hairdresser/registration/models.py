from django.db import models

from django.utils.translation import gettext as _

# Create your models here.


class Salon(models.Model):
    """
    A class to represents salon model.
    """

    name = models.CharField(max_length=50, verbose_name=_('Salon name'))
    address = models.CharField(max_length=50, verbose_name=_('Address'))
    phone_number = models.CharField(max_length=12, verbose_name=_('Phone number'))
    open_from = models.TimeField(verbose_name=_('Open from'))
    open_to = models.TimeField(verbose_name=_('Open to'))
    active = models.BooleanField(default=True, verbose_name=_('Is active'))
    employees = models.ManyToManyField('auth.User', verbose_name=_('Assigned employees'))

    def __str__(self):
        return f'{self.name}'

    class Meta:

        verbose_name = _('Salon')
        verbose_name_plural = _('Salons')


class Service(models.Model):
    """
    A class to represents service model.
    """

    name = models.CharField(max_length=50, verbose_name=_('Service name'))
    time = models.TimeField(verbose_name=_('Executing time'))
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
    employee = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=_('Employee'))
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, verbose_name=_('_Salon'))
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name=_('Service'))
    start = models.DateTimeField(verbose_name=_('From'))
    stop = models.DateTimeField(verbose_name=_('To'))
    client_name = models.CharField(max_length=50, verbose_name=_('Client name'))
    client_phone_number = models.CharField(max_length=12, verbose_name=_("Client's phone number"))
    finished = models.BooleanField(default=False, verbose_name=_('Is finished'))

    discount = models.DecimalField(max_length=5, decimal_places=2, blank=True, verbose_name=_('Discount'))
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('Price'))

    class Meta:
        verbose_name = _('Visit')
        verbose_name_plural = _('Visits')
