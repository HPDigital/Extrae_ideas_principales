"""
Extrae_ideas_principales
"""

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Descargar las stopwords
nltk.download('punkt')
nltk.download('stopwords')

def limpiar_texto(texto):
    # Convertir el texto a minúsculas
    texto = texto.lower()
    # Eliminar la puntuación
    texto_sin_puntuacion = texto.translate(str.maketrans('', '', string.punctuation))
    return texto_sin_puntuacion

def obtener_ideas_principales(texto, num_ideas=5):
    # Limpiar el texto
    texto_limpio = limpiar_texto(texto)

    # Tokenizar el texto
    palabras = word_tokenize(texto_limpio)

    # Filtrar stopwords
    palabras_filtradas = [palabra for palabra in palabras if palabra not in stopwords.words('spanish')]

    # Contar frecuencia de palabras
    frecuencias = Counter(palabras_filtradas)

    # Obtener las palabras más comunes
    ideas_principales = frecuencias.most_common(num_ideas)

    return ideas_principales

# Leer el documento
ruta_documento = "C:\\Users\\HP\\Desktop\\CATO CURSOS-1-2024\\GER-TI CATO1-2024\\Cursos\\SEMANA 8\\Texto_video_2.txt"
with open(ruta_documento, 'r', encoding='utf-8') as archivo:
    texto_documento = archivo.read()

# Obtener las ideas principales
ideas_principales = obtener_ideas_principales(texto_documento, 5)
print("Ideas principales (palabras más frecuentes):")
for palabra, frecuencia in ideas_principales:
    print(f"{palabra}: {frecuencia}")


# In[ ]:






if __name__ == "__main__":
    pass
