from django.db import models
from django.db.models import Model
from django.core.exceptions import ObjectDoesNotExist

class ProductIDField(models.CharField):

    description = "Unique product identifier"

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 50
        kwargs["unique"] = True
        super(self).__init__(*args, **kwargs)

class OrderField(models.PositiveIntegerField):
    def pre_save(self, model_instance: Model, add: bool):
        # if we don't include the order
        if getattr(model_instance, self.attname) is None:
            try:
                obj = self.model.objects.lastest(self.attname)
                value = obj.order + 1
            except ObjectDoesNotExist:
                value = 1
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)