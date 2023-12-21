import shortuuid
from django.db import models


def gen_uuid():
    return shortuuid.ShortUUID().random(length=13) + 'AP'

class Airplane(models.Model):
    uid = models.CharField(max_length=15, primary_key=True, unique=True, default=gen_uuid)
    id = models.PositiveIntegerField(default=1)
    passenger = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id, self.passenger}"
