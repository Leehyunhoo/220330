from django.db import models

# Create your models here.

class Post(models.Model):
    file = models.FileField(upload_to='post_images')
    
    def __str__(self):
        return self.title