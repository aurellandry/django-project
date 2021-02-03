from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.http import JsonResponse


""""
Affichage de la page 'Profil' qui recense toutes les
informations utilisateur
"""
@login_required
def profil(request):
    return render(request, 'profil/profil.html')

"""
Modification des informations utilisateur
"""
def updateUser(request):
    user = request.user

    if (request.method == "POST" and len(request.POST["email"]) > 0):
        user.email  = request.POST["email"]
        user.save()

        return JsonResponse({'email': user.email}, status=200)
    else:
        return JsonResponse(
            {
                "message": "Erreur interne"
            },
            status=500
        )
