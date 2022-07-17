from django.contrib import admin
from .models import Product,OrderItem,Order,BillingAddress,Comment,Contact
from django import forms
from .forms import ContactForm




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','active']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'item',
        'quantity',
        'ordered',
    ]
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','new_comment','text','is_active','recommend','datetime_created')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    form = ContactForm
    list_display = ['name','number','email']


admin.site.register(Order)
admin.site.register(BillingAddress)

