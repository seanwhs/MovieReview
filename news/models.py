from django.db import models

# Create your models here.

class New(models.Model):
    headline = models.CharField(max_length=250)
    body = models.TextField()
    date = models.DateField()
    url_source = models.URLField(blank = True, null = True)

    def __str__(self):
        return self.headline[0:30]    
