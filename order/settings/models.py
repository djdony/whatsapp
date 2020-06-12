from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_extensions.db.models import TimeStampedModel


class Country(TimeStampedModel, models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=100)
    currency = models.CharField(max_length=2)
    status = models.BooleanField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class Region(TimeStampedModel, models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=1)
    country_id = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='region')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'


class City(TimeStampedModel, models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=1)
    region_id = models.ForeignKey(Region, on_delete=models.PROTECT, related_name='city')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class CompanyType(TimeStampedModel, models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company Type'
        verbose_name_plural = 'Company Types'


class Company(TimeStampedModel, models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=200, null=True, blank=True)
    whatsapp = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=200)
    www = models.URLField(null=True)
    logo = models.ImageField(upload_to='uploads/company', null=True, blank=True)
    status = models.BooleanField(default=1)
    city_id = models.ForeignKey(Region, on_delete=models.PROTECT)
    company_type_id = models.ForeignKey(CompanyType, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

