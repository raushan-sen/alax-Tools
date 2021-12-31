from django.db import models
import os
# Create your models here.
class Files(models.Model):
    Feature_image=models.FileField(upload_to='static/alax')

    def delete(self, *args, **kwargs):
        self.Feature_image.delete()
        self.os.remove(Feature_image.name)
        super().delete(*args, **kwargs)

class All_File(models.Model):
    File_link=models.TextField(default='00000',blank=True,null=True)
    FileName=models.TextField(default='000000',blank=True,null=True)
    
class FirebaseStorage(models.Model):
    apiKey=models.TextField(default='dsfc',blank=True,null=True)
    authDomain=models.TextField(default='dsfc',blank=True,null=True)
    databaseURL=models.TextField(default='dsfc',blank=True,null=True)
    storageBucket=models.TextField(default='dsfc',blank=True,null=True)
