from django.db import models

# Create your models here.
class Gif(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    uploader_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.uploader_name}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    gifs = models.ManyToManyField(Gif, related_name="categories")

    def __str__(self) -> str:
        return f'{self.name}'


# Gif.objects.create(title = 'red_clown',url = '',uploader_name = 'YUri')




