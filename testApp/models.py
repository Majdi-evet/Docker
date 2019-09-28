# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Testmodel(models.Model):
    album = models.CharField(max_length=100)
    song = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
        return self.album