from django import forms

class CartAddProductForm(forms.Form):
	PRODUCT_QUANTITY_CHOICES = [(i,str(i)) for i in range (1,10)]
	quantity = forms.TypedChoiceField(choices = PRODUCT_QUANTITY_CHOICES)
	update = forms.BooleanField(required = False,initial = False,widget = forms.HiddenInput)