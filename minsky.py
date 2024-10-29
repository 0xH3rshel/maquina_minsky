import os
import sys

def main():
    # Comprobamos si se ha pasado el nombre del archivo como argumento
    if len(sys.argv) != 2:
        print("Error: Debes proporcionar el archivo de programa como argumento.")
        print("Uso: python3 minsky.py programa.minsky")
        sys.exit(1)
    
    file_name = sys.argv[1]
    
    # Comprobamos que el archivo existe
    if not os.path.isfile(file_name):
        print(f"Error: El archivo '{file_name}' no existe en el directorio actual.")
        sys.exit(1)
    
    print(f"Procesando '{file_name}'...")

    # Parsear programa
    program = parse_program(file_name)

    # Ejecutar programa
    registers = execute_program(program)
    print("Estado final de los registros:", registers)
    print("Fin del programa")
    return

def execute_program(program):

    registers = []
    instruction_pointer = 0
    
    # Ejecutar el programa hasta que el índice de instrucción esté fuera del rango
    while 0 <= instruction_pointer < len(program):
        # Obtener la instrucción actual
        instruction = program[instruction_pointer]
        instr_type, reg_num, dest_1, dest_2 = instruction
        
        while len(registers) <= reg_num:
            registers.append(0)
        
        if instr_type == 0:  # Instrucción 'inc'
            registers[reg_num] += 1
            instruction_pointer = dest_1

        elif instr_type == 1:  # Instrucción 'dec'
            if registers[reg_num] == 0:
                instruction_pointer = dest_1
            else:
                registers[reg_num] -= 1
                instruction_pointer = dest_2
    return registers

def parse_program(file_name):
    program = []
    labels = {}
    raw_instructions = []

    # Primera pasada para guardar etiquetas
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()

            # Ignorar comentarios y líneas vacías
            if line.startswith("#") or not line:
                continue

            # Captura de etiqueta (e.g., "start:")
            if ":" in line:
                label = line.replace(":", "").strip()
                labels[label] = len(raw_instructions)
            else:
                # Guardar la instrucción en crudo para procesarla después
                raw_instructions.append(line)

    # Segunda pasada para convertir instrucciones y resolver etiquetas
    for index, line in enumerate(raw_instructions):
        if line.startswith("inc"):
            parts = line.split(',')
            reg_num = int(parts[0].split()[1].strip())
            dest_label = parts[1].strip()
            dest_1 = int(index + 1) if dest_label == "n" else labels.get(dest_label, dest_label)
            program.append([0, reg_num, dest_1, 0])

        elif line.startswith("dec"):
            parts = line.split(',')
            reg_num = int(parts[0].split()[1].strip())
            dest_label_1 = parts[1].strip()
            dest_label_2 = parts[2].strip()
            dest_1 = int(index + 1) if dest_label_1 == "n" else labels.get(dest_label_1, dest_label_1)
            dest_2 = int(index + 1) if dest_label_2 == "n" else labels.get(dest_label_2, dest_label_2)
            program.append([1, reg_num, dest_1, dest_2])
        else:
            print(f"Advertencia: línea no reconocida '{line}'")

    return program

if __name__ == "__main__":
    main()
