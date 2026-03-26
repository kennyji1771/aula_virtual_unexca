import pandas as pd
import os

# Datos de ejemplo (primeras clases y temas)
data = [
    # Clase 1, tema 1
    {
        'PNF': 'Informática',
        'TrayectoID': 'arquitectura',
        'TrayectoTitulo': 'Arquitectura del Computador',
        'TrayectoNivel': 'Técnico Universitario Básico',
        'TrayectoDuracion': '2 Semestres',
        'SemestreID': 'sem1',
        'SemestreTitulo': 'Semestre I: Fundamentos y Componentes de la Máquina',
        'SemestreFilosofia': 'Conocer, Tocar, Comprender',
        'ClaseID': 'sem1_clase1',
        'ClaseTitulo': 'Clase 1: Evolución Histórica y Generalidades del Sistema Informático',
        'ClaseDescripcion': 'Recorrido por los hitos tecnológicos desde el ábaco hasta la computadora moderna.',
        'ClaseArchivos': '[{"nombre": "Presentación de la clase", "url": "https://drive.google.com/..."}]',
        'TemaID': 't1_1',
        'TemaTitulo': 'Línea de tiempo colaborativa',
        'ContenidoTexto': 'Construye con tus compañeros una línea de tiempo física en el aula usando imágenes y datos clave (Ábaco, ENIAC, IBM PC, dispositivos actuales).',
        'ContenidoImagen': 'Imagen/linea_tiempo.jpg',
        'ContenidoAudio': 'audio/linea_tiempo.mp3',
        'ContenidoVideo': '',
        'QuizPregunta': '',
        'QuizOpciones': '',
        'QuizCorrecta': '',
        'QuizFeedback': '',
        'Consideraciones': 'Usa material reciclado para la línea de tiempo.|Cada grupo debe presentar una era histórica.'
    },
    # Clase 1, tema 2
    {
        'PNF': 'Informática',
        'TrayectoID': 'arquitectura',
        'TrayectoTitulo': 'Arquitectura del Computador',
        'TrayectoNivel': 'Técnico Universitario Básico',
        'TrayectoDuracion': '2 Semestres',
        'SemestreID': 'sem1',
        'SemestreTitulo': 'Semestre I: Fundamentos y Componentes de la Máquina',
        'SemestreFilosofia': 'Conocer, Tocar, Comprender',
        'ClaseID': 'sem1_clase1',
        'ClaseTitulo': 'Clase 1: Evolución Histórica y Generalidades del Sistema Informático',
        'ClaseDescripcion': 'Recorrido por los hitos tecnológicos desde el ábaco hasta la computadora moderna.',
        'ClaseArchivos': '',
        'TemaID': 't1_2',
        'TemaTitulo': 'Video-análisis: Evolución de las computadoras',
        'ContenidoTexto': 'Observa el documental y responde la guía de preguntas sobre las generaciones de computadoras.',
        'ContenidoImagen': '',
        'ContenidoAudio': '',
        'ContenidoVideo': 'https://youtu.be/XXXX',
        'QuizPregunta': '¿Qué tecnología marcó la transición de la primera a la segunda generación?',
        'QuizOpciones': 'Transistores|Válvulas de vacío|Circuitos integrados|Microprocesadores',
        'QuizCorrecta': '0',
        'QuizFeedback': '¡Correcto! Los transistores reemplazaron a las válvulas de vacío, haciendo las computadoras más pequeñas y fiables.',
        'Consideraciones': 'El video está disponible en el canal del aula virtual.|Las respuestas se entregan en formato digital.'
    },
    # Clase 1, tema 3
    {
        'PNF': 'Informática',
        'TrayectoID': 'arquitectura',
        'TrayectoTitulo': 'Arquitectura del Computador',
        'TrayectoNivel': 'Técnico Universitario Básico',
        'TrayectoDuracion': '2 Semestres',
        'SemestreID': 'sem1',
        'SemestreTitulo': 'Semestre I: Fundamentos y Componentes de la Máquina',
        'SemestreFilosofia': 'Conocer, Tocar, Comprender',
        'ClaseID': 'sem1_clase1',
        'ClaseTitulo': 'Clase 1: Evolución Histórica y Generalidades del Sistema Informático',
        'ClaseDescripcion': 'Recorrido por los hitos tecnológicos desde el ábaco hasta la computadora moderna.',
        'ClaseArchivos': '',
        'TemaID': 't1_3',
        'TemaTitulo': 'Mapa conceptual: Entrada-Proceso-Salida (E-P-S)',
        'ContenidoTexto': 'Construye un mapa conceptual con ejemplos cotidianos del ciclo E-P-S. Identifica entradas, procesos y salidas en un microondas, una calculadora y un mensaje de WhatsApp.',
        'ContenidoImagen': 'Imagen/mapa_eps.jpg',
        'ContenidoAudio': 'audio/eps.mp3',
        'ContenidoVideo': '',
        'QuizPregunta': '',
        'QuizOpciones': '',
        'QuizCorrecta': '',
        'QuizFeedback': '',
        'Consideraciones': 'Puede realizarse en papel o digital.|Comparte tu mapa en el foro de la clase.'
    }
    # Puedes añadir aquí más clases y temas
]

# Crear DataFrame y guardar
df = pd.DataFrame(data)
df.to_excel('estructura_curso.xlsx', sheet_name='Datos', index=False)

print("✅ Plantilla Excel 'estructura_curso.xlsx' creada correctamente.")
