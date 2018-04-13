# -*- coding: utf-8 -*-

from django.db import models
from django.template.defaultfilters import slugify



class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    views = models.IntegerField(blank=True, null=True, default=0)
    likes = models.IntegerField(blank=True, null=True, default=0)
    slug = models.SlugField(blank=True, null=True, unique=True)
    text = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('category_detail', kwargs={'pk':self.pk})
    #
    # def get_update_url(self):
    #     return reverse('category_update', kwargs={'pk':self.pk})

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
