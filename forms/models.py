from django.db import models

class Form(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)