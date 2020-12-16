from django.shortcuts import render
from django.http import JsonResponse
from . dashboard_serializer_cumplimientos import *
# Create your views here.

###################################################################################
###############################INDEX###############################################
###################################################################################

#@login_required(login_url=login_required_ruta)
def index(request):
    return render(request, "dashboardventas/cumplimiento.html")  

####################################################################################
###############################DISTRIBUIDORAS#######################################
####################################################################################       

#@login_required(login_url=login_required_ruta)
def jsonCump(request):
    jsonData = json_parser_cump()
    return JsonResponse(jsonData, safe=False)

#@login_required(login_url=login_required_ruta)
def jsonCumpEntero(request):
    jsonData = json_parser_cump_entero()
    return JsonResponse(jsonData, safe=False)

#@login_required(login_url=login_required_ruta)
def jsonCumpDespresado(request):
    jsonData = json_parser_cump_despresado()
    return JsonResponse(jsonData, safe=False)

#@login_required(login_url=login_required_ruta)
def jsonCumpFiletes(request):
    jsonData = json_parser_cump_filetes()
    return JsonResponse(jsonData, safe=False)

#@login_required(login_url=login_required_ruta)
def jsonCumpEmbutidos(request):
    jsonData = json_parser_cump_embutidos()
    return JsonResponse(jsonData, safe=False)

#@login_required(login_url=login_required_ruta)
def jsonCumpCongelados(request):
    jsonData = json_parser_cump_congelados()
    return JsonResponse(jsonData, safe=False) 

#@login_required(login_url=login_required_ruta)
def jsonCumpHuevosConsumo(request):
    jsonData = json_parser_cump_huevosconsumo()
    return JsonResponse(jsonData, safe=False) 

#@login_required(login_url=login_required_ruta)
def jsonCumpPollitosBB(request):
    jsonData = json_parser_cump_pollitos_bb()
    return JsonResponse(jsonData, safe=False)

#@login_required(login_url=login_required_ruta)
def jsonCumpPollonaPonedora(request):
    jsonData = json_parser_pollonas_ponedora()
    return JsonResponse(jsonData, safe=False)

#@login_required(login_url=login_required_ruta)
def jsonCumpPollonaVivo(request):
    jsonData = json_parser_pollo_vivo()
    return JsonResponse(jsonData, safe=False)

#@login_required(login_url=login_required_ruta)
def jsonCumpHuevoFeretil(request):
    jsonData = json_parser_huevo_fertil()
    return JsonResponse(jsonData, safe=False)

#@login_required(login_url=login_required_ruta)
def jsonCumpAbaComercial(request):
    jsonData = json_parser_aba_comercial()
    return JsonResponse(jsonData, safe=False)

#@login_required(login_url=login_required_ruta)
def jsonCumpMascotas(request):
    jsonData = json_parser_mascotas()
    return JsonResponse(jsonData, safe=False)  

#@login_required(login_url=login_required_ruta)
def jsonCumpLacteos(request):
    jsonData = json_parser_lacteos()
    return JsonResponse(jsonData, safe=False)

#@login_required(login_url=login_required_ruta)
def jsonCumpAceites(request):
    jsonData = json_parser_aceites()
    return JsonResponse(jsonData, safe=False) 

#@login_required(login_url=login_required_ruta)
def jsonDistribuidoraAcar(request):
    jsonData = json_parser_distribuidora_acarigua()
    return JsonResponse(jsonData, safe=False)

#@login_required(login_url=login_required_ruta)
def jsonDistribuidoraBarc(request):
    jsonData = json_parser_distribuidora_barcelona()
    return JsonResponse(jsonData, safe=False) 

#@login_required(login_url=login_required_ruta)
def jsonDistribuidoraBarq(request):
    jsonData = json_parser_distribuidora_barquisimeto()
    return JsonResponse(jsonData, safe=False)

#@login_required(login_url=login_required_ruta)
def jsonDistribuidoraBoli(request):
    jsonData = json_parser_distribuidora_bolivar()
    return JsonResponse(jsonData, safe=False)

#@login_required(login_url=login_required_ruta)
def jsonDistribuidoraCara(request):
    jsonData = json_parser_distribuidora_caracas()
    return JsonResponse(jsonData, safe=False)

#@login_required(login_url=login_required_ruta)
def jsonDistribuidoraFijo(request):
    jsonData = json_parser_distribuidora_fijo()
    return JsonResponse(jsonData, safe=False) 

#@login_required(login_url=login_required_ruta)
def jsonDistribuidoraMara(request):
    jsonData = json_parser_distribuidora_mara()
    return JsonResponse(jsonData, safe=False)

#@login_required(login_url=login_required_ruta)
def jsonDistribuidoraMatu(request):
    jsonData = json_parser_distribuidora_matu()
    return JsonResponse(jsonData, safe=False) 

#@login_required(login_url=login_required_ruta)
def jsonDistribuidoraTachira(request):
    jsonData = json_parser_distribuidora_tach()
    return JsonResponse(jsonData, safe=False)     

#@login_required(login_url=login_required_ruta)
def jsonDistribuidoraVale(request):
    jsonData = json_parser_distribuidora_vale()
    return JsonResponse(jsonData, safe=False)

#@login_required(login_url=login_required_ruta)
def jsonDistribuidoraVigi(request):
    jsonData = json_parser_distribuidora_vigi()
    return JsonResponse(jsonData, safe=False)    

#@login_required(login_url=login_required_ruta)
def jsonDistribuidoraPlantas(request):
    jsonData = json_parser_distribuidora_plantas()
    return JsonResponse(jsonData, safe=False)

#@login_required(login_url=login_required_ruta)
def jsonDistribuidoraGranjas(request):
    jsonData = json_parser_distribuidora_granjas()
    return JsonResponse(jsonData, safe=False)

#@login_required(login_url=login_required_ruta)
def jsonDistribuidoraServifresco(request):
    jsonData = json_parser_distribuidora_servifresco()
    return JsonResponse(jsonData, safe=False)

#@login_required(login_url=login_required_ruta)
def jsonDistribuidoraCorporativo(request):
    jsonData = json_parser_distribuidora_corporativo()
    return JsonResponse(jsonData, safe=False)                                                                                                          
