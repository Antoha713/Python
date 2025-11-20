from django.db import models

class cars_brand(models.Model):
    BRAND_NAME = models.CharField(max_length=100)
    BRAND_COUNTRY = models.CharField(max_length=100)
    BRAND_RATING = models.IntegerField()

    def __str__(self):
        return self.BRAND_NAME

