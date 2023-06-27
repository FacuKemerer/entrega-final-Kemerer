from django import forms

class cliente_form(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    telefono = forms.IntegerField()

class auto_form(forms.Form):
    nombre_cliente = forms.CharField(max_length=20)
    apellido_cliente = forms.CharField(max_length=20)
    patente = forms.CharField(max_length=10)

class historia_form(forms.Form):
    patente = forms.CharField(max_length=10)
    descripcion = forms.CharField(widget=forms.Textarea())

class buscar_auto(forms.Form):
    patente = forms.CharField(max_length=10)
    