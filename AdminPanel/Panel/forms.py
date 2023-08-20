from django import forms

from Panel.models import Food


class AddFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'p-2 border rounded'}),
            'category': forms.Select(attrs={'class': 'mt-2 mb-2 p-2 border rounded'}),
            'description': forms.Textarea(attrs={'class': 'h-10 p-2 border rounded', 'rows': 1}),
            'price': forms.NumberInput(attrs={'class': 'p-2 border rounded'}),
            'slug': forms.TextInput(attrs={'class': 'p-2 border rounded'}),
        }