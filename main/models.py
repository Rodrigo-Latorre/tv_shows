from django.db import models
 
class Signup (models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=25)
    allowed = models.BooleanField(default=True)
    avatar = models.ImageField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/User_icon_2.svg/48px-User_icon_2.svg.png')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Networks (models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Shows (models.Model):
    title = models.CharField(max_length=255)
    network = models.ForeignKey(Networks, related_name="shows", on_delete = models.CASCADE)
    descr = models.TextField()
    release_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)