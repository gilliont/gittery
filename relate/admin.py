# -*- coding: utf-8 -*-

from django.contrib import admin
from relate.models import Program, Price, Order

admin.site.register(Program)
admin.site.register(Order)
admin.site.register(Price)