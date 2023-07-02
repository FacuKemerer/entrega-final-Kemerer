from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.IntegerField()

    def __str__(self):
        return f"{self.apellido} {self.nombre}"

class Auto(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    patente = models.TextField(max_length=7)

    def __str__(self):
        return f"{self.cliente} - Patente: {self.patente}"

class HistorialTrabajos(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, null=False)
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.auto} del {self.fecha}" 

