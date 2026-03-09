import pandas as pd
import customtkinter as ctk
from tkinter import messagebox as mb

def convert_file(path:str) -> pd.DataFrame:
    '''
        Este script permite convertir un archivo csv a otro csv, con las columnas indicadas por el header
    '''

    with open(path, 'r') as f:
        lines = f.readlines()
        header = lines[0].strip().split(',')

        new_text = []
        new_text.append(header)

        for l in lines[1:]:

            if len(l.strip().split(',')) == 2*(len(header)) - 1:
                contador = 0
                n = ""

                for char in l.strip():
                    if char == ',':
                        contador +=1


                        if contador %2 == 0:
                            n += "."
                        
                        else:
                            n += ","
                    else:
                        n += char

                new_text.append(n.split(','))

    df = pd.DataFrame(new_text[1:], columns=new_text[0])

    if 'Nro.' in df.columns:
        df['Nro.'] = pd.to_numeric(df['Nro.'], errors='coerce').astype("Int64")
    
    if 'Time' in df.columns:
        df['Time'] = pd.to_numeric(df['Time'], errors='coerce')

    if 'Speed' in df.columns:
        df['Speed'] = pd.to_numeric(df['Speed'], errors='coerce')
    
    if 'distance' in df.columns:
        df['distance']  = pd.to_numeric(df['distance'], errors='coerce')

    if 'Force' in df.columns:
        df['Force']  = pd.to_numeric(df['Force'], errors='coerce')

    save_path = ctk.filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

    if save_path:
        df.to_excel(save_path, engine='openpyxl', index=False)
        mb.showinfo(title='Exito', message='Archivo convertido y guardado exitosamente.')

    else:
        mb.showerror(title='Error', message='No se seleccionó una ubicación para guardar el archivo.')

if __name__ == '__main__':
    path = 'datos_originales.csv'
    df = convert_file(path)
    df.to_excel('datos_convertidos.xlsx', engine='openpyxl', index=False) 