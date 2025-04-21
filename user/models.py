from django.db import models

# Create your models here.
class Product(models.Model):
    productname=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.productname}---{self.id}"
    
class Customer(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}"
    
class Reviews(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True, blank=True,  related_name='reviews')
    rating = models.CharField(max_length=10)
    review = models.TextField(blank=True)
    created_by = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_reviews')
    updated_by = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rating}---{self.created_by}----{self.id}"