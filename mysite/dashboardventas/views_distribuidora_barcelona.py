from django.shortcuts import render
from django.http import JsonResponse
from .db_serializer_distribuidora_barcelona import *
# Create your views here.

###################################################################################
###############################INDEX###############################################
###################################################################################

#@login_required(login_url=login_required_ruta)
def index(request):
    return render(request, "dashboardventas/dbarcelona.html")  

####################################################################################
###############################DISTRIBUIDORAS#######################################
####################################################################################       

#@login_required(login_url=login_required_ruta)
def jsonVtasVolumend(request):
    jsonData = json_parser_volumend()
    return JsonResponse(jsonData, safe=False)

#@login_required(login_url=login_required_ruta)
def jsonVtasPreciod(request):
    jsonData = json_parser_montod()
    return JsonResponse(jsonData, safe=False) 

#@login_required(login_url=login_required_ruta)
def jsonVtasTotald(request):
    jsonData = json_parser_totald()
    return JsonResponse(jsonData, safe=False)


####################################################################################
###############################FORECAST#############################################
####################################################################################
#@login_required(login_url=login_required_ruta)
def jsonVtasVolumenf(request):
    jsonData = json_parser_volumenf()
    return JsonResponse(jsonData, safe=False)

#@login_required(login_url=login_required_ruta)
def jsonVtasMontof(request):
    jsonData = json_parser_montof()
    return JsonResponse(jsonData, safe=False) 

#@login_required(login_url=login_required_ruta)
def jsonAnocon(request):
    jsonData = json_parser_semcon()
    return JsonResponse(jsonData, safe=False)  

