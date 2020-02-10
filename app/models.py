from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField()
    avatar = models.FileField(upload_to="avatars/")

    def __str__(self):
        return self.name
    