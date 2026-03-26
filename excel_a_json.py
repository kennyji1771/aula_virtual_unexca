import pandas as pd
import json
import os
import sys

def parse_json_field(value):
    """Convierte un string JSON a objeto Python."""
    if pd.isna(value) or value == '':
        return None
    try:
        return json.loads(value)
    except:
        print(f"⚠️  Advertencia: No se pudo parsear JSON: {value}")
        return None

def parse_list_field(value, separator='|'):
    """Convierte un string separado por | en lista."""
    if pd.isna(value) or value == '':
        return []
    return [item.strip() for item in value.split(separator)]

def main():
    print("📖 Leyendo archivo estructura_curso.xlsx...")
    try:
        df = pd.read_excel('estructura_curso.xlsx', sheet_name='Datos', dtype=str)
    except FileNotFoundError:
        print("❌ Error: No se encuentra el archivo estructura_curso.xlsx. Asegúrate de que esté en la misma carpeta.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error al leer el Excel: {e}")
        sys.exit(1)

    # Reemplazar NaN por cadena vacía
    df = df.fillna('')

    # Obtener el PNF (suponemos que todas las filas tienen el mismo)
    pnf = df['PNF'].iloc[0]

    # Estructura jerárquica
    trayectos = {}

    print("🔧 Procesando filas...")
    for idx, row in df.iterrows():
        # Nivel 1: Trayecto
        trayecto_id = row['TrayectoID']
        if trayecto_id not in trayectos:
            trayectos[trayecto_id] = {
                'id': trayecto_id,
                'titulo': row['TrayectoTitulo'],
                'nivel': row['TrayectoNivel'],
                'duracion': row['TrayectoDuracion'],
                'semestres': {}
            }
        # Nivel 2: Semestre
        semestre_id = row['SemestreID']
        if semestre_id not in trayectos[trayecto_id]['semestres']:
            trayectos[trayecto_id]['semestres'][semestre_id] = {
                'id': semestre_id,
                'titulo': row['SemestreTitulo'],
                'filosofia': row['SemestreFilosofia'],
                'clases': {}
            }
        # Nivel 3: Clase
        clase_id = row['ClaseID']
        if clase_id not in trayectos[trayecto_id]['semestres'][semestre_id]['clases']:
            archivos = parse_json_field(row['ClaseArchivos'])
            if archivos is None:
                archivos = []
            trayectos[trayecto_id]['semestres'][semestre_id]['clases'][clase_id] = {
                'id': clase_id,
                'titulo': row['ClaseTitulo'],
                'descripcion': row['ClaseDescripcion'],
                'archivos': archivos,
                'temas': []
            }
        # Nivel 4: Tema
        tema = {
            'id': row['TemaID'],
            'titulo': row['TemaTitulo'],
            'contenido': {
                'texto': row['ContenidoTexto']
            },
            'consideraciones': parse_list_field(row['Consideraciones'])
        }
        # Añadir campos opcionales solo si tienen contenido
        if row['ContenidoImagen']:
            tema['contenido']['imagen'] = row['ContenidoImagen']
        if row['ContenidoAudio']:
            tema['contenido']['audio'] = row['ContenidoAudio']
        if row['ContenidoVideo']:
            tema['contenido']['video'] = row['ContenidoVideo']
        # Quiz
        if row['QuizPregunta']:
            tema['contenido']['quiz'] = {
                'pregunta': row['QuizPregunta'],
                'opciones': parse_list_field(row['QuizOpciones']),
                'correcta': int(row['QuizCorrecta']) if row['QuizCorrecta'] else 0,
                'feedback': row['QuizFeedback']
            }
        # Agregar tema a la clase
        trayectos[trayecto_id]['semestres'][semestre_id]['clases'][clase_id]['temas'].append(tema)

    # Convertir diccionarios internos a listas para el JSON final
    output = {
        'pnf': pnf,
        'trayectos': []
    }
    for trayecto in trayectos.values():
        trayecto['semestres'] = list(trayecto['semestres'].values())
        for semestre in trayecto['semestres']:
            semestre['clases'] = list(semestre['clases'].values())
        output['trayectos'].append(trayecto)

    # Guardar JSON
    with open('estructura.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print("✅ estructura.json generado correctamente.")

if __name__ == "__main__":
    main()
