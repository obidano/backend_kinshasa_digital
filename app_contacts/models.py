from datetime import datetime

from django.db import models


# Create your models here.
class Contacts(models.Model):
    nom = models.CharField(max_length=255, blank=True)
    prenom = models.CharField(max_length=255, blank=True)
    postnom = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    societe = models.CharField(max_length=255, blank=True)
    birthdate = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

    class Meta:
        db_table = 'tbl_contacts'
