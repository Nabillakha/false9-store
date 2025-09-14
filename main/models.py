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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    thumbnail = models.URLField(blank=True, null=True) #boleh kosong
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jersey')
    is_featured = models.BooleanField(default=False)
    sold = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    @property
    def is_product_bestseller(self):
        return self.sold > 750
        
    def increment_solds(self):
        self.sold += 1
        self.stock -= 1
        self.save()