from django.db import models
from django.contrib.auth.models import User

def return_path(instance, filename):
    return 'profile_access/{0}_train_data/{1}'.format(instance.user.username, filename)

class AcousticModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=50)
    audio_data = models.FileField(null=True,upload_to=return_path)
    sampling_rate = models.IntegerField()
    audio_format = models.CharField(max_length=10)

    def __str__(self):
        return self.model_name
