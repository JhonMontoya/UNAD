import spacy
from spacy.lang.es.stop_words import STOP_WORDS
from rapidfuzz import process

nlp = spacy.load('es_core_news_sm')

def limpiar_texto(texto):
    doc = nlp(texto.lower())
    tokens = [token.lemma_ for token in doc if token.text not in STOP_WORDS]
    return ' '.join(tokens)

tareas = [
    'Hacer la compra',
    'Lavar el coche',
    'Hacer la comida',
    'Sacar a pasear al perro',
    'Hacer ejercicio',
    'Estudiar IA',
]

tareas_limpias = [limpiar_texto(tarea) for tarea in tareas]

while True:
    entrada = input('Introduce una tarea: ').lower()
    entrada_limpia = limpiar_texto(entrada)
    tarea_mas_similar, coincidencia, _ = process.extractOne(entrada_limpia, tareas_limpias)

    if coincidencia > 70:
        print(f'La tarea más similar es: {tareas[tareas_limpias.index(tarea_mas_similar)]}')
    else:
        print(coincidencia)
        print('No se ha encontrado ninguna tarea similar')
    
    continuar = input('¿Quieres introducir otra tarea? (s/n): ')
    if continuar.lower() != 's':
        break