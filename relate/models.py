# -*- coding: utf-8 -*-

from django.db import models

class Program(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Price(models.Model):
    program = models.ForeignKey(Program)
    # from_date = models.DateTimeField()
    # to_date = models.DateTimeField()
    def __str__(self):		
        return("Price obj: {}").format(self.program)

class Order(models.Model):
    state = models.CharField(max_length=20)
    items = models.ManyToManyField(Price)

    def __str__(self):		
        return("Order obj: {}").format(self.state)


