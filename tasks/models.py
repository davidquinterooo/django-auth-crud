from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # TextField ideal para textos mas grandes 
    # blank=True el valor puede quedarse vacio
    created = models.DateTimeField(auto_now_add=True)
    # Permite guardar la fecha y la hora
    # auto_now_add por defecto se agregara la fecha
    dateCompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' by - ' + self.user.username
    #Se muestra el contenido de titulo