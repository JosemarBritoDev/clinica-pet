from django.db import models
#from localflavor.br.br_states import STATE_CHOICES

class EnderecoCliente(models.Model):
    rua = models.CharField(max_length=100, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    complemento = models.CharField(max_length=100, null=False, blank=False)
    bairro = models.CharField(max_length=100, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
  #  estado = models.CharField(max_length=2, choices=STATE_CHOICES)
    cep = models.CharField(max_length=100, null=False, blank=False)


class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)

