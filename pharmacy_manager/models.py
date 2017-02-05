from django.db import models

# Create your models here.


class Drug(models.Model):
    drug_name = models.CharField(max_length=100)
    description = models.TextField()
    manufacturer = models.CharField(max_length=50)
    code = models.CharField(max_length=20)
    exp_date = models.CharField(max_length=20)
    thumb_nail = models.ImageField(upload_to='photos/')