from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from aero_mx.models.hangar import Hangar
from mjg_base.services import auth_service, utility_service
from mjg_base.classes.log import Log
from mjg_base.decorators import require_authentication
from aero_mx.models.aircraft import AircraftCategory, AircraftMake, AircraftModel, AircraftAttribute, Aircraft

log = Log()


@require_authentication()
def home(request):
    utility_service.clear_breadcrumbs()
    user = auth_service.get_user()
    hangar = Hangar.get_by_user(user)

    if not hangar:
        log.info(f"Creating hangar for {user} (#{user.id})")
        hangar = Hangar()
        hangar.owner = user.django_user()
        hangar.save()



    return render(
        request,
        "aero_mx/hangar/home.html",
        {
            "hangar": hangar,
        }
    )


@require_authentication()
def add_aircraft(request):
    utility_service.add_breadcrumb("Hangar", "hangar:home", "fal fa-warehouse")
    utility_service.add_breadcrumb("Add Aircraft", "hangar:add_aircraft", "fal fa-plane")

    categories = AircraftCategory.objects.all().order_by("title")

    if request.method == "POST":
        pass

    else:
        return render(
            request, "aero_mx/hangar/add_aircraft.html",
            {"categories": categories}
        )



