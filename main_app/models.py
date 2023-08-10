from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
    
class Chat(models.Model):
    members = models.ManyToManyField(User, related_name ='chat_rooms')
    product = models.ForeignKey(Product)

class Message(models.Model):
    room = models.ForeignKey(Chat, related_name= 'message', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=255)
    user = models.OneToOneField(User)

class Address(models.Model):
   city = models.CharField(max_length=255)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.ForeignKey(Address, on_delete=models.PROTECT)
    birth_date = models.DateField(null=True, blank=True)

