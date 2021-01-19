from django.db import models
from django.urls import reverse


class Contact(models.Model):
    """Модель контактов"""
    full_name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.id})

    class Meta:
        ordering = ('full_name',)
