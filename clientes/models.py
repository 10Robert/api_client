from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=50, )
    cpf = models.CharField( max_length=14, unique=True)
    rg = models.CharField(max_length=9)
    celular = models.CharField(max_length=14)
    ativo = models.BooleanField()
    foto = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nome
    
