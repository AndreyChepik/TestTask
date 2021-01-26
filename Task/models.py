from django.db import models

class ClassifierModel(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

