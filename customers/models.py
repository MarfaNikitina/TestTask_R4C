from django.db import models


class Customer(models.Model):
    email = models.CharField(max_length=255, blank=False, null=False)
    name = models.CharField(max_length=255, blank=False, null=False, default='Nemo')

    def __str__(self):
        return self.name
