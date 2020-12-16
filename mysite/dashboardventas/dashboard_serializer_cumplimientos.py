# coding=utf-8
import cx_Oracle
import json


oracle_con = cx_Oracle.connect("bi/bi@172.20.5.103/orclind")

#Volumen
def json_parser_cump():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data

#Entero
def json_parser_cump_entero():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and negocio = 'ENTERO'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data

#Entero
def json_parser_cump_despresado():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and negocio = 'DESPRESADO'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data 

#Filetes
def json_parser_cump_filetes():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and negocio = 'FILETES'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data

#Embutidos
def json_parser_cump_embutidos():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and negocio = 'EMBUTIDOS'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data

#Embutidos
def json_parser_cump_congelados():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and negocio = 'CONGELADOS'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data

#Huevos de consumo
def json_parser_cump_huevosconsumo():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and negocio = 'HUEVOS DE CONSUMO'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data


#Pollitos BB
def json_parser_cump_pollitos_bb():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and negocio = 'POLLITO BB - ENGORDE'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data


#Pollitos BB
def json_parser_pollonas_ponedora():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and negocio = 'POLLONA PONEDORA'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data


#Pollo Vivo
def json_parser_pollo_vivo():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and negocio = 'POLLO VIVO'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data

#Huevo fertil
def json_parser_huevo_fertil():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and negocio = 'HUEVO FERTIL'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data  

#Aba comercial
def json_parser_aba_comercial():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and negocio = 'ABA COMERCIAL'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data

#Mascotas
def json_parser_mascotas():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and negocio = 'MASCOTAS'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data   

#Lacteos
def json_parser_lacteos():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and negocio = 'LACTEOS'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data

#Lacteos
def json_parser_aceites():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and negocio = 'ACEITES'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data


#Distribuidora Acarigua
def json_parser_distribuidora_acarigua():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and distribuidora = 'Acar'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data

#Distribuidora Barcelona
def json_parser_distribuidora_barcelona():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and distribuidora = 'Barc'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data

#Distribuidora Barquisimeto
def json_parser_distribuidora_barquisimeto():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and distribuidora = 'Barq'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data

#Distribuidora Bolivar
def json_parser_distribuidora_bolivar():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and distribuidora = 'Boli'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data

#Distribuidora Caracas
def json_parser_distribuidora_caracas():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and distribuidora = 'Cara'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data

#Distribuidora Punto Fijo
def json_parser_distribuidora_fijo():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and distribuidora = 'Fijo'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data


#Distribuidora Maracaibo
def json_parser_distribuidora_mara():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and distribuidora = 'Mara'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data

#Distribuidora Maturin
def json_parser_distribuidora_matu():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and distribuidora = 'Matu'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data

#Distribuidora Tachira
def json_parser_distribuidora_tach():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and distribuidora = 'Tach'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data


#Distribuidora Valencia
def json_parser_distribuidora_vale():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and distribuidora = 'Vale'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data


#Distribuidora El Vigia
def json_parser_distribuidora_vigi():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and distribuidora = 'Vigi'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data

#Distribuidora Plantas
def json_parser_distribuidora_plantas():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and distribuidora = 'Plantas'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data

#Distribuidora Plantas
def json_parser_distribuidora_granjas():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and distribuidora = 'Granjas'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data

#Distribuidora Plantas
def json_parser_distribuidora_servifresco():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and distribuidora = 'Serv'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data

#Distribuidora Corporativo
def json_parser_distribuidora_corporativo():
  query = " select ceil((sum(volumen)/sum(volumenf))*100) cumpv, ceil((sum(monto)/sum(montof))*100) cumpp"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and distribuidora = 'Corp'"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"cumpv": row[0], "cumpp": row[1]})
  conn.close    
  return json_data                
