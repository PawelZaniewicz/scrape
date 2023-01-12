from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Mpk(models.Model):
    ActiveType = models.TextChoices('ActiveType', 'AKTYWNY NIEAKTYWNY')
    name = models.CharField(max_length=10, verbose_name="Kod MPK")
    status = models.CharField(blank=True, choices=ActiveType.choices, max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('mpk')
        verbose_name_plural = _('mpk')


class Manager(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False, verbose_name="Imię")
    last_name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Nazwisko")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _('kierownik')
        verbose_name_plural = _('kierownicy')


class Plant(models.Model):
    plant_name = models.CharField(max_length=255, verbose_name="Nazwa wytwórni")
    mpk = models.ForeignKey(Mpk, on_delete=models.CASCADE, verbose_name="MPK")
    manager_wmb = models.ForeignKey(Manager, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Kierownik WMB")
    sn_computer = models.CharField(max_length=30, verbose_name="Komputer wagowy (S/N)")

    def __str__(self):
        return f"{self.plant_name} [ {self.mpk} ]  "

    class Meta:
        verbose_name = _('wytwórnia')
        verbose_name_plural = _('wytwórnie')