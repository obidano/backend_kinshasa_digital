import json
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
import re

# Create your views here.
from app_contacts.models import Contacts


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
        return JsonResponse(dict(msg=msg, status=0), safe=False, status=500)

    # mail validation
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        msg = "L'adresse mail n'est pas valide"
        return JsonResponse(dict(msg=msg, status=0), safe=False, status=500)

    # check length and startswith
    if len(phone) < 13 or not phone.startswith(+243):
        msg = "La longeur du numero n'est pas correcte " \
              "ou le numero ne commence pas par +243"
        return JsonResponse(dict(msg=msg, status=0), safe=False, status=500)

    authorized_network = ["89", "88", "90", "81", "84", "99", "97", "82"]
    prefix_phone = phone[-9:][:2]

    if not prefix_phone in authorized_network:
        msg = "Ce numero ne fait pas partie des reseaux autorisés en RDC"
        return JsonResponse(dict(msg=msg, status=0), safe=False, status=500)

    newData = Contacts(**data)
    newData.created_at = datetime.now()
    newData.save()

    return JsonResponse(dict(msg="Creation reussie", id=newData.pk, status=1), safe=False)


def update_contact(req):
    data = json.loads(req.body)
    nom = data.get('nom')
    prenom = data.get('prenom')
    email = data.get('email')
    phone = data.get('phone')
    societe = data.get('societe')
    id = data.get('id')

    query = Contacts.objects.filter(id=id)
    if not query.exists():
        msg = "L'ID de ce contact n'existe pas"
        return JsonResponse(dict(msg=msg, status=0), safe=False, status=500)
    # check required fields
    if not nom or not prenom or not email or not phone or not societe:
        msg = "Un des champs obligatoires est manquant"
        return JsonResponse(dict(msg=msg, status=0), safe=False, status=500)

    # mail validation
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        msg = "L'adresse mail n'est pas valide"
        return JsonResponse(dict(msg=msg, status=0), safe=False, status=500)

    # check length and startswith
    if len(phone) < 13 or not phone.startswith(+243):
        msg = "La longeur du numero n'est pas correcte " \
              "ou le numero ne commence pas par +243"
        return JsonResponse(dict(msg=msg, status=0), safe=False, status=500)

    authorized_network = ["89", "88", "90", "81", "84", "99", "97", "82"]
    prefix_phone = phone[-9:][:2]

    if not prefix_phone in authorized_network:
        msg = "Ce numero ne fait pas partie des reseaux autorisés en RDC"
        return JsonResponse(dict(msg=msg, status=0), safe=False, status=500)

    del data['updated_at']
    query.update(updated_at=datetime.now(), **data)
    return JsonResponse(dict(msg="Mise à jour reussie", status=1), safe=False)


def delete_contact(req, id):
    query = Contacts.objects.filter(id=id)
    if not query.exists():
        msg = "L'ID de ce contact n'existe pas"
        return JsonResponse(dict(msg=msg, status=0), safe=False, status=500)

    query.delete()
    return JsonResponse(dict(msg="Suppression reussie", status=1), safe=False)
