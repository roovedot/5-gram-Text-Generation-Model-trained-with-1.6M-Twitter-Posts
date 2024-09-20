import pickle
import random

# Cargar el SuccessorMap desde el archivo
with open('C:/Users/ikera/OneDrive/Escritorio/Asignaturas/IA_ExtraOficial/WS_IA_Extraoficial/Language Model/data/5gramSuccMap.pkl', 'rb') as f:
    print("cargando Diccionario...")
    successorMap = pickle.load(f)
    print("Cargado con exito")

print("------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# necesita 4 palabras que aparezcan seguidas en el texto (se podría modificar para cogerlas aleatoriamente del .txt)
word1 = 'hmm'
word2 = 'i'
word3 = 'dreamed'
word4 = 'that'
for i in range(150):
  print (word1, end=" ") #imprime una palabra por ciclo
  word5 = random.choice(successorMap[(word1, word2, word3, word4)])
  word1 = word2 #sobreescribimos las variables para avanzar por la frase
  word2 = word3 
  word3 = word4
  word4 = word5


print("\n\n------------------------------------------------------------------------------------------------------------------------------------------------------")
