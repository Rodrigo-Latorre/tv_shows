from django.db import models
 
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