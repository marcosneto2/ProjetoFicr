from django.db import models

# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Contato(models.Model):
        sno = models.AutoField(primary_key=True)
        name = models.CharField(max_length=50)
        email = models.CharField(max_length=50)
        numero = models.CharField(max_length=12)
        desc = models.TextField()
        time = models.DateTimeField(auto_now_add=True)