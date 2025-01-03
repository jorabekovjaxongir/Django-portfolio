from django.db import models

class Collection(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='collection/')

    def __str__(self) -> str:
        return self.title