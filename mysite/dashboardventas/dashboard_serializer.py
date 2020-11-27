# coding=utf-8
import cx_Oracle
import json


oracle_con = cx_Oracle.connect("bi/bi@172.20.5.103/orclind")

#Volumen
def json_parser_volumen():
  query = "select negocio, sum(volumen) volumen from ventas_prv0057 where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|') and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|') group by negocio"
  # print(query)
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"negocio": row[0], "volumen": row[1]})
  conn.close    
  return json_data

#Precio
def json_parser_precio():
  query = "select negocio, sum(monto_div) monto from ventas_prv0057 where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|') and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|') group by negocio"
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"negocio": row[0], "precio": row[1]})
  conn.close    
  return json_data

#PrecioPromedio
def json_parser_precio_promedio():
  query = "select negocio,  sum(volumen)/sum(monto_div) promedio"
  query += " FROM ventas_prv0057"
  query += " WHERE ANOCON  = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " AND semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " AND TIPO_NEGOCIO = 'V0A'"
  query += " group by negocio"
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"negocio": row[0], "promedio": row[1]})
  conn.close    
  return json_data 


#PrecioPromedio
def json_parser_cumplimiento_volumen():
  query = "SELECT negocio, volumen"
  query += " FROM PRESUPUESTO_VENTAS"
  query += " WHERE ANOCON  = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " AND semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " AND volumen > 0"
  conn = oracle_con
  c = conn.cursor()
  c.execute(
     "ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY'")
  c.execute(query)
  json_data = list([])
  for row in c:
      json_data.append({"negocio": row[0], "cumplimiento": row[1]})
  conn.close    
  return json_data       
