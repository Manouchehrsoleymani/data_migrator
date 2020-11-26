from django.db import models

# Create your models here.
class Network_destination(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')
    name=models.CharField(max_length = 100)
    path=models.CharField(max_length = 200)
    user=models.CharField(max_length = 50, blank=True)
    password=models.CharField(max_length = 50, blank=True   )
    protocol = models.CharField(max_length=50)

class Source_path(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')
    name=models.CharField(max_length = 100)
    path=models.CharField(max_length = 255)
    