from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.conf import settings

from clinica.base.decorators import cargo_requerido
from ..forms import consulta_forms
from ..services import pet_service, consulta_service
from ..entidades import consulta


# 🔒 Cargos permitidos: Administrador (0), Veterinário (1)
@cargo_requerido([0, 1])
def inserir_consulta(request, id):
    pet = pet_service.listar_pet_id(id)
    if request.method == "POST":
        form_consulta = consulta_forms.ConsultaPetForm(request.POST)
        if form_consulta.is_valid():
            motivo_consulta = form_consulta.cleaned_data["motivo_consulta"]
            peso_atual = form_consulta.cleaned_data["peso_atual"]
            avaliacao_medica = form_consulta.cleaned_data["avaliacao_medica"]
            medicamento_atual = form_consulta.cleaned_data["medicamento_atual"]
            medicamentos_prescritos = form_consulta.cleaned_data["medicamentos_prescritos"]
            exames_prescritos = form_consulta.cleaned_data["exames_prescritos"]

            consulta_nova = consulta.ConsultaPet(
                pet=pet,
                motivo_consulta=motivo_consulta,
                peso_atual=peso_atual,
                avaliacao_medica=avaliacao_medica,
                medicamento_atual=medicamento_atual,
                medicamentos_prescritos=medicamentos_prescritos,
                exames_prescritos=exames_prescritos
            )
            consulta_service.cadastrar_consulta(consulta_nova)
            return redirect('base:listar_pet_id', pet.id)
    else:
        form_consulta = consulta_forms.ConsultaPetForm()
    return render(request, 'consultas/form_consulta.html', {'form_consulta': form_consulta})


# 🔒 Cargos permitidos: todos (0, 1, 2, 3)
@cargo_requerido([0, 1, 2, 3])
def listar_consulta_id(request, id):
    consulta = consulta_service.listar_consulta(id)
    return render(request, 'consultas/lista_consulta.html', {'consulta': consulta})


# 🔒 Envio de email da consulta
@login_required
def enviar_consulta_email(request, id):
    consulta = consulta_service.listar_consulta(id)
    pet_consulta = pet_service.listar_pet_id(consulta.pet.id)

    assunto = f"Detalhes da Consulta do seu Pet {pet_consulta.nome}"
    corpo_email = "Resumo da consulta do seu pet."
    email_remetente = settings.EMAIL_HOST_USER
    email_destino = [pet_consulta.dono.email]

    html_conteudo = render_to_string(
        'consultas/consulta_email.html',
        {'consulta': consulta},
        request=request
    )

    try:
        send_mail(
            subject=assunto,
            message=corpo_email,
            from_email=email_remetente,
            recipient_list=email_destino,
            html_message=html_conteudo
        )
        messages.success(request, "Email enviado com sucesso!")
    except BadHeaderError:
        messages.error(request, "Erro ao enviar email. Cabeçalho inválido.")
    except Exception as e:
        messages.error(request, f"Erro ao enviar email: {str(e)}")

    return redirect('base:listar_consulta_id', id)
