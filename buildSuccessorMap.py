import pickle
import re

filename = 'C:/Users/ikera/OneDrive/Escritorio/Asignaturas/IA_ExtraOficial/WS_IA_Extraoficial/Language Model/data/DS_Tweets_text.txt'

def clean_tweet(text):
    # Eliminar menciones (@usuario)
    text = re.sub(r'@\w+', '', text)
    # Eliminar hashtags (#hashtag)
    text = re.sub(r'#\w+', '', text)
    # Eliminar &s 
    text = re.sub(r'&\S+', '', text)
    # Eliminar enlaces (http:// o https://)
    text = re.sub(r'http\S+', '', text)
    # Eliminar guiones
    text = re.sub(r'-', '', text)
    # Eliminar múltiples espacios en blanco
    text = re.sub(r'\s+', ' ', text).strip()
    return text


'''def buildTrigramSuccessorMap(text):
    window = [] #inicialize window as list
    words = text.split()
    successorMap = {}
    for word in words:
        cleaned_word = clean_tweet(word) #Clean
        cleaned_word = word.lower().strip(';-“’”:—‘!()_"') #Normalize punctuationExamples=['.;,-“’”:?—‘!()_"']
        if cleaned_word:  # verificar que la palabra no esté vacía
            window.append(cleaned_word)
            if len(window) >= 3:
                bigram = (window[0], window[1]) # first 2 words as context
                successor = window[2] #3rd word as successor to the bigram
                ### Build SuccessorMap
                if bigram not in successorMap: #si la palabra inicial no está registrada
                    successorMap[bigram] = [successor] #Inicializa su mapa con la palabra
                else:
                    successorMap[bigram].append(successor) #Añade palabras al mapa
                ###
                window.pop(0) 
    return successorMap'''


def build5gramSuccessorMap(text):
    window = [] #inicialize window as list
    words = text.split()
    successorMap = {}
    for word in words:
        cleaned_word = clean_tweet(word) #Clean
        cleaned_word = word.lower().strip(';-“’”:—‘!()_"') #Normalize punctuationExamples=['.;,-“’”:?—‘!()_"']
        if cleaned_word:  # verificar que la palabra no esté vacía
            window.append(cleaned_word)
            if len(window) >= 5:
                bigram = (window[0], window[1], window[2], window[3]) # first 4 words as context
                successor = window[4] #3rd word as successor to the bigram
                ### Build SuccessorMap
                if bigram not in successorMap: #si la palabra inicial no está registrada
                    successorMap[bigram] = [successor] #Inicializa su mapa con la palabra
                else:
                    successorMap[bigram].append(successor) #Añade palabras al mapa
                ###
                window.pop(0) 
    return successorMap

print("--------------------------------------------------------------------------\n")

with open(filename, 'r', encoding='utf-8') as dataSet:
    successorMap = build5gramSuccessorMap(dataSet.read())
    with open('5gramSuccMap_5gram.pkl', 'wb') as f:
        pickle.dump(successorMap, f)



print("\n\n--------------------------------------------------------------------------")
