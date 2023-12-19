from django.db import models
from django.contrib.auth.models import User

class Google_Captured_Image(models.Model):
    image = models.ImageField(upload_to='uploaded_images/google/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    zoom = models.IntegerField(default=0)
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)

    def __str__(self):
        return self.user + " " + str(self.uploaded_at)