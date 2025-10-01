# Create your models here.
import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),            # jersey klub, timnas, retro
        ('boots', 'Football Boots'),     # sepatu bola / futsal
        ('training', 'Training Gear'),   # kaos latihan, celana training, vest
        ('accessories', 'Accessories'),  # sarung tangan, shin guard, headband
        ('ball', 'Football'),            # bola official & latihan
        ('lifestyle', 'Lifestyle'),      # hoodie, tshirt, casual wear
        ('collectibles', 'Collectibles'),# scarf, poster, merchandise
        ('others', 'Others'),            # kategori lain-lain
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    thumbnail = models.URLField(blank=True, null=True) #boleh kosong
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jersey')
    is_featured = models.BooleanField(default=False) #apakah produk ini termasuk produk unggulan
    sold = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    view = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    @property
    def is_product_bestseller(self):
        return self.sold > 750
    
    @property
    def is_product_available(self):
        return self.stock > 0
    
    @property
    def is_product_is_trending(self):
        return self.view > 500
    
    def increment_views(self):
        self.view += 1
        self.save()
        
    def increment_solds(self):
        self.sold += 1
        self.stock -= 1
        self.save()