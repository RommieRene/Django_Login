from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField('Category name', max_length=60)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'
    
   
class Product(models.Model):

    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='cat_prod')
    name = models.CharField('Product name', max_length=50)
    price = models.PositiveIntegerField('Product price')
    img = models.ImageField('product image',upload_to='home_images')
    about = models.TextField('about product')
    slug = models.SlugField('product slug', unique=True)
    
    
    def __str__(self):
        return self.name
    
    



class Contact(models.Model):

    email = models.EmailField('Contact email')
    phone = models.CharField('Contact phone', max_length=40)
    subject = models.CharField('Contact subject',max_length=50)
    message = models.TextField('Contact message')

    def __str__(self):
        return self.email
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)