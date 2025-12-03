from django import forms
from .models import ItemEstoque

# Create your forms here.

class ItemEstoqueForm(forms.ModelForm):
    class Meta:
        model = ItemEstoque
        fields = [
            'nome', 
            'quantidade', 
            'descricao',
            'localizacao', 
            'categoria', 
            'donoprenome', 
            'donosobrenome'
        ]   