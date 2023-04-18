from django import forms
from django.contrib.auth import get_user_model

from .models import Order, ProductInOrder

User = get_user_model()


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'phone', 'comments']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        if self.request and self.request.user.is_authenticated:
            self.fields['name'].initial = self.request.user.username
            self.fields['email'].initial = self.request.user.email
            self.fields['phone'].widget.attrs.update({'placeholder': 'Телефон'})
            self.fields['comments'].widget.attrs.update({'placeholder': 'Комментарий'})
        else:    
            self.fields['name'].widget.attrs.update({'placeholder': 'Имя'})            
            self.fields['email'].widget.attrs.update({'placeholder': 'Email'}) 
            self.fields['phone'].widget.attrs.update({'placeholder': 'Телефон'})      
            self.fields['comments'].widget.attrs.update({'placeholder': 'Комментарий'})
        


# # PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
# UNIT_CHOICES = (
#     ("t", "т"),
#     ("m", "м"),
# )


# class CartAddProductForm(forms.Form):
#     quantity = forms.IntegerField() # TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
#     update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
#     unit = forms.ChoiceField(choices=UNIT_CHOICES)
#     length = forms.IntegerField()

#     def __init__(self,  *args, **kwargs):
#         length = kwargs.pop('length')
#         super(CartAddProductForm, self).__init__(*args, **kwargs)
#         self.fields['length'].initial = length

#     def clean(self):
#         quantity = int(self.cleaned_data.get('quantity'))
#         length = int(self.cleaned_data.get('length'))
#         unit = self.cleaned_data.get('unit')

#         if unit == 'm' and (quantity % length != 0):
#             raise forms.ValidationError('Введите значение кратное длине')
