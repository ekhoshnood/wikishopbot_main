from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.forms import CheckboxSelectMultiple

from django.db.models.signals import post_delete
from django.dispatch import receiver



class SaleType(models.Model):
    # wholesale or retail
    name                = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Senf(models.Model):
    #shoes, glassess or ...
    name                = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


# data list model
class Channel(models.Model):
    chat_id                 = models.IntegerField(blank=True, null=True, unique=True)
    admin_id                = models.IntegerField(blank=True, null=True)
    admin_user              = models.CharField(max_length=50, null=True)
    chat_title              = models.CharField(max_length=50, blank=True)
    chat_username           = models.CharField(max_length=50)
    phone                   = models.IntegerField(null=True)
    date_purchased          = models.DateField(auto_now_add=True) # TODO: date field will be added when purchasing with this (datetime.datetime.today().date())
    is_purchased            = models.BooleanField(default=True)
    saletype                = models.ManyToManyField(SaleType)
    senf                    = models.ManyToManyField(Senf)

    def __str__(self):
        return self.chat_username


class Post(models.Model):
    channel                 = models.ForeignKey(Channel, on_delete=models.CASCADE)
    message_id              = models.IntegerField(blank=True, null=True)
    date                    = models.IntegerField(blank=True, null=True)
    text                    = models.TextField(max_length=5000, null=True)
    price                   = models.IntegerField(blank=True, null=True)
    image                   = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.message_id)

@receiver(post_delete, sender=Post)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
