from .models import Name, Fam, Otc, Street, MainItem
from django.forms.models import ModelForm
import django.forms as forms
class NameForm(ModelForm):
    class Meta:
        model = Name
        fields = '__all__'
        widgets = {
            'val': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),
        }
        
class FamForm(ModelForm):
    class Meta:
        model = Fam
        fields = '__all__'
        widgets = {
            'val': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),
        }
class OtcForm(ModelForm):
    class Meta:
        model = Otc
        fields = '__all__'
        widgets = {
            'val': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),
        }
class StreetForm(ModelForm):
    class Meta:
        model = Street
        fields = '__all__'
        widgets = {
            'val': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),
        }
class MainItemForm(ModelForm):
    class Meta:
        model = MainItem
        fields = '__all__'
        widgets = {
            'bldn': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),
            'bldn_k': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),
            'appr': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),
            'tel': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 165px;'}),
            'fam': forms.Select(attrs={'class': 'form-select', 'style': 'width: 120px;'}),
            'name': forms.Select(attrs={'class': 'form-select', 'style': 'width: 100px;'}),
            'otc': forms.Select(attrs={'class': 'form-select', 'style': 'width: 130px;'}),
            'street': forms.Select(attrs={'class': 'form-select', 'style': 'width: 130px;'}),
            
        }