from django.db import models
from localflavor.br.br_states import STATE_CHOICES
from localflavor.br.validators import BRPostalCodeValidator


class BRZipCodeField(models.CharField):
    """
    Campo de modelo para CEP brasileiro (formato 00000-000 ou 00000000).
    Este campo é um invólucro mínimo sobre CharField que aplica BRPostalCodeValidator.
    """

    def __init__(self, *args, **kwargs):
        # CEP tem no máximo 9 caracteres quando formatado (#####-###)
        kwargs.setdefault('max_length', 9)
        # Garante que o validador de CEP seja aplicado
        validators = list(kwargs.pop('validators', []))
        validators.append(BRPostalCodeValidator())
        kwargs['validators'] = validators
        super().__init__(*args, **kwargs)


class EnderecoCliente(models.Model):
    rua = models.CharField(max_length=100, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    complemento = models.CharField(max_length=100, null=False, blank=False)
    bairro = models.CharField(max_length=100, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    estado = models.CharField(max_length=2, null=False, choices=STATE_CHOICES, blank=False)
    # Use o campo específico para CEP com validação apropriada
    cep = BRZipCodeField(null=False, blank=False)


class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    endereco = models.ForeignKey(EnderecoCliente, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
