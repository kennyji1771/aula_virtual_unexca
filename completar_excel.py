import pandas as pd

# ========== SEMESTRE I (ya existente) ==========
filas = []

# Clase 1: Evolución Histórica
clase1_id = "sem1_clase1"
clase1_titulo = "Clase 1: Evolución Histórica y Generalidades del Sistema Informático"
clase1_desc = "Recorrido por los hitos tecnológicos desde el ábaco hasta la computadora moderna."
archivos1 = '[{"nombre":"Presentación de la clase","url":"https://drive.google.com/..."},{"nombre":"Línea de tiempo interactiva","url":"https://drive.google.com/..."}]'

filas.append({
    'PNF': 'Informática',
    'TrayectoID': 'arquitectura',
    'TrayectoTitulo': 'Arquitectura del Computador',
    'TrayectoNivel': 'Técnico Universitario Básico',
    'TrayectoDuracion': '2 Semestres',
    'SemestreID': 'sem1',
    'SemestreTitulo': 'Semestre I: Fundamentos y Componentes de la Máquina',
    'SemestreFilosofia': 'Conocer, Tocar, Comprender',
    'ClaseID': clase1_id,
    'ClaseTitulo': clase1_titulo,
    'ClaseDescripcion': clase1_desc,
    'ClaseArchivos': archivos1,
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
})
filas.append({
    'PNF': 'Informática',
    'TrayectoID': 'arquitectura',
    'TrayectoTitulo': 'Arquitectura del Computador',
    'TrayectoNivel': 'Técnico Universitario Básico',
    'TrayectoDuracion': '2 Semestres',
    'SemestreID': 'sem1',
    'SemestreTitulo': 'Semestre I: Fundamentos y Componentes de la Máquina',
    'SemestreFilosofia': 'Conocer, Tocar, Comprender',
    'ClaseID': clase1_id,
    'ClaseTitulo': clase1_titulo,
    'ClaseDescripcion': clase1_desc,
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
})
filas.append({
    'PNF': 'Informática',
    'TrayectoID': 'arquitectura',
    'TrayectoTitulo': 'Arquitectura del Computador',
    'TrayectoNivel': 'Técnico Universitario Básico',
    'TrayectoDuracion': '2 Semestres',
    'SemestreID': 'sem1',
    'SemestreTitulo': 'Semestre I: Fundamentos y Componentes de la Máquina',
    'SemestreFilosofia': 'Conocer, Tocar, Comprender',
    'ClaseID': clase1_id,
    'ClaseTitulo': clase1_titulo,
    'ClaseDescripcion': clase1_desc,
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
})

# Clase 2: Componentes del Hardware
clase2_id = "sem1_clase2"
clase2_titulo = "Clase 2: Componentes del Hardware, Ensamblaje y Normas de Seguridad"
clase2_desc = "Identificación y manipulación de los componentes físicos de un computador. Normas de seguridad electrostática y técnicas de ensamblaje."
archivos2 = '[{"nombre":"Guía de seguridad y herramientas","url":"https://drive.google.com/..."},{"nombre":"Video: Despiece y ensamblaje","url":"https://www.youtube.com/watch?v=YYYY"}]'

filas.append({
    'PNF': 'Informática',
    'TrayectoID': 'arquitectura',
    'TrayectoTitulo': 'Arquitectura del Computador',
    'TrayectoNivel': 'Técnico Universitario Básico',
    'TrayectoDuracion': '2 Semestres',
    'SemestreID': 'sem1',
    'SemestreTitulo': 'Semestre I: Fundamentos y Componentes de la Máquina',
    'SemestreFilosofia': 'Conocer, Tocar, Comprender',
    'ClaseID': clase2_id,
    'ClaseTitulo': clase2_titulo,
    'ClaseDescripcion': clase2_desc,
    'ClaseArchivos': archivos2,
    'TemaID': 't2_1',
    'TemaTitulo': 'Demostración en vivo: Despiece de un computador',
    'ContenidoTexto': 'El instructor realiza el despiece completo de un computador mientras explica cada componente y su función.',
    'ContenidoImagen': 'Imagen/despiece.jpg',
    'ContenidoAudio': '',
    'ContenidoVideo': 'https://youtu.be/YYYY',
    'QuizPregunta': '',
    'QuizOpciones': '',
    'QuizCorrecta': '',
    'QuizFeedback': '',
    'Consideraciones': 'Toma notas de los pasos de seguridad.|Identifica al menos 5 componentes.'
})
filas.append({
    'PNF': 'Informática',
    'TrayectoID': 'arquitectura',
    'TrayectoTitulo': 'Arquitectura del Computador',
    'TrayectoNivel': 'Técnico Universitario Básico',
    'TrayectoDuracion': '2 Semestres',
    'SemestreID': 'sem1',
    'SemestreTitulo': 'Semestre I: Fundamentos y Componentes de la Máquina',
    'SemestreFilosofia': 'Conocer, Tocar, Comprender',
    'ClaseID': clase2_id,
    'ClaseTitulo': clase2_titulo,
    'ClaseDescripcion': clase2_desc,
    'ClaseArchivos': '',
    'TemaID': 't2_2',
    'TemaTitulo': 'Práctica: Ensamblaje con pulsera antiestática',
    'ContenidoTexto': 'En parejas, arman y desarman un computador siguiendo la guía, aplicando normas de seguridad.',
    'ContenidoImagen': 'Imagen/ensamblaje.jpg',
    'ContenidoAudio': '',
    'ContenidoVideo': '',
    'QuizPregunta': '',
    'QuizOpciones': '',
    'QuizCorrecta': '',
    'QuizFeedback': '',
    'Consideraciones': 'Usa la pulsera antiestática en todo momento.|Registra cada paso con fotos.'
})

# Clase 3: Sistemas Numéricos
clase3_id = "sem1_clase3"
clase3_titulo = "Clase 3: Sistemas Numéricos y Representación de Datos"
clase3_desc = "Estudio de los sistemas binario, octal, hexadecimal y su relación con el mundo digital. Conversiones y representación de datos en computadoras."
archivos3 = '[{"nombre":"Tablas de conversión","url":"https://drive.google.com/..."},{"nombre":"Calculadora binaria en línea","url":"https://www.rapidtables.com/convert/number/binary-to-decimal.html"}]'

filas.append({
    'PNF': 'Informática',
    'TrayectoID': 'arquitectura',
    'TrayectoTitulo': 'Arquitectura del Computador',
    'TrayectoNivel': 'Técnico Universitario Básico',
    'TrayectoDuracion': '2 Semestres',
    'SemestreID': 'sem1',
    'SemestreTitulo': 'Semestre I: Fundamentos y Componentes de la Máquina',
    'SemestreFilosofia': 'Conocer, Tocar, Comprender',
    'ClaseID': clase3_id,
    'ClaseTitulo': clase3_titulo,
    'ClaseDescripcion': clase3_desc,
    'ClaseArchivos': archivos3,
    'TemaID': 't3_1',
    'TemaTitulo': 'Analogía con monedas y billetes',
    'ContenidoTexto': 'Explicación de sistemas numéricos usando diferentes monedas (sistema decimal vs. binario como "tengo/no tengo").',
    'ContenidoImagen': 'Imagen/monedas.jpg',
    'ContenidoAudio': '',
    'ContenidoVideo': '',
    'QuizPregunta': '',
    'QuizOpciones': '',
    'QuizCorrecta': '',
    'QuizFeedback': '',
    'Consideraciones': ''
})
filas.append({
    'PNF': 'Informática',
    'TrayectoID': 'arquitectura',
    'TrayectoTitulo': 'Arquitectura del Computador',
    'TrayectoNivel': 'Técnico Universitario Básico',
    'TrayectoDuracion': '2 Semestres',
    'SemestreID': 'sem1',
    'SemestreTitulo': 'Semestre I: Fundamentos y Componentes de la Máquina',
    'SemestreFilosofia': 'Conocer, Tocar, Comprender',
    'ClaseID': clase3_id,
    'ClaseTitulo': clase3_titulo,
    'ClaseDescripcion': clase3_desc,
    'ClaseArchivos': '',
    'TemaID': 't3_2',
    'TemaTitulo': 'Taller: La Calculadora Humana',
    'ContenidoTexto': 'Los estudiantes, usando tarjetas con dígitos binarios, se convierten en "bits" y realizan conversiones en grupo moviéndose físicamente.',
    'ContenidoImagen': '',
    'ContenidoAudio': 'audio/calculadora_humana.mp3',
    'ContenidoVideo': '',
    'QuizPregunta': '',
    'QuizOpciones': '',
    'QuizCorrecta': '',
    'QuizFeedback': '',
    'Consideraciones': 'Crea una tarjeta con tu nombre en binario.'
})

# Clase 4: Lógica Digital
clase4_id = "sem1_clase4"
clase4_titulo = "Clase 4: Lógica Digital y Circuitos Combinacionales"
clase4_desc = "Principios de álgebra booleana, compuertas lógicas y diseño de circuitos combinacionales. Introducción a la simulación con software."
archivos4 = '[{"nombre":"Simulador Logisim","url":"https://sourceforge.net/projects/circuit/"},{"nombre":"Práctica: Tablas de verdad","url":"https://drive.google.com/..."}]'

filas.append({
    'PNF': 'Informática',
    'TrayectoID': 'arquitectura',
    'TrayectoTitulo': 'Arquitectura del Computador',
    'TrayectoNivel': 'Técnico Universitario Básico',
    'TrayectoDuracion': '2 Semestres',
    'SemestreID': 'sem1',
    'SemestreTitulo': 'Semestre I: Fundamentos y Componentes de la Máquina',
    'SemestreFilosofia': 'Conocer, Tocar, Comprender',
    'ClaseID': clase4_id,
    'ClaseTitulo': clase4_titulo,
    'ClaseDescripcion': clase4_desc,
    'ClaseArchivos': archivos4,
    'TemaID': 't4_1',
    'TemaTitulo': 'Juego de interruptores',
    'ContenidoTexto': 'Demostración física con interruptores y bombillas para representar compuertas AND, OR y NOT.',
    'ContenidoImagen': 'Imagen/interruptores.jpg',
    'ContenidoAudio': '',
    'ContenidoVideo': '',
    'QuizPregunta': '',
    'QuizOpciones': '',
    'QuizCorrecta': '',
    'QuizFeedback': '',
    'Consideraciones': ''
})
filas.append({
    'PNF': 'Informática',
    'TrayectoID': 'arquitectura',
    'TrayectoTitulo': 'Arquitectura del Computador',
    'TrayectoNivel': 'Técnico Universitario Básico',
    'TrayectoDuracion': '2 Semestres',
    'SemestreID': 'sem1',
    'SemestreTitulo': 'Semestre I: Fundamentos y Componentes de la Máquina',
    'SemestreFilosofia': 'Conocer, Tocar, Comprender',
    'ClaseID': clase4_id,
    'ClaseTitulo': clase4_titulo,
    'ClaseDescripcion': clase4_desc,
    'ClaseArchivos': '',
    'TemaID': 't4_2',
    'TemaTitulo': 'Taller: Construyendo con compuertas',
    'ContenidoTexto': 'Uso de kits de electrónica básica para construir circuitos simples: AND, OR, NOT, XOR.',
    'ContenidoImagen': 'Imagen/circuito.jpg',
    'ContenidoAudio': '',
    'ContenidoVideo': '',
    'QuizPregunta': '',
    'QuizOpciones': '',
    'QuizCorrecta': '',
    'QuizFeedback': '',
    'Consideraciones': 'Verifica la tabla de verdad de cada compuerta.|Graba un video mostrando tu circuito funcionando.'
})

# ========== SEMESTRE II ==========
# Clase 5: Microprocesadores y Ciclo de Ejecución
clase5_id = "sem2_clase1"
clase5_titulo = "Clase 1: Microprocesadores y Ciclo de Ejecución de Instrucciones"
clase5_desc = "Estructura interna de la CPU, ciclo fetch-decode-execute, arquitecturas CISC/RISC."
archivos5 = '[{"nombre":"Simulador CPU","url":"https://www.cpusimulator.com/"},{"nombre":"Documento: Ciclo de instrucción","url":"https://drive.google.com/..."}]'

filas.append({
    'PNF': 'Informática',
    'TrayectoID': 'arquitectura',
    'TrayectoTitulo': 'Arquitectura del Computador',
    'TrayectoNivel': 'Técnico Universitario Básico',
    'TrayectoDuracion': '2 Semestres',
    'SemestreID': 'sem2',
    'SemestreTitulo': 'Semestre II: Arquitectura Interna y Gestión de Recursos',
    'SemestreFilosofia': 'Del Hardware al Sistema Vivo',
    'ClaseID': clase5_id,
    'ClaseTitulo': clase5_titulo,
    'ClaseDescripcion': clase5_desc,
    'ClaseArchivos': archivos5,
    'TemaID': 't5_1',
    'TemaTitulo': 'Analogía del chef en la cocina',
    'ContenidoTexto': 'La CPU es el chef, la ALU cocina, la Unidad de Control sigue la receta, los Registros son la mesa de trabajo.',
    'ContenidoImagen': '',
    'ContenidoAudio': '',
    'ContenidoVideo': 'https://youtu.be/XXXX',
    'QuizPregunta': '¿Cuál es la función de la Unidad de Control?',
    'QuizOpciones': 'Ejecutar operaciones aritméticas|Coordinar las operaciones del procesador|Almacenar datos temporales|Gestionar la memoria',
    'QuizCorrecta': '1',
    'QuizFeedback': 'Correcto. La Unidad de Control dirige el flujo de instrucciones.',
    'Consideraciones': 'Observa el video y anota las partes de la CPU.'
})
filas.append({
    'PNF': 'Informática',
    'TrayectoID': 'arquitectura',
    'TrayectoTitulo': 'Arquitectura del Computador',
    'TrayectoNivel': 'Técnico Universitario Básico',
    'TrayectoDuracion': '2 Semestres',
    'SemestreID': 'sem2',
    'SemestreTitulo': 'Semestre II: Arquitectura Interna y Gestión de Recursos',
    'SemestreFilosofia': 'Del Hardware al Sistema Vivo',
    'ClaseID': clase5_id,
    'ClaseTitulo': clase5_titulo,
    'ClaseDescripcion': clase5_desc,
    'ClaseArchivos': '',
    'TemaID': 't5_2',
    'TemaTitulo': 'Simulación del ciclo fetch-decode-execute',
    'ContenidoTexto': 'Usa un simulador de CPU para ejecutar instrucciones paso a paso y observar el flujo.',
    'ContenidoImagen': '',
    'ContenidoAudio': '',
    'ContenidoVideo': '',
    'QuizPregunta': '',
    'QuizOpciones': '',
    'QuizCorrecta': '',
    'QuizFeedback': '',
    'Consideraciones': 'Registra en un informe las instrucciones ejecutadas.'
})

# Clase 6: Jerarquía de Memoria
clase6_id = "sem2_clase2"
clase6_titulo = "Clase 2: Jerarquía y Tecnologías de Memorias"
clase6_desc = "Pirámide de memoria, tipos de memoria (RAM, caché, ROM), memoria virtual."
archivos6 = '[{"nombre":"Presentación memorias","url":"https://drive.google.com/..."}]'

filas.append({
    'PNF': 'Informática',
    'TrayectoID': 'arquitectura',
    'TrayectoTitulo': 'Arquitectura del Computador',
    'TrayectoNivel': 'Técnico Universitario Básico',
    'TrayectoDuracion': '2 Semestres',
    'SemestreID': 'sem2',
    'SemestreTitulo': 'Semestre II: Arquitectura Interna y Gestión de Recursos',
    'SemestreFilosofia': 'Del Hardware al Sistema Vivo',
    'ClaseID': clase6_id,
    'ClaseTitulo': clase6_titulo,
    'ClaseDescripcion': clase6_desc,
    'ClaseArchivos': archivos6,
    'TemaID': 't6_1',
    'TemaTitulo': 'Pirámide física de memorias',
    'ContenidoTexto': 'Construye una pirámide con cajas que representan registros, caché, RAM y disco.',
    'ContenidoImagen': '',
    'ContenidoAudio': '',
    'ContenidoVideo': '',
    'QuizPregunta': '¿Qué memoria es la más rápida?',
    'QuizOpciones': 'Disco duro|RAM|Caché|Registros',
    'QuizCorrecta': '3',
    'QuizFeedback': 'Los registros son los más rápidos, seguidos por la caché.',
    'Consideraciones': 'Explica por qué la jerarquía mejora el rendimiento.'
})
filas.append({
    'PNF': 'Informática',
    'TrayectoID': 'arquitectura',
    'TrayectoTitulo': 'Arquitectura del Computador',
    'TrayectoNivel': 'Técnico Universitario Básico',
    'TrayectoDuracion': '2 Semestres',
    'SemestreID': 'sem2',
    'SemestreTitulo': 'Semestre II: Arquitectura Interna y Gestión de Recursos',
    'SemestreFilosofia': 'Del Hardware al Sistema Vivo',
    'ClaseID': clase6_id,
    'ClaseTitulo': clase6_titulo,
    'ClaseDescripcion': clase6_desc,
    'ClaseArchivos': '',
    'TemaID': 't6_2',
    'TemaTitulo': 'Midiendo tiempos de acceso',
    'ContenidoTexto': 'Usa herramientas del sistema para medir el tiempo de acceso a diferentes niveles de memoria.',
    'ContenidoImagen': '',
    'ContenidoAudio': '',
    'ContenidoVideo': '',
    'QuizPregunta': '',
    'QuizOpciones': '',
    'QuizCorrecta': '',
    'QuizFeedback': '',
    'Consideraciones': 'Documenta los resultados en una tabla.'
})

# Clase 7: Entrada/Salida y Buses
clase7_id = "sem2_clase3"
clase7_titulo = "Clase 3: Subsistema de Entrada/Salida y Transferencia de Información"
clase7_desc = "Dispositivos de E/S, técnicas de transferencia (polling, interrupciones, DMA), buses de datos."
archivos7 = '[{"nombre":"Diagrama de buses","url":"https://drive.google.com/..."}]'

filas.append({
    'PNF': 'Informática',
    'TrayectoID': 'arquitectura',
    'TrayectoTitulo': 'Arquitectura del Computador',
    'TrayectoNivel': 'Técnico Universitario Básico',
    'TrayectoDuracion': '2 Semestres',
    'SemestreID': 'sem2',
    'SemestreTitulo': 'Semestre II: Arquitectura Interna y Gestión de Recursos',
    'SemestreFilosofia': 'Del Hardware al Sistema Vivo',
    'ClaseID': clase7_id,
    'ClaseTitulo': clase7_titulo,
    'ClaseDescripcion': clase7_desc,
    'ClaseArchivos': archivos7,
    'TemaID': 't7_1',
    'TemaTitulo': 'Simulación de transferencias (polling, interrupciones, DMA)',
    'ContenidoTexto': 'En grupos, representen físicamente los roles (CPU, dispositivo, DMA) y simulen las tres técnicas.',
    'ContenidoImagen': '',
    'ContenidoAudio': '',
    'ContenidoVideo': '',
    'QuizPregunta': '¿Qué técnica libera a la CPU durante la transferencia de datos?',
    'QuizOpciones': 'Polling|Interrupciones|DMA|Cache',
    'QuizCorrecta': '2',
    'QuizFeedback': 'DMA permite que los datos se transfieran sin intervención constante de la CPU.',
    'Consideraciones': 'Dibuja un diagrama de cada técnica.'
})
filas.append({
    'PNF': 'Informática',
    'TrayectoID': 'arquitectura',
    'TrayectoTitulo': 'Arquitectura del Computador',
    'TrayectoNivel': 'Técnico Universitario Básico',
    'TrayectoDuracion': '2 Semestres',
    'SemestreID': 'sem2',
    'SemestreTitulo': 'Semestre II: Arquitectura Interna y Gestión de Recursos',
    'SemestreFilosofia': 'Del Hardware al Sistema Vivo',
    'ClaseID': clase7_id,
    'ClaseTitulo': clase7_titulo,
    'ClaseDescripcion': clase7_desc,
    'ClaseArchivos': '',
    'TemaID': 't7_2',
    'TemaTitulo': 'Identificación de buses en placa madre',
    'ContenidoTexto': 'Observa una placa madre real e identifica los conectores de expansión (PCIe, SATA, etc.).',
    'ContenidoImagen': '',
    'ContenidoAudio': '',
    'ContenidoVideo': '',
    'QuizPregunta': '',
    'QuizOpciones': '',
    'QuizCorrecta': '',
    'QuizFeedback': '',
    'Consideraciones': 'Fotografía los conectores y etiquétalos.'
})

# Clase 8: BIOS, UEFI y Sistemas Operativos
clase8_id = "sem2_clase4"
clase8_titulo = "Clase 4: El Puente Software-Hardware: BIOS, UEFI y Sistemas Operativos"
clase8_desc = "Configuración de BIOS/UEFI, particionamiento de discos, instalación de sistemas operativos."
archivos8 = '[{"nombre":"Guía de instalación Ubuntu","url":"https://ubuntu.com/tutorials"},{"nombre":"Manual de VirtualBox","url":"https://www.virtualbox.org/manual"}]'

filas.append({
    'PNF': 'Informática',
    'TrayectoID': 'arquitectura',
    'TrayectoTitulo': 'Arquitectura del Computador',
    'TrayectoNivel': 'Técnico Universitario Básico',
    'TrayectoDuracion': '2 Semestres',
    'SemestreID': 'sem2',
    'SemestreTitulo': 'Semestre II: Arquitectura Interna y Gestión de Recursos',
    'SemestreFilosofia': 'Del Hardware al Sistema Vivo',
    'ClaseID': clase8_id,
    'ClaseTitulo': clase8_titulo,
    'ClaseDescripcion': clase8_desc,
    'ClaseArchivos': archivos8,
    'TemaID': 't8_1',
    'TemaTitulo': 'Explorando la BIOS/UEFI',
    'ContenidoTexto': 'Accede a la configuración del firmware y explora las opciones de arranque, fecha/hora, etc.',
    'ContenidoImagen': '',
    'ContenidoAudio': '',
    'ContenidoVideo': '',
    'QuizPregunta': '¿Qué tecnología reemplazó a la BIOS tradicional?',
    'QuizOpciones': 'UEFI|CMOS|POST|EEPROM',
    'QuizCorrecta': '0',
    'QuizFeedback': 'UEFI (Unified Extensible Firmware Interface) es el estándar actual.',
    'Consideraciones': 'Toma capturas de las pantallas de la BIOS/UEFI.'
})
filas.append({
    'PNF': 'Informática',
    'TrayectoID': 'arquitectura',
    'TrayectoTitulo': 'Arquitectura del Computador',
    'TrayectoNivel': 'Técnico Universitario Básico',
    'TrayectoDuracion': '2 Semestres',
    'SemestreID': 'sem2',
    'SemestreTitulo': 'Semestre II: Arquitectura Interna y Gestión de Recursos',
    'SemestreFilosofia': 'Del Hardware al Sistema Vivo',
    'ClaseID': clase8_id,
    'ClaseTitulo': clase8_titulo,
    'ClaseDescripcion': clase8_desc,
    'ClaseArchivos': '',
    'TemaID': 't8_2',
    'TemaTitulo': 'Particionamiento e instalación de sistemas operativos',
    'ContenidoTexto': 'Usa una máquina virtual para crear particiones (MBR y GPT) e instalar un sistema operativo libre.',
    'ContenidoImagen': '',
    'ContenidoAudio': '',
    'ContenidoVideo': '',
    'QuizPregunta': '',
    'QuizOpciones': '',
    'QuizCorrecta': '',
    'QuizFeedback': '',
    'Consideraciones': 'Documenta el proceso con capturas de pantalla.'
})

# ========== GENERAR EL ARCHIVO EXCEL ==========
df = pd.DataFrame(filas)
df.to_excel('estructura_curso.xlsx', sheet_name='Datos', index=False)

print("✅ Archivo estructura_curso.xlsx generado con todas las clases y temas (ambos semestres).")
print(f"   Total de filas: {len(df)}")
