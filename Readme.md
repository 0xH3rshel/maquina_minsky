# Intérprete de Máquina de Minsky en Python

Este script en Python interpreta y ejecuta programas escritos en el lenguaje de la **Máquina de Minsky** con instrucciones simples de incremento y decremento. Es útil para quienes deseen explorar los principios básicos de la computación y entender cómo funcionan las máquinas de registro.

## Características
- **Instrucciones soportadas**: `inc` (incremento) y `dec` (decremento condicional con salto).
    - inc [numero registro], [numero instruccion / "n" para siguiente linea / nombre etiqueta]
    - dec [numero registro], [salto para condicion si 0 (igual que inc pero condicional)], [salto condicion no 0 (igual que inc pero condicional)] 
- **Etiquetas y Saltos**: Permite definir etiquetas en el código y hacer saltos condicionales, facilitando la creación de bucles y estructuras de control.
- **Comentarios y Manejo de Errores**: Ignora comentarios y maneja errores comunes, como archivos no encontrados o instrucciones no válidas.

## Uso
1. Cada instrucción debe estar en una línea separada
2. Los comentarios comienzan con `#` y las etiquetas deben contener `:`.
3. Ejecuta el script con el archivo de programa como argumento:
```bash
$ python3 minsky.py programa.minsky
```

### Ejemplo de Archivo `.minsky`

```plaintext
# Ejemplo etiqueta
:start

# Inicio el registro 5 con valor 6
inc 5, n
inc 5, n
inc 5, n
inc 5, n
inc 5, n
inc 5, n

# Objetivo copiar el valor 5 al registro 9
# Utilizo un registro temporal 2 para llevar la cuenta
dec 2, n, zero_reg2 
dec 5, n, n
:bucle
inc 9, n
inc 2, n
dec 5, start, bucle

# Podemos ajustarlo a 0 despues si queremos
:zero_reg2
dec 2, n, zero_reg2

:fin
inc 1, n
```