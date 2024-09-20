from collections import Counter

filename = 'DS_libroEnTxt.txt'

def countWords(text):
    count = 0
    words = text.split() #divide las palabras
    for word in words: #para cada palabra:
        count += 1
    return count

###
''' Devuelve un item en forma de dupla (elemento, contador) de 
    el elemento cuyo contador sea {numero} si lo hay. 
    Devuelve una tupla vacía si no lo encuentra  '''
def buscarNumeroContador(contador, numero):
    found = False
    itemList = list(contador.items())
    i = 0
    while (i < len(itemList) and not found):
        if itemList[i][1] == numero:
            return itemList[i]
        i += 1
    print("no se ha encontrado")
    return ()

def makeWordCountDict(text):
    word_counts = {} #inicializa un diccionario
    words = text.split() #divide las palabras
    for word in words: #para cada palabra:
        word = word.lower().strip('.;,-“’”:?—‘!()_.')  # Normaliza y limpia
        if word in word_counts: #Si la palabra ya se ha registrado 
            word_counts[word] += 1 #Aumenta el contador
        else:   
            word_counts[word] = 1 #registra la palabra e inicializa el contador a 1
    return word_counts

def makeWordCounter(text):
    counter = Counter()
    words = text.split()
    for word in words:
        word = word.lower().strip('.;,-“’”:?—‘!()_.') #cleans word
        counter[word] += 1
    return counter

###
''' Returns a counter for each unique pair of consecutive words'''
def bigramCounter(text):
    window = [] #inicialize window as list
    words = text.split()
    bigram_counter = Counter()
    for word in words:
        cleaned_word = word.strip('.;,-“’”:?—‘!()_').lower() #clean words
        if cleaned_word:  # verificar que la palabra no esté vacía
            window.append(cleaned_word)
            if len(window) >= 2:
                bigram = tuple(window) # save current window as tuple
                bigram_counter[bigram] +=1 # add tuple to counter
                window.pop(0) 
    return bigram_counter


print("-----------------------------------------------------------------------")

#Imprime la primera linea del libro y un diccionario con ella
'''
with open(filename, 'r', encoding='utf-8') as reader:
    lines = reader.readlines()
    print(lines[1])
    print(makeWordCountDict(lines[1]))
'''

# Print the 25 most used words with Dictionary:
'''
with open(filename, 'r', encoding='utf-8') as book:
    wordCountDict = makeWordCountDict(book.read())
    sortedDict = sorted(wordCountDict.items(), key=lambda item: item[1], reverse=True)
    #sorts most used words first
    for i in range (25):
        print(f"{i+1}. '{sortedDict[i][0]}': {sortedDict[i][1]}")
        #Prints in format {position}. {Key}: {word Count}
'''

#Print the 25 most used words with Counter:
'''
with open(filename, 'r', encoding='utf-8') as book:
    wordCounter = makeWordCounter(book.read())
    print(wordCounter.most_common(25))
'''
#Prueba buscarNumeroContador()
'''
with open(filename, 'r', encoding='utf-8') as book:
    wordCounter = makeWordCounter(book.read())
    print(buscarNumeroContador(wordCounter, 444))
'''

#Contador de pares de palabras consecutivas
with open(filename, 'r', encoding='utf-8') as book:
    bigramCounter = bigramCounter(book.read())
    print(bigramCounter.most_common(5))

print("-----------------------------------------------------------------------")

