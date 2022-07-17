from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField



PRODUCT_CHOICES = [
    ('T','T-shirt'),
    ('J','Jeens'),
    ('S','Shoes')
]

PRODUCT_SIZE = [
    ('L','Large'),
    ('S','Small'),
    ('M','Medium')
]



class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    discount_price = models.IntegerField(blank=True,null=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='image/',blank=True,null=False)
    wear = models.CharField(choices=PRODUCT_CHOICES,max_length=1)
    size = models.CharField(choices=PRODUCT_SIZE, max_length=1)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', args =[self.id])

    def get_add_to_cart_url(self):
        return reverse('add-to-cart', args =[self.id])

    def get_remove_from_cart_url(self):
        return reverse('remove-from-cart', args =[self.id])




class OrderItem(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    item =models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
   

    def __str__(self):
        return f'{self.user}:{self.item}'

    def get_total_item_price_url(self):
        return self.quantity * self.item.price

    def reduce_quantity(self):
        if self.quantity > 1:
            self.quantity -= 1
            self.save()
        else:
            self.delete()


 

    
class Order(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now=True)
    ordered_date = models.DateTimeField(auto_now=True)
    ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey('BillingAddress',on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price_url()
        return total

    def reduce_order_item_quantity(self, item_pk):
        try:
            order_item = self.items.get(item_id=item_pk)
            order_item.reduce_quantity()
            return True
        except OrderItem.DoesNotExist:
            return False

class BillingAddress(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    descript = models.CharField( max_length=200)
    apartment_address = models.CharField(max_length=50)
    country = CountryField(multiple=False)
    number = models.IntegerField(blank=True)

    def __str__(self):
        return self.user.username
    

class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    new_comment = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    text = models.TextField()
    is_active = models.BooleanField(default = True)
    recommend = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    

class Contact(models.Model):
    name = models.CharField(max_length=50)
    number = PhoneNumberField()
    email = models.EmailField(max_length=254)
    text = models.TextField()

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('contact-us')
    



class Payment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, blank=True, null=True)
    cart_number = models.IntegerField()