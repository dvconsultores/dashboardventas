# coding=utf-8
import cx_Oracle
import json


oracle_con = cx_Oracle.connect("bi/bi@172.20.5.103/orclind")

#Volumen
def json_parser_volumend():
  query = " select INITCAP(negocio)"
  query += " , volumen"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and distribuidora = 'Fijo'"
  query += " and volumenf > 0"
  query += " order by 1"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")  
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"distribuidora": row[0], "volumen": row[1]})
  conn.close    
  return json_data

#Monto
def json_parser_montod():
  query = " select INITCAP(negocio)"
  query += " , monto"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and distribuidora = 'Fijo'"
  query += " and volumenf > 0"
  query += " order by 1"
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"distribuidora": row[0], "monto": row[1]})
  conn.close    
  return json_data

#PrecioPromedio
def json_parser_totald():
  query = "select  to_char(sum(volumen),'999G999G999D99', 'NLS_NUMERIC_CHARACTERS='',.''') totalvd, to_char(sum(monto),'999G999G999D99', 'NLS_NUMERIC_CHARACTERS='',.''') totalmd"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and distribuidora = 'Fijo'"
  query += " and volumenf > 0"
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"totalvd": row[0], "totalmd": row[1]})
  conn.close    
  return json_data 

#Semana contable
def json_parser_semcon():
  query = "select SPLITCAD(FUN_CALENDARIO(sysdate),1,'|'), SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " from dual"
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"anocon": row[0], "semcon": row[1]})
  conn.close    
  return json_data   

##########################################################################################################  
####################################################Forecast##############################################
##########################################################################################################
#Volumen
def json_parser_volumenf():
  query = " select INITCAP(negocio)"
  query += " , volumenf"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and distribuidora = 'Fijo'"
  query += " and volumenf > 0"
  query += " order by 1"
  print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"distribuidora": row[0], "volumen": row[1]})
  conn.close    
  return json_data

#Volumen
def json_parser_montof():
  query = " select INITCAP(negocio)"
  query += " , montof"
  query += " from dashboard_ventas"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and distribuidora = 'Fijo'"
  query += " and volumenf > 0"
  query += " order by 1"
  #print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"distribuidora": row[0], "monto": row[1]})
  conn.close    
  return json_data  