from PIL import Image
from django.db import models
from django.contrib.auth.models import User

def return_path(instance, filename):
    return 'profile_access/{0}/{1}'.format(instance.user.username, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True)
    image = models.ImageField(default='blank.jpg', upload_to='profile_pics')

    
    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


#class Product(models.Model):
#    name = models.CharField(max_length=50)
#    price = models.DecimalField(max_digits=9, decimal_places=2)
#
#    def __str__(self):
#        return self.name

   
  
 

