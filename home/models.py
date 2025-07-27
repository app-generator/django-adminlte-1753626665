# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Device Groups(models.Model):

    #__Device Groups_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    divicegroupname = models.TextField(max_length=255, null=True, blank=True)

    #__Device Groups_FIELDS__END

    class Meta:
        verbose_name        = _("Device Groups")
        verbose_name_plural = _("Device Groups")


class Deviceusers(models.Model):

    #__Deviceusers_FIELDS__
    dpassword = models.TextField(max_length=255, null=True, blank=True)

    #__Deviceusers_FIELDS__END

    class Meta:
        verbose_name        = _("Deviceusers")
        verbose_name_plural = _("Deviceusers")


class Devices(models.Model):

    #__Devices_FIELDS__
    deviceip = models.TextField(max_length=255, null=True, blank=True)
    devicemanage = models.TextField(max_length=255, null=True, blank=True)
    deviceuser = models.ForeignKey(DeviceUsers, on_delete=models.CASCADE)
    devicegroup = models.ForeignKey(Device Groups, on_delete=models.CASCADE)

    #__Devices_FIELDS__END

    class Meta:
        verbose_name        = _("Devices")
        verbose_name_plural = _("Devices")



#__MODELS__END
