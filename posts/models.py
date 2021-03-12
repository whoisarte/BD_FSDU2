from django.db import models

class Post(models.Model):
    nombre = models.TextField()
    correo = models.TextField(default = "")

    def __str__(self):
    	return self.text[:50]
