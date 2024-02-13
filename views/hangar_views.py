from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from aero_mx.models.hangar import Hangar
from mjg_base.services import auth_service
from mjg_base.classes.log import Log
from mjg_base.decorators import require_authentication

log = Log()


@require_authentication()
def home(request):
    user = auth_service.get_user()
    hangar = Hangar.get_by_user(user)

    if not hangar:
        log.info(f"Creating hangar for {user} (#{user.id})")
        hangar = Hangar()
        hangar.owner = user.django_user()
        hangar.save()

    return render(
        request,
        "aero_mx/home.html",
        {
            "hangar": hangar,
        }
    )
