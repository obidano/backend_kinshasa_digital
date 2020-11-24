import json

from django.http import JsonResponse
from django.shortcuts import render
import re


# Create your views here.


def create_contact(req):
    data = json.loads(req.body)
    nom = data.get('nom')
    prenom = data.get('prenom')
    email = data.get('email')
    phone = data.get('phone')
    societe = data.get('societe')
    # check required fields
    if not nom or not prenom or not email or not phone or not societe:
        msg = "Un des champs obligatoires est manquant"
        return JsonResponse(dict(msg=msg), safe=False, status=500)

    # mail validation
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        msg = "L'adresse mail n'est pas valide"
        return JsonResponse(dict(msg=msg), safe=False, status=500)
    # check length and startswith
    if len(phone) < 13 or not phone.startswith(+243):
        msg = "La longeur du numero n'est pas correcte " \
              "ou le numero ne commence pas par +243"
        return JsonResponse(dict(msg=msg), safe=False, status=500)

