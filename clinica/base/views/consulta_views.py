from django.shortcuts import redirect, render
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
