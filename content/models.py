from django.db import models

# Create your models here.
class Slamm(models.Model):
    name = models.CharField(max_length=50)
    blood = models.CharField(blank=False, max_length=10)
    t = models.CharField(blank=False, max_length=1000)
    mail = models.EmailField(blank=False, unique=True)
    address = models.CharField(blank=False, max_length=1000)
    contact = models.CharField(max_length=10, blank=False)
    contact1 = models.CharField(max_length=10, blank=True)


    def __str__(self):
        return self.mail
