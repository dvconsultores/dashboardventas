#from django.contrib import admin
from django.urls import path, re_path
#from django.conf.urls import url, include
#from django.contrib.auth import views as auth_views

from . import views, views_entero, views_despresado, views_filetes, views_embutidos, views_congelados, views_huevos, views_pollosbb
from . import views_pollovivo, views_aba, views_mascotas, views_lacteos, views_aceite, views_pollona, views_huevof
from . import views_distribuidora_acarigua, views_distribuidora_barcelona, views_distribuidora_barquisimeto
from . import views_distribuidora_bolivar, views_distribuidora_caracas, views_distribuidora_fijo, views_distribuidora_maracaibo
from . import views_distribuidora_maturin, views_distribuidora_tachira, views_distribuidora_valencia, views_distribuidora_vigia

app_name = 'dashboardventas'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    #
    path('entero/', views_entero.index, name='entero'),
    path('', views_entero.index, name='entero'),
    #
    path('despresado/', views_despresado.index, name='despresado'),
    path('', views_despresado.index, name='despresado'),
    #
    path('filetes/', views_filetes.index, name='filetes'),
    path('', views_filetes.index, name='filetes'),
    #
    path('embutidos/', views_embutidos.index, name='embutidos'),
    path('', views_embutidos.index, name='embutidos'),
    #
    path('congelados/', views_congelados.index, name='congelados'),
    path('', views_congelados.index, name='congelados'),
    #
    path('huevos/', views_huevos.index, name='huevos'),
    path('', views_huevos.index, name='huevos'),
    #
    path('pollosbb/', views_pollosbb.index, name='pollosbb'),
    path('', views_pollosbb.index, name='pollosbb'),
    #
    path('pollovivo/', views_pollovivo.index, name='pollovivo'),
    path('', views_pollovivo.index, name='pollovivo'),
    #
    path('aba/', views_aba.index, name='aba'),
    path('', views_aba.index, name='aba'),
    #
    path('mascotas/', views_mascotas.index, name='mascotas'),
    path('', views_mascotas.index, name='mascotas'),
    #
    path('lacteos/', views_lacteos.index, name='lacteos'),
    path('', views_lacteos.index, name='lacteos'),
    #
    path('aceite/', views_aceite.index, name='aceite'),
    path('', views_aceite.index, name='aceite'),
    #
    path('pollona/', views_pollona.index, name='pollona'),
    path('', views_pollona.index, name='pollona'),
    #
    path('huevofertil/', views_huevof.index, name='huevofertil'),
    path('', views_huevof.index, name='huevofertil'),
    #
    path('dacarigua/', views_distribuidora_acarigua.index, name='dacarigua'),
    path('', views_distribuidora_acarigua.index, name='dacarigua'),
    #
    path('dbarcelona/', views_distribuidora_barcelona.index, name='dbarcelona'),
    path('', views_distribuidora_barcelona.index, name='dbarcelona'),
    #
    path('dbarquisimeto/', views_distribuidora_barquisimeto.index, name='dbarquisimeto'),
    path('', views_distribuidora_barquisimeto.index, name='dbarquisimeto'),
    #
    path('dbolivar/', views_distribuidora_bolivar.index, name='dbolivar'),
    path('', views_distribuidora_bolivar.index, name='dbolivar'),
    #
    path('dcaracas/', views_distribuidora_caracas.index, name='dcaracas'),
    path('', views_distribuidora_caracas.index, name='dcaracas'),
    #
    path('dfijo/', views_distribuidora_fijo.index, name='dfijo'),
    path('', views_distribuidora_fijo.index, name='dfijo'),
    #
    path('dmaracaibo/', views_distribuidora_maracaibo.index, name='dmara'),
    path('', views_distribuidora_maracaibo.index, name='dmara'),
    #
    path('dmaturin/', views_distribuidora_maturin.index, name='dmaturin'),
    path('', views_distribuidora_maturin.index, name='dmaturin'),
    #
    path('dtachira/', views_distribuidora_tachira.index, name='dtachira'),
    path('', views_distribuidora_tachira.index, name='dtachira'),
    #
    path('dvalencia/', views_distribuidora_valencia.index, name='dvalencia'),
    path('', views_distribuidora_valencia.index, name='dvalencia'),
    #
    path('dvigia/', views_distribuidora_vigia.index, name='dvigia'),
    path('', views_distribuidora_vigia.index, name='dvigia'),
    ###################Distribuidoras############################################
    path('volumend', views.jsonVtasVolumend, name='volumend'),
    path('montod', views.jsonVtasPreciod, name='montod'),
    path('totald', views.jsonVtasTotald, name='totald'),
    ###################Forecast##################################################
    path('volumenf', views.jsonVtasVolumenf, name='volumenf'),
    path('montof', views.jsonVtasMontof, name='montof'),
    ###################Anocon####################################################
    path('anocon', views.jsonAnocon, name='anocon'),

    #############################################################################
    ##########################ENTERO#############################################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_entero', views_entero.jsonVtasVolumend, name='volumend_entero'),
    path('montod_entero', views_entero.jsonVtasPreciod, name='montod_entero'),
    path('totald_entero', views_entero.jsonVtasTotald, name='totald_entero'),
    ###################Forecast##################################################
    path('volumenf_entero', views_entero.jsonVtasVolumenf, name='volumenf_entero'),
    path('montof_entero', views_entero.jsonVtasMontof, name='montof_entero'),

    #############################################################################
    ##########################DESPRESADO#########################################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_despresado', views_despresado.jsonVtasVolumend, name='volumend_despresado'),
    path('montod_despresado', views_despresado.jsonVtasPreciod, name='montod_despresado'),
    path('totald_despresado', views_despresado.jsonVtasTotald, name='totald_despresado'),
    ###################Forecast##################################################
    path('volumenf_despresado', views_despresado.jsonVtasVolumenf, name='volumenf_despresado'),
    path('montof_despresado', views_despresado.jsonVtasMontof, name='montof_despresado'),

    #############################################################################
    ##########################FILETES#########################################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_filetes', views_filetes.jsonVtasVolumend, name='volumend_filetes'),
    path('montod_filetes', views_filetes.jsonVtasPreciod, name='montod_filetes'),
    path('totald_filetes', views_filetes.jsonVtasTotald, name='totald_filetes'),
    ###################Forecast##################################################
    path('volumenf_filetes', views_filetes.jsonVtasVolumenf, name='volumenf_filetes'),
    path('montof_filetes', views_filetes.jsonVtasMontof, name='montof_filetes'),

    #############################################################################
    ##########################EMBUTIDOS#########################################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_embutidos', views_embutidos.jsonVtasVolumend, name='volumend_embutidos'),
    path('montod_embutidos', views_embutidos.jsonVtasPreciod, name='montod_embutidos'),
    path('totald_embutidos', views_embutidos.jsonVtasTotald, name='totald_embutidos'),
    ###################Forecast##################################################
    path('volumenf_embutidos', views_embutidos.jsonVtasVolumenf, name='volumenf_embutidos'),
    path('montof_embutidos', views_embutidos.jsonVtasMontof, name='montof_embutidos'),

    #############################################################################
    ##########################CONGELADOS#########################################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_congelados', views_congelados.jsonVtasVolumend, name='volumend_congelados'),
    path('montod_congelados', views_congelados.jsonVtasPreciod, name='montod_congelados'),
    path('totald_congelados', views_congelados.jsonVtasTotald, name='totald_congelados'),
    ###################Forecast##################################################
    path('volumenf_congelados', views_congelados.jsonVtasVolumenf, name='volumenf_congelados'),
    path('montof_congelados', views_congelados.jsonVtasMontof, name='montof_congelados'),

    #############################################################################
    ##########################HUEVOS#############################################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_huevos', views_huevos.jsonVtasVolumend, name='volumend_huevos'),
    path('montod_huevos', views_huevos.jsonVtasPreciod, name='montod_huevos'),
    path('totald_huevos', views_huevos.jsonVtasTotald, name='totald_huevos'),
    ###################Forecast##################################################
    path('volumenf_huevos', views_huevos.jsonVtasVolumenf, name='volumenf_huevos'),
    path('montof_huevos', views_huevos.jsonVtasMontof, name='montof_huevos'),

    #############################################################################
    ##########################POLLOS BB##########################################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_pollosbb', views_pollosbb.jsonVtasVolumend, name='volumend_pollosbb'),
    path('montod_pollosbb', views_pollosbb.jsonVtasPreciod, name='montod_pollosbb'),
    path('totald_pollosbb', views_pollosbb.jsonVtasTotald, name='totald_pollosbb'),
    ###################Forecast##################################################
    path('volumenf_pollosbb', views_pollosbb.jsonVtasVolumenf, name='volumenf_pollosbb'),
    path('montof_pollosbb', views_pollosbb.jsonVtasMontof, name='montof_pollosbb'),

    #############################################################################
    ##########################POLLO VIVO##########################################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_pollovivo', views_pollovivo.jsonVtasVolumend, name='volumend_pollovivo'),
    path('montod_pollovivo', views_pollovivo.jsonVtasPreciod, name='montod_pollovivo'),
    path('totald_pollovivo', views_pollovivo.jsonVtasTotald, name='totald_pollovivo'),
    ###################Forecast##################################################
    path('volumenf_pollovivo', views_pollovivo.jsonVtasVolumenf, name='volumenf_pollovivo'),
    path('montof_pollovivo', views_pollovivo.jsonVtasMontof, name='montof_pollovivo'),

    #############################################################################
    ##########################ABA################################################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_aba', views_aba.jsonVtasVolumend, name='volumend_aba'),
    path('montod_aba', views_aba.jsonVtasPreciod, name='montod_aba'),
    path('totald_aba', views_aba.jsonVtasTotald, name='totald_aba'),
    ###################Forecast##################################################
    path('volumenf_aba', views_aba.jsonVtasVolumenf, name='volumenf_aba'),
    path('montof_aba', views_aba.jsonVtasMontof, name='montof_aba'),

    #############################################################################
    ##########################MASCOTAS############################################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_mascotas', views_mascotas.jsonVtasVolumend, name='volumend_mascotas'),
    path('montod_mascotas', views_mascotas.jsonVtasPreciod, name='montod_mascotas'),
    path('totald_mascotas', views_mascotas.jsonVtasTotald, name='totald_mascotas'),
    ###################Forecast##################################################
    path('volumenf_mascotas', views_mascotas.jsonVtasVolumenf, name='volumenf_mascotas'),
    path('montof_mascotas', views_mascotas.jsonVtasMontof, name='montof_mascotas'),

    #############################################################################
    ##########################LACTEOS############################################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_lacteos', views_lacteos.jsonVtasVolumend, name='volumend_lacteos'),
    path('montod_lacteos', views_lacteos.jsonVtasPreciod, name='montod_lacteos'),
    path('totald_lacteos', views_lacteos.jsonVtasTotald, name='totald_lacteos'),
    ###################Forecast##################################################
    path('volumenf_lacteos', views_lacteos.jsonVtasVolumenf, name='volumenf_lacteos'),
    path('montof_lacteos', views_lacteos.jsonVtasMontof, name='montof_lacteos'),

    #############################################################################
    ##########################ACEITES############################################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_aceite', views_aceite.jsonVtasVolumend, name='volumend_aceite'),
    path('montod_aceite', views_aceite.jsonVtasPreciod, name='montod_aceite'),
    path('totald_aceite', views_aceite.jsonVtasTotald, name='totald_aceite'),
    ###################Forecast##################################################
    path('volumenf_aceite', views_aceite.jsonVtasVolumenf, name='volumenf_aceite'),
    path('montof_aceite', views_aceite.jsonVtasMontof, name='montof_aceite'),

    #############################################################################
    ##########################POLLONA############################################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_pollona', views_pollona.jsonVtasVolumend, name='volumend_pollona'),
    path('montod_pollona', views_pollona.jsonVtasPreciod, name='montod_pollona'),
    path('totald_pollona', views_pollona.jsonVtasTotald, name='totald_pollona'),
    ###################Forecast##################################################
    path('volumenf_pollona', views_pollona.jsonVtasVolumenf, name='volumenf_pollona'),
    path('montof_pollona', views_pollona.jsonVtasMontof, name='montof_pollona'),

    #############################################################################
    ##########################HUEVO FERTIL########################################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_huevof', views_huevof.jsonVtasVolumend, name='volumend_huevof'),
    path('montod_huevof', views_huevof.jsonVtasPreciod, name='montod_huevof'),
    path('totald_huevof', views_huevof.jsonVtasTotald, name='totald_huevof'),
    ###################Forecast##################################################
    path('volumenf_huevof', views_huevof.jsonVtasVolumenf, name='volumenf_huevof'),
    path('montof_huevof', views_huevof.jsonVtasMontof, name='montof_huevof'),

    #############################################################################
    ##########################DISTRIBUIDORA ACARIGUA#############################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_dacarigua', views_distribuidora_acarigua.jsonVtasVolumend, name='volumend_dacarigua'),
    path('montod_dacarigua', views_distribuidora_acarigua.jsonVtasPreciod, name='montod_dacarigua'),
    path('totald_dacarigua', views_distribuidora_acarigua.jsonVtasTotald, name='totald_dacarigua'),
    ###################Forecast##################################################
    path('volumenf_dacarigua', views_distribuidora_acarigua.jsonVtasVolumenf, name='volumenf_dacarigua'),
    path('montof_dacarigua', views_distribuidora_acarigua.jsonVtasMontof, name='montof_dacarigua'),

    #############################################################################
    ##########################DISTRIBUIDORA BARCELONA#############################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_dbarcelona', views_distribuidora_barcelona.jsonVtasVolumend, name='volumend_dbarcelona'),
    path('montod_dbarcelona', views_distribuidora_barcelona.jsonVtasPreciod, name='montod_dbarcelona'),
    path('totald_dbarcelona', views_distribuidora_barcelona.jsonVtasTotald, name='totald_dbarcelona'),
    ###################Forecast##################################################
    path('volumenf_dbarcelona', views_distribuidora_barcelona.jsonVtasVolumenf, name='volumenf_dbarcelona'),
    path('montof_dbarcelona', views_distribuidora_barcelona.jsonVtasMontof, name='montof_dbarcelona'),

    #############################################################################
    ##########################DISTRIBUIDORA BARQUISIMETO#############################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_dbarquisimeto', views_distribuidora_barquisimeto.jsonVtasVolumend, name='volumend_dbarquisimeto'),
    path('montod_dbarquisimeto', views_distribuidora_barquisimeto.jsonVtasPreciod, name='montod_dbarquisimeto'),
    path('totald_dbarquisimeto', views_distribuidora_barquisimeto.jsonVtasTotald, name='totald_dbarquisimeto'),
    ###################Forecast##################################################
    path('volumenf_dbarquisimeto', views_distribuidora_barquisimeto.jsonVtasVolumenf, name='volumenf_dbarquisimeto'),
    path('montof_dbarquisimeto', views_distribuidora_barquisimeto.jsonVtasMontof, name='montof_dbarquisimeto'),

    #############################################################################
    ##########################DISTRIBUIDORA BOLIVAR#############################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_dbolivar', views_distribuidora_bolivar.jsonVtasVolumend, name='volumend_dbolivar'),
    path('montod_dbolivar', views_distribuidora_bolivar.jsonVtasPreciod, name='montod_dbolivar'),
    path('totald_dbolivar', views_distribuidora_bolivar.jsonVtasTotald, name='totald_dbolivar'),
    ###################Forecast##################################################
    path('volumenf_dbolivar', views_distribuidora_bolivar.jsonVtasVolumenf, name='volumenf_dbolivar'),
    path('montof_dbolivar', views_distribuidora_bolivar.jsonVtasMontof, name='montof_dbolivar'),

    #############################################################################
    ##########################DISTRIBUIDORA CARACAS#############################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_dcaracas', views_distribuidora_caracas.jsonVtasVolumend, name='volumend_dcaracas'),
    path('montod_dcaracas', views_distribuidora_caracas.jsonVtasPreciod, name='montod_dcaracas'),
    path('totald_dcaracas', views_distribuidora_caracas.jsonVtasTotald, name='totald_dcaracas'),
    ###################Forecast##################################################
    path('volumenf_dcaracas', views_distribuidora_caracas.jsonVtasVolumenf, name='volumenf_dcaracas'),
    path('montof_dcaracas', views_distribuidora_caracas.jsonVtasMontof, name='montof_dcaracas'),

    #############################################################################
    ##########################DISTRIBUIDORA PTO FIJO#############################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_dfijo', views_distribuidora_fijo.jsonVtasVolumend, name='volumend_dfijo'),
    path('montod_dfijo', views_distribuidora_fijo.jsonVtasPreciod, name='montod_dfijo'),
    path('totald_dfijo', views_distribuidora_fijo.jsonVtasTotald, name='totald_dfijo'),
    ###################Forecast##################################################
    path('volumenf_dfijo', views_distribuidora_fijo.jsonVtasVolumenf, name='volumenf_dfijo'),
    path('montof_dfijo', views_distribuidora_fijo.jsonVtasMontof, name='montof_dfijo'),

    #############################################################################
    ##########################DISTRIBUIDORA MARACAY#############################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_dmara', views_distribuidora_maracaibo.jsonVtasVolumend, name='volumend_dmara'),
    path('montod_dmara', views_distribuidora_maracaibo.jsonVtasPreciod, name='montod_dmara'),
    path('totald_dmara', views_distribuidora_maracaibo.jsonVtasTotald, name='totald_dmara'),
    ###################Forecast##################################################
    path('volumenf_dmara', views_distribuidora_maracaibo.jsonVtasVolumenf, name='volumenf_dmara'),
    path('montof_dmara', views_distribuidora_maracaibo.jsonVtasMontof, name='montof_dmara'),

    #############################################################################
    ##########################DISTRIBUIDORA MATURIN#############################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_dmaturin', views_distribuidora_maturin.jsonVtasVolumend, name='volumend_dmaturin'),
    path('montod_dmaturin', views_distribuidora_maturin.jsonVtasPreciod, name='montod_dmaturin'),
    path('totald_dmaturin', views_distribuidora_maturin.jsonVtasTotald, name='totald_dmaturin'),
    ###################Forecast##################################################
    path('volumenf_dmaturin', views_distribuidora_maturin.jsonVtasVolumenf, name='volumenf_dmaturin'),
    path('montof_dmaturin', views_distribuidora_maturin.jsonVtasMontof, name='montof_dmaturin'),

    #############################################################################
    ##########################DISTRIBUIDORA TACHIRA#############################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_dtachira', views_distribuidora_tachira.jsonVtasVolumend, name='volumend_dtachira'),
    path('montod_dtachira', views_distribuidora_tachira.jsonVtasPreciod, name='montod_dtachira'),
    path('totald_dtachira', views_distribuidora_tachira.jsonVtasTotald, name='totald_dtachira'),
    ###################Forecast##################################################
    path('volumenf_dtachira', views_distribuidora_tachira.jsonVtasVolumenf, name='volumenf_dtachira'),
    path('montof_dtachira', views_distribuidora_tachira.jsonVtasMontof, name='montof_dtachira'),

    #############################################################################
    ##########################DISTRIBUIDORA VALENCIA#############################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_dvalencia', views_distribuidora_valencia.jsonVtasVolumend, name='volumend_dvalencia'),
    path('montod_dvalencia', views_distribuidora_valencia.jsonVtasPreciod, name='montod_dvalencia'),
    path('totald_dvalencia', views_distribuidora_valencia.jsonVtasTotald, name='totald_dvalencia'),
    ###################Forecast##################################################
    path('volumenf_dvalencia', views_distribuidora_valencia.jsonVtasVolumenf, name='volumenf_dvalencia'),
    path('montof_dvalencia', views_distribuidora_valencia.jsonVtasMontof, name='montof_dvalencia'),

    #############################################################################
    ##########################DISTRIBUIDORA VIGIA#############################
    #############################################################################
    ###################Distribuidoras############################################
    path('volumend_dvigia', views_distribuidora_valencia.jsonVtasVolumend, name='volumend_dvigia'),
    path('montod_dvigia', views_distribuidora_valencia.jsonVtasPreciod, name='montod_dvigia'),
    path('totald_dvigia', views_distribuidora_valencia.jsonVtasTotald, name='totald_dvigia'),
    ###################Forecast##################################################
    path('volumenf_dvigia', views_distribuidora_valencia.jsonVtasVolumenf, name='volumenf_dvigia'),
    path('montof_dvigia', views_distribuidora_valencia.jsonVtasMontof, name='montof_dvigia'),
]

