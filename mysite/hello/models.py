from django.db import models

class Santa(models.Model):
    name = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)

    class Meta:
        app_label = 'hello'