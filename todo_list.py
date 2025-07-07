import json
import os

TASKS_FILE = "tasks.json"

def cargar_tareas():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def guardar_tareas(tareas):
    with open(TASKS_FILE, "w") as f:
        json.dump(tareas, f, indent=4)

def agregar_tarea(nombre, descripcion):
    tareas = cargar_tareas()
    nueva_tarea = {
        "id": len(tareas) + 1,
        "nombre": nombre,
        "descripcion": descripcion,
        "estado": "Pendiente"
    }
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    print(f"Tarea '{nombre}' agregada correctamente.")

def listar_tareas():
    tareas = cargar_tareas()
    if not tareas:
        print("No hay tareas registradas.")
        return
    print("\nTareas registradas:")
    for tarea in tareas:
        print(f"- [{tarea['estado']}] {tarea['id']} - {tarea['nombre']}: {tarea['descripcion']}")

def marcar_completada(id_tarea):
    tareas = cargar_tareas()
    for tarea in tareas:
        if tarea["id"] == id_tarea:
            tarea["estado"] = "Completada"
            guardar_tareas(tareas)
            print(f"Tarea '{tarea['nombre']}' marcada como completada.")
            return
    print(f"No se encontró tarea con ID {id_tarea}.")

def limpiar_tareas():
    guardar_tareas([])
    print("Todas las tareas han sido eliminadas.")

def editar_tarea(nombre_tarea, nueva_descripcion):
    tareas = cargar_tareas()
    for tarea in tareas:
        if tarea["nombre"] == nombre_tarea:
            tarea["descripcion"] = nueva_descripcion
            guardar_tareas(tareas)
            print(f"Tarea '{nombre_tarea}' actualizada con nueva descripción.")
            return
    print(f"No se encontró la tarea '{nombre_tarea}'.")


def ver_tarea(nombre_tarea):
    tareas = cargar_tareas()
    for tarea in tareas:
        if tarea["nombre"] == nombre_tarea:
            print(f"\nTask: {tarea['nombre']}")
            print(f"Description: {tarea['descripcion']}")
            print(f"Status: {tarea['estado']}")
            return
    print(f"No se encontró la tarea '{nombre_tarea}'.")
def menu():
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Limpiar todas las tareas")
        print("5. Editar una tarea existente")
        print("6. Ver detalles de una tarea específica")
        print("7. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción: ")
            agregar_tarea(nombre, descripcion)
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            try:
                id_tarea = int(input("ID de la tarea a marcar como completada: "))
                marcar_completada(id_tarea)
            except ValueError:
                print("Por favor ingresa un número válido.")
        elif opcion == "4":
            limpiar_tareas()
        elif opcion == "5":
            nombre = input("Nombre de la tarea a editar: ")
            nueva_desc = input("Nueva descripción: ")
            editar_tarea(nombre, nueva_desc)
        elif opcion == "6":
            nombre = input("Nombre de la tarea a ver: ")
            ver_tarea(nombre)
        elif opcion == "7":
            print("Saliendo del gestor de tareas.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
if __name__ == "__main__":
    menu()