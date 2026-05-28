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

class CollectionMovies(models.Model):
    Show_ID = models.CharField(max_length=20)
    Type = models.CharField(max_length=20)
    Title = models.CharField(max_length=200)
    Director = models.CharField(max_length=200, blank=True, null=True)
    Country = models.CharField(max_length=100, blank=True, null=True)
    Date_Added = models.CharField(max_length=50, blank=True, null=True)
    Release_Year = models.IntegerField()
    Rating = models.CharField(max_length=20)
    Duration = models.CharField(max_length=20, blank=True, null=True)
    Listed_In = models.CharField(max_length=300)
    def __str__(self):
        return self.Title
