from django.db import models
from mjg_base.classes.log import Log
from django.contrib.auth.models import User

log = Log()


class Hangar(models.Model):
    """
    A hangar belongs to one User and holds all their aircraft
    """
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(
        User, models.CASCADE, related_name="hangar", blank=False, null=False, unique=True, db_index=True
    )

    def aircraft(self):
        self.aircraft_set.all().order_by('year')

    @classmethod
    def get_by_user(cls, user):
        try:
            if user:
                user_id = user if str(user).isnumeric() else user.id
                return cls.objects.get(owner__id=user_id)
        except Exception as ee:
            log.debug(ee)

    @classmethod
    def get(cls, hangar_id):
        try:
            if hangar_id:
                return cls.objects.get(pk=hangar_id)
        except Exception as ee:
            log.debug(ee)


