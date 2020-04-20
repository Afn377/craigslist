from django.db import models

# Create your models here.

class Search(models.Model):
    search = models.CharField(max_length=580)
    created = models.TimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Searches'

    def __str__(self):
        return self.search