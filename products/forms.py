from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import Comment , Contact
from phonenumber_field.widgets import PhoneNumberPrefixWidget

PAYMENT_CHOICES = [
    ('S','Saman'),
    ('M','Melli')
]



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields =['name','number','email','text',]
        widgets = {
           'phone': PhoneNumberPrefixWidget(initial='IR'),
        }

        
class CheckoutForm(forms.Form):
    apartment_address = forms.CharField(widget = forms.TextInput(attrs={
        'class':"form__input form__input--2",
        'placeholder':'1234 APARTMENT'
    }))

    descript =forms.CharField(widget = forms.Textarea)
    country = CountryField(blank_label='-----(select country)------').formfield(widget=CountrySelectWidget())
    number = forms.IntegerField(widget = forms.TextInput(attrs={
        'class':"form__input form__input--2",
        'placeholder':'0912456'
    }))

    f_name = forms.CharField(widget = forms.TextInput(attrs={
        'class':"form__input form__input--2",
        'placeholder':'امیرحسین '
    }))

    l_name = forms.CharField(widget = forms.TextInput(attrs={
        'class':"form__input form__input--2",
        'placeholder':'رحیمی'
    }))

    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES)



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =['text','recommend',]


class PaymentForm(forms.Form):
    card_number = forms.IntegerField(required=True)

    
    
