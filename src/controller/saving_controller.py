import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import psycopg2
from config.secret_config import PGHOST, PGDATABASE, PGUSER, PGPASSWORD

from src.model.app import Saving

def connect_db():
    conn = psycopg2.connect(host=PGHOST, database=PGDATABASE, user=PGUSER, password=PGPASSWORD, sslmode='require')
    return conn

def create_savings_table():
    conn = connect_db()
    cursor = conn.cursor()
    try:
        with open ('sql/create_saving_table.sql', 'r') as query:
            query = query.read()
            
        cursor.execute(query)
            
        conn.commit()
        print("Tabla ahorros creada correctamente.")

    except Exception as e:
        print(f"Error creando la tabla: {e}")
    finally:
        cursor.close()
        conn.close()

def insert_saving(saving: Saving):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        with open ('sql/insert_saving.sql', 'r') as query:
            query = query.read()
            
        cursor.execute(query, saving.do_tuple())
            
        conn.commit()
        print("Ahorro insertado correctamente.")
    except Exception as e:
        print(f"Error insertando el ahorro: {e}")
    finally:
        cursor.close()
        conn.close()

def delete_saving(id_saving: int):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        with open ('sql/delete_saving.sql', 'r') as query:
            query = query.read()
            
        cursor.execute(query, (id_saving,))
            
        conn.commit()
        print("Ahorro eliminado correctamente.")
    except Exception as e:
        print(f"Error eliminando el ahorro: {e}")
    finally:
        cursor.close()
        conn.close()

def update_saving(id_saving: int, saving: Saving):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        with open ('sql/update_saving.sql', 'r') as query:
            query = query.read()
            
        new_saving = saving.do_tuple()
        cursor.execute(query, (*new_saving, id_saving))
            
        conn.commit()
        print("Ahorro actualizado correctamente.")
    except Exception as e:
        print(f"Error actualizando los ahorros: {e}")
    finally:
        cursor.close()
        conn.close()

def select_savings(id_saving: int):
    conn = connect_db()
    cursor = conn.cursor()
    result = []
    try:
        with open ('sql/select_saving.sql', 'r') as query:
            query = query.read()
        cursor.execute(query, (id_saving,))
        rows = cursor.fetchall()
        for row in rows:
            result.append(row)
    except Exception as e:
        print(f"Error seleccionando todos los ahorros: {e}")
    finally:
        cursor.close()
        conn.close()
    return result

def select_saving_monto(monto: float):
    conn = connect_db()
    cursor = conn.cursor()
    result =[]
    try:
        with open ('sql/select_saving_monto.sql', 'r') as query:
            query = query.read()
        cursor.execute(query, (monto,))
        rows = cursor.fetchall()
        for row in rows:
            result.append(row)
    except Exception as e:
        print(f"Error seleccionando todos los ahorros: {e}")
    finally:
        cursor.close()
        conn.close()
    return result

def select_all_savings():
    conn = connect_db()
    cursor = conn.cursor()
    result =[]
    try:
        with open ('sql/select_all_savings.sql', 'r') as query:
            query = query.read()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            result.append(row)
    except Exception as e:
        print(f"Error seleccionando todos los ahorros: {e}")
    finally:
        cursor.close()
        conn.close()
    return result

# Ejemplo de uso
#create_savings_table()
ahorro_ejemplo = Saving(500000, 0.4, 20)
#insert_saving(ahorro_ejemplo)
select_savings(2)