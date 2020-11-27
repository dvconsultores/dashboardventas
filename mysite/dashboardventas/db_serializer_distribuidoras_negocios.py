# coding=utf-8
import cx_Oracle
import json


oracle_con = cx_Oracle.connect("bi/bi@172.20.5.103/orclind")

#Volumen
def json_parser_volumend():
  query = "select case when SPLITCAD(desc_dim1,2,' ') = 'MARACAIBO'  then 'Mara'"
  query += " when SPLITCAD(desc_dim1,2,' ') = 'EL' then 'Vigi'"
  query += " when SPLITCAD(desc_dim1,2,' ') = 'TACHIRA' then 'Tach'"
  query += " when SPLITCAD(desc_dim1,2,' ') = 'BARCELONA' then 'Barc'"
  query += " when SPLITCAD(desc_dim1,2,' ') = 'BARQUISIMETO' then 'Barq'"
  query += " when SPLITCAD(desc_dim1,2,' ') = 'BOLIVAR' then 'Boli'"
  query += " when SPLITCAD(desc_dim1,2,' ') = 'VALENCIA' then 'Vale'"
  query += " when SPLITCAD(desc_dim1,2,' ') = 'CARACAS' then 'Cara'"
  query += " when SPLITCAD(desc_dim1,2,' ') = 'MATURIN' then 'Matu'"
  query += " when SPLITCAD(desc_dim1,2,' ') = 'PUNTO' then 'Fijo'"
  query += " when SPLITCAD(desc_dim1,2,' ') = 'ACARIGUA' then 'Acar'"
  query += " else 'Corp' end distribuidora"
  query += " , sum(round(volumen,2)) volumen"
  query += " from ventas_prv0057"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and dim1 in (SELECT cod FROM DISTRIBUIDORAS)"
  query += " and negociokpi = 'AVES BENEFICIADAS ENTERO'"
  query += " and nombre_vendendor not in ('MARIA LUISA PAEZ', 'MARIA DE CEDEÑO','MARIA ANGELICA MACHADO','ANTHONY OROZCO')"
  query += " group by desc_dim1 order by 1"
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
  query = "select case when SPLITCAD(desc_dim1,2,' ') = 'MARACAIBO'  then 'Mara'"
  query += " when SPLITCAD(desc_dim1,2,' ') = 'EL' then 'Vigi'"
  query += " when SPLITCAD(desc_dim1,2,' ') = 'TACHIRA' then 'Tach'"
  query += " when SPLITCAD(desc_dim1,2,' ') = 'BARCELONA' then 'Barc'"
  query += " when SPLITCAD(desc_dim1,2,' ') = 'BARQUISIMETO' then 'Barq'"
  query += " when SPLITCAD(desc_dim1,2,' ') = 'BOLIVAR' then 'Boli'"
  query += " when SPLITCAD(desc_dim1,2,' ') = 'VALENCIA' then 'Vale'"
  query += " when SPLITCAD(desc_dim1,2,' ') = 'CARACAS' then 'Cara'"
  query += " when SPLITCAD(desc_dim1,2,' ') = 'MATURIN' then 'Matu'"
  query += " when SPLITCAD(desc_dim1,2,' ') = 'PUNTO' then 'Fijo'"
  query += " when SPLITCAD(desc_dim1,2,' ') = 'ACARIGUA' then 'Acar'"
  query += " else 'Corp' end distribuidora"
  query += " , sum(round(monto_div,2)) volumen"
  query += " from ventas_prv0057"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and dim1 in (SELECT cod FROM DISTRIBUIDORAS)"
  query += " and negociokpi = 'AVES BENEFICIADAS ENTERO'"
  query += " and nombre_vendendor not in ('MARIA LUISA PAEZ', 'MARIA DE CEDEÑO','MARIA ANGELICA MACHADO','ANTHONY OROZCO')"
  query += " group by desc_dim1 order by 1"
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
  query = "select  to_char(sum(volumen),'999G999G999D99', 'NLS_NUMERIC_CHARACTERS='',.''') totalvd, to_char(sum(monto_div),'999G999G999D99', 'NLS_NUMERIC_CHARACTERS='',.''') totalmd"
  query += " from ventas_prv0057"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and dim1 in (SELECT cod FROM DISTRIBUIDORAS)"
  query += " and negociokpi = 'AVES BENEFICIADAS ENTERO'"
  query += " and nombre_vendendor not in ('MARIA LUISA PAEZ', 'MARIA DE CEDEÑO','MARIA ANGELICA MACHADO','ANTHONY OROZCO')"
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
  query = "select case when SPLITCAD(DISTRIBUIDORA,1,' ') = 'MARACAIBO'  then 'Mara'"
  query += " when SPLITCAD(DISTRIBUIDORA,1,' ') = 'EL' then 'Vigi'"
  query += " when SPLITCAD(DISTRIBUIDORA,1,' ') = 'TACHIRA' then 'Tach'"
  query += " when SPLITCAD(DISTRIBUIDORA,1,' ') = 'BARCELONA' then 'Barc'"
  query += " when SPLITCAD(DISTRIBUIDORA,1,' ') = 'BARQUISIMETO' then 'Barq'"
  query += " when SPLITCAD(DISTRIBUIDORA,1,' ') = 'BOLIVAR' then 'Boli'"
  query += " when SPLITCAD(DISTRIBUIDORA,1,' ') = 'VALENCIA' then 'Vale'"
  query += " when SPLITCAD(DISTRIBUIDORA,1,' ') = 'CARACAS' then 'Cara'"
  query += " when SPLITCAD(DISTRIBUIDORA,1,' ') = 'MATURIN' then 'Matu'"
  query += " when SPLITCAD(DISTRIBUIDORA,1,' ') = 'PUNTO' then 'Fijo'"
  query += " when SPLITCAD(DISTRIBUIDORA,1,' ') = 'ACARIGUA' then 'Acar'"
  query += " else 'Corp' end distribuidora"
  query += " , sum(round(volumen,2)) volumen"
  query += " from presupuesto_ventas_dist"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and distribuidora not in ('CORPORATIVO')"
  query += " and UPPER(AGRUPACION) = 'ENTERO'"
  query += " group by DISTRIBUIDORA order by 1"
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

#Volumen
def json_parser_montof():
  query = "select case when SPLITCAD(DISTRIBUIDORA,1,' ') = 'MARACAIBO'  then 'Mara'"
  query += " when SPLITCAD(DISTRIBUIDORA,1,' ') = 'EL' then 'Vigi'"
  query += " when SPLITCAD(DISTRIBUIDORA,1,' ') = 'TACHIRA' then 'Tach'"
  query += " when SPLITCAD(DISTRIBUIDORA,1,' ') = 'BARCELONA' then 'Barc'"
  query += " when SPLITCAD(DISTRIBUIDORA,1,' ') = 'BARQUISIMETO' then 'Barq'"
  query += " when SPLITCAD(DISTRIBUIDORA,1,' ') = 'BOLIVAR' then 'Boli'"
  query += " when SPLITCAD(DISTRIBUIDORA,1,' ') = 'VALENCIA' then 'Vale'"
  query += " when SPLITCAD(DISTRIBUIDORA,1,' ') = 'CARACAS' then 'Cara'"
  query += " when SPLITCAD(DISTRIBUIDORA,1,' ') = 'MATURIN' then 'Matu'"
  query += " when SPLITCAD(DISTRIBUIDORA,1,' ') = 'PUNTO' then 'Fijo'"
  query += " when SPLITCAD(DISTRIBUIDORA,1,' ') = 'ACARIGUA' then 'Acar'"
  query += " else 'Corp' end distribuidora"
  query += " , sum(round(monto,2)) monto"
  query += " from presupuesto_ventas_dist_pu"
  query += " where anocon = SPLITCAD(FUN_CALENDARIO(sysdate),1,'|')"
  query += " and semcon = SPLITCAD(FUN_CALENDARIO(sysdate),3,'|')"
  query += " and distribuidora not in ('CORPORATIVO')"
  query += " and UPPER(AGRUPACION) = 'ENTERO'"
  query += " group by DISTRIBUIDORA order by 1"
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