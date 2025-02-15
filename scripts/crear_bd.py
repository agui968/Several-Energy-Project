import psycopg2
from psycopg2 import sql
import pandas as pd
from sqlalchemy import create_engine
import io

ruta = "../data/processed/fixed_price.csv"
df = pd.read_csv(ruta)
#df.columns = df.columns.str.lower()


db_params = {
    'host': '34.78.249.103',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'cristian99'
}

conn = psycopg2.connect(**db_params)
cursor = conn.cursor()


table_name = 'fixed_price'

columns_and_types = [
    ('sistema', 'TEXT'),
    ('cia', 'TEXT'),
    ('producto', 'TEXT'),
    ('producto_cia', 'TEXT'),
    ('tarifa', 'TEXT'),
    ('fee', 'TEXT'),
    ('p1_p', 'DOUBLE PRECISION'),
    ('p2_p', 'DOUBLE PRECISION'),
    ('p3_p', 'DOUBLE PRECISION'),
    ('p4_p', 'DOUBLE PRECISION'),
    ('p5_p', 'DOUBLE PRECISION'),
    ('p6_p', 'DOUBLE PRECISION'),
    ('p1_e', 'DOUBLE PRECISION'),
    ('p2_e', 'DOUBLE PRECISION'),
    ('p3_e', 'DOUBLE PRECISION'),
    ('p4_e', 'TEXT'),
    ('p5_e', 'TEXT'),
    ('p6_e', 'TEXT')
]

csv_data = io.StringIO()
df.to_csv(csv_data, index=False, header=True, sep=',')

create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([f'{col} {data_type}' for col, data_type in columns_and_types])});"
cursor.execute(create_table_query)
conn.commit()

csv_data.seek(0)  
copy_query = f"COPY {table_name} FROM STDIN WITH CSV HEADER DELIMITER ',';"
cursor.copy_expert(sql=copy_query, file=csv_data)
conn.commit()

#---------------------------------------------------------------segundo csv---------------------------------------------------------------------

ruta = "./data/processed/indexed_price.csv"
df = pd.read_csv(ruta)

table_name = 'indexed_price'

columns_and_types = [
    ('SISTEMA', 'TEXT'),
    ('TARIFA', 'TEXT'),
    ('CIA', 'TEXT'),
    ('MES', 'TIMESTAMP'),
    ('FEE', 'TEXT'),
    ('P1', 'DOUBLE PRECISION'),
    ('P2', 'DOUBLE PRECISION'),
    ('P3', 'DOUBLE PRECISION'),
    ('P4', 'DOUBLE PRECISION'),
    ('P5', 'DOUBLE PRECISION'),
    ('P6', 'DOUBLE PRECISION')

]

csv_data = io.StringIO()
df.to_csv(csv_data, index=False, header=True, sep=',')

create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([f'{col} {data_type}' for col, data_type in columns_and_types])});"
cursor.execute(create_table_query)
conn.commit()

csv_data.seek(0)  
copy_query = f"COPY {table_name} FROM STDIN WITH CSV HEADER DELIMITER ',';"
cursor.copy_expert(sql=copy_query, file=csv_data)
conn.commit()


#------------------------------------------------------Tercer CSV------------------------------------------------------------------


ruta = "./data/processed/indexed_price_power.csv"
df = pd.read_csv(ruta)

table_name = 'indexed_price_power'

columns_and_types = [
    ('SISTEMA', 'TEXT'),
    ('CIA', 'TEXT'),
    ('PRODUCTO', 'TEXT'),
    ('PRODUCTO_CIA', 'TEXT'),
    ('TARIFA', 'TEXT'),
    ('P1', 'DOUBLE PRECISION'),
    ('P2', 'DOUBLE PRECISION'),
    ('P3', 'DOUBLE PRECISION'),
    ('P4', 'DOUBLE PRECISION'),
    ('P5', 'DOUBLE PRECISION'),
    ('P6', 'DOUBLE PRECISION')
]

csv_data = io.StringIO()
df.to_csv(csv_data, index=False, header=True, sep=',')

create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([f'{col} {data_type}' for col, data_type in columns_and_types])});"
cursor.execute(create_table_query)
conn.commit()

csv_data.seek(0)  
copy_query = f"COPY {table_name} FROM STDIN WITH CSV HEADER DELIMITER ',';"
cursor.copy_expert(sql=copy_query, file=csv_data)
conn.commit()

#CERRAMOS CONEXION

cursor.close()
conn.close()