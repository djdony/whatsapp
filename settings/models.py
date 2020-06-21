from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _


class Country(TimeStampedModel, models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=100, db_index=True)
    currency = models.CharField(max_length=3)
    status = models.BooleanField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')


class Region(TimeStampedModel, models.Model):
    name = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=1)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='region')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Region')
        verbose_name_plural = _('Regions')


class City(TimeStampedModel, models.Model):
    name = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=1)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, related_name='city')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')


class CompanyType(TimeStampedModel, models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True)
    status = models.BooleanField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Company Type')
        verbose_name_plural = _('Company Types')


class Company(TimeStampedModel, models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    whatsapp = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=200)
    www = models.URLField(null=True, blank=True)
    logo = models.ImageField(upload_to='company', null=True, blank=True)
    status = models.BooleanField(default=1)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='company')
    company_type = models.ForeignKey(CompanyType, on_delete=models.PROTECT, related_name='company')
    users = models.ManyToManyField(User, blank=True, related_name='companies')

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

