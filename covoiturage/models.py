from django.db import models  # noqa: F401
from django.db import models

class Trajet(models.Model):
    conducteur = models.CharField(max_length=100) 
    ville_depart = models.CharField(max_length=100)
    ville_arrivee = models.CharField(max_length=100)
    date_depart = models.DateField()
    heure_depart = models.TimeField()
    places = models.IntegerField()
    prix_places = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return f"{self.ville_depart} -> {self.ville_arrivee} par {self.conducteur}"