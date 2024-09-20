from collections import Counter
import random

filename = 'DS_libroEnTxt.txt'

def buildSuccessorMap(text):
    window = [] #inicialize window as list
    words = text.split()
    successorMap = {}
    for word in words:
        cleaned_word = word.strip('.;,-“’”:?—‘!()_"').lower() #clean words
        if cleaned_word:  # verificar que la palabra no esté vacía
            window.append(cleaned_word)
            if len(window) >= 2:
                bigram = tuple(window) # save current window as tuple
                ### Build SuccessorMap
                if bigram[0] not in successorMap: #si la palabra inicial no está registrada
                    successorMap[bigram[0]] = [bigram[1]] #Inicializa su mapa con la palabra
                else:
                    successorMap[bigram[0]].append(bigram[1]) #Añade palabras al mapa
                ###
                window.pop(0) 
    return successorMap

print("--------------------------------------------------------------------------\n")

with open(filename, 'r', encoding='utf-8') as book:
    successorMap = buildSuccessorMap(book.read())

print(successorMap['capable'])

######################## Interfaz de usuario #########################################
frase_completa = []
print("TRY TO BULD A PHRASE WITH ME: \nYOU SAY ONE WORD AND I SAY ANOTHER. YOU CAN STOP THE PROGRAM BY WRITING 'stop', AND YOU CAN STOP ME FROM GENERATING A NEXT WORD BY WRITING  A '.' POINT AT THE END OF YOUR INPUT \n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
palabra_actual = input("Introduce una palabra para comenzar (o 'stop' para finalizar): ").strip().lower()
frase_completa.append(palabra_actual)

while palabra_actual != "stop":
    if palabra_actual in successorMap:
        palabra_siguiente = random.choice(successorMap[palabra_actual])
        
        frase_completa.append(palabra_siguiente)
        print(f"Palabra generada: {palabra_siguiente}")
    else:
        print("La palabra no tiene sucesores conocidos en el texto.")
    
    palabra_actual = input("Introduce una nueva palabra (o 'stop' para finalizar): ")
    if palabra_actual != "stop":
        frase_completa.append(palabra_actual) #guarda el imput tal cual se haya escrito
    palabra_actual = palabra_actual.strip(';,-“’”:?—‘!()_"').strip().lower() #limpia antes de buscar en el successorMap

# Imprimir la frase completa
print("\nFrase completa creada:")
print(' '.join(frase_completa))
#####################################################################################

print("\n\n--------------------------------------------------------------------------")
