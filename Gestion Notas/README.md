# Enunciado del ejercicio: Registro de notas

Crear un programa en Python que permita registrar y gestionar las notas de estudiantes en distintas asignaturas.

## 📝 Instrucciones:

El programa debe permitir las siguientes funcionalidades a través de un menú:

1. **Registrar nota de estudiante**
   - Solicitar el nombre del estudiante y el nombre de la asignatura.
   - Ingresar la nota correspondiente (entre 1.0 y 7.0).
   - Si el estudiante o la asignatura no existen, deben ser creados.
   - Si la asignatura ya está registrada para el estudiante, debe actualizarse la nota.

2. **Ver notas de los estudiantes**
   - Mostrar todos los estudiantes con sus asignaturas y notas registradas.

3. **Ver promedio general por estudiante**
   - Calcular el promedio de todas las notas de cada estudiante y mostrarlo.

4. **Salir del programa**
   - Finalizar la ejecución del programa con un mensaje de despedida.

## ✅ Requisitos técnicos

- Usar diccionarios anidados para almacenar la información.
- Validar que las notas sean numéricas y estén en el rango de 1.0 a 7.0.
- Manejar errores de formato (por ejemplo, si se ingresa texto en vez de un número).
- El programa debe repetirse hasta que el usuario elija salir.

## 💡 Estructura esperada de los datos

```python
{
  "ana": {
    "matematicas": {"nota": 6.5},
    "historia": {"nota": 5.0}
  },
  "pedro": {
    "lenguaje": {"nota": 6.0}
  }
}
