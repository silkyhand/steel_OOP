from django import forms
from products.models import Product
# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
UNIT_CHOICES = (
    ("t", "т"),
    ("m", "м"),
)


class CartAddProductForm(forms.ModelForm):
    quantity = forms.IntegerField() # TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    unit = forms.ChoiceField(choices=UNIT_CHOICES)

    def clean_quantity(self):
        quantity = int(self.cleaned_data['quantity'])
        length = int(self.cleaned_data['length'])
        unit = self.cleaned_data.get('unit')

        if unit == 'm' and (quantity % length != 0):
            raise forms.ValidationError('Введите значение кратное длине')
        return quantity

    class Meta:        
        model = Product        
        fields = ('length',) 

 