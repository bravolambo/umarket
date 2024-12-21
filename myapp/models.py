from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    college=models.CharField(max_length=255 ,default='')
    block=models.CharField(max_length=255 ,default='')
    description = models.TextField()  # Set default value here
    image = models.ImageField(upload_to='product_images/', default='default.jpg')  # Set your default value here
    contact = models.CharField(max_length=15, blank=True, null=True)
    
    
    def __str__(self):
        return self.name

