from django.db import models

class Blogs(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    images = models.ImageField()

    def __str__(self):
        return self.title