from django.db import models

class ClassifierModel(models.Model):
    """Model that stores input information"""
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.code
