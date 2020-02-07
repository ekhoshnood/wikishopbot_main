from django.contrib import admin
from .models import Senf, SaleType, Channel, Post, MyModelAdmin


admin.site.register(Senf)
admin.site.register(SaleType)
admin.site.register(Channel, MyModelAdmin)
admin.site.register(Post)
