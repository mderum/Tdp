from django.db import models

# Create your models here.


class Deal(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()
    image=models.ImageField(default='images/default.jpg',upload_to='images/',blank=True,null=True)
    publish=models.DateField( auto_now_add=True)



    def __str__(self):
        return f' {self.title}'
