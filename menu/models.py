# from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.

# class MenuItem(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     description = models.TextField(blank=True)
    
#     def __str__(self):
#         return self.name
    
# class Cart(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
    
    
# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
#     menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
    
#     def get_total_price(self):
#         return self.quantity * self.menu_item.price