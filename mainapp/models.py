from django.db import models

# Create your models here.
class RecommendationHistory(models.Model):
    requested = models.CharField(100)
    rating = models.CharField(20, default='Not Rated')
    rec_1 = models.CharField(100)
    rec_2 = models.CharField(100)
    rec_3 = models.CharField(100)
    rec_4 = models.CharField(100)
    rec_5 = models.CharField(100)
    rec_6 = models.CharField(100)
    rec_7 = models.CharField(100)
    rec_8 = models.CharField(100)
    rec_9 = models.CharField(100)
    rec_10 = models.CharField(100)
    created_at = models.DateTimeField(auto_now_add=True)

