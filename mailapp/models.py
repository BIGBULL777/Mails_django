from django.db import models

# Create your models here.
class SendMail(models.Model):
    content = models.TextField(max_length = 100,null = True)
    Email = models.CharField(max_length=50)
    image = models.ImageField(upload_to=None,null = True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Email
    