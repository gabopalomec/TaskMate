from tasks.task_manager import TaskManager

def main():
    manager = TaskManager()
    while True:
        print("\n📋 TaskMate - Gestor de tareas")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Completar tarea")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            descripcion = input("Descripción de la tarea: ")
            manager.add_task(descripcion)
        elif opcion == "2":
            manager.list_tasks()
        elif opcion == "3":
            task_id = int(input("ID de tarea a completar: "))
            manager.complete_task(task_id)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
