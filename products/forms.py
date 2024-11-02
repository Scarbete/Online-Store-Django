from django import forms


class ProductCreateForms(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(max_length=255, min_length=6)
    description = forms.CharField(max_length=255, min_length=20)
    price = forms.FloatField(required=False)
    rate = forms.FloatField(required=False)


class CommentCreateForms(forms.Form):
    text = forms.CharField(max_length=255, min_length=3)