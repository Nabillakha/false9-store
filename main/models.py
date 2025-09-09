# Create your models here.
import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),            # jersey klub, timnas, retro
        ('boots', 'Football Boots'),     # sepatu bola / futsal
        ('training', 'Training Gear'),   # kaos latihan, celana training, vest
        ('accessories', 'Accessories'),  # sarung tangan, shin guard, headband
        ('ball', 'Football'),            # bola official & latihan
        ('lifestyle', 'Lifestyle'),      # hoodie, tshirt, casual wear
        ('collectibles', 'Collectibles') # scarf, poster, merchandise
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    thumbnail = models.URLField(blank=True, null=True) #boleh kosong
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jersey')
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    @property
    def is_news_hot(self):
        return self.news_views > 20
        
    def increment_views(self):
        self.news_views += 1
        self.save()