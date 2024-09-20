import csv
import re

# Nombre del archivo CSV de entrada y del archivo TXT de salida
csv_filename = 'C:/Users/ikera/OneDrive/Escritorio/Asignaturas/IA_ExtraOficial/WS_IA_Extraoficial/Language Model/DS_Tweets.csv'
txt_filename = 'C:/Users/ikera/OneDrive/Escritorio/Asignaturas/IA_ExtraOficial/WS_IA_Extraoficial/Language Model/DS_Tweets_text.txt'

def clean_tweet(text):
    # Eliminar menciones (@usuario)
    text = re.sub(r'@\w+', '', text)
    # Eliminar hashtags (#hashtag)
    text = re.sub(r'#\w+', '', text)
    # Eliminar enlaces (http:// o https://)
    text = re.sub(r'http\S+', '', text)
    # Eliminar guiones
    text = re.sub(r'-', '', text)
    # Eliminar múltiples espacios en blanco
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Abre el archivo CSV para leer y el archivo TXT para escribir
with open(csv_filename, 'r', encoding='utf-8') as csv_file, open(txt_filename, 'w', encoding='utf-8') as txt_file:
    # Crea un lector CSV
    csv_reader = csv.reader(csv_file)
    

    # Recorre cada fila del archivo CSV
    for row in csv_reader:
        # Extrae el texto del tweet, que se encuentra en la sexta columna (índice 5)
        tweet_text = row[5]
        tweet_text = clean_tweet(tweet_text)
        print(tweet_text)
        
        # Escribe el texto del tweet en el archivo TXT
        txt_file.write(tweet_text + '\n')


