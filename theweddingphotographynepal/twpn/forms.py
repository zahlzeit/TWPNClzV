# from django import forms
# from django.forms import fields, models, widgets
# from .models import Service

# class PostService(forms.ModelForm):
#     class Meta():
#         model = Service
#         fields = ('vendor_id', 'service_name', 'service_price', 'service_desc')

#         widgets = {
#             'vendor_id': forms.Select(attrs={'class': 'data'}),
#             'service_name': forms.TextInput(attrs={'class': 'data'}),
#             'service_price': forms.FloatField(attrs={'class': 'data'}),
#             'service_desc': forms.TextInput(attrs={'class': 'data'}),
#         }