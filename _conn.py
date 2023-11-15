from tkinter import messagebox
import mysql.connector

def banco_select(consulta):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="piestoque"
        )
        
        cursor = conn.cursor()

        cursor.execute(consulta)
        resultado = cursor.fetchall()
        
        conn.commit()  
        cursor.close()
        conn.close()

        return (resultado)

    except mysql.connector.Error as e:
        messagebox.showerror("Erro de Conexão", f"Erro: {e}")
        raise  # Levanta a exceção novamente para ser tratada no código que chamou a função

def banco_default(**consulta):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="piestoque"
        )
        
        cursor = conn.cursor()

        cursor.execute(consulta['querry'])
        if consulta['last_ID']:
            last_id = cursor.lastrowid
        else:
            last_id = None

        # Se for uma consulta SELECT, recuperar os resultados

        conn.commit()  
        cursor.close()
        conn.close()

        return (last_id)

    except mysql.connector.Error as e:
        messagebox.showerror("Erro de Conexão", f"Erro: {e}")
        raise  # Levanta a exceção novamente para ser tratada no código que chamou a função

def teste():
    print("teste")
