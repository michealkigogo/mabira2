from django.db import models
from django.db import models
from django.core.files.storage import default_storage

class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)

    @property
    def image_url(self):
        if self.image and default_storage.exists(self.image.name):
            return self.image.url
        return '/static/images/default_item_image.jpg'  # Path to a default image

# Create your models here.
