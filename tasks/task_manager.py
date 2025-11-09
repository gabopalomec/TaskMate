class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description):
        task = {"id": self.next_id, "description": description, "done": False}
        self.tasks.append(task)
        self.next_id += 1
        print(f"Tarea agregada: {description}")

    def list_tasks(self):
        if not self.tasks:
            print("No hay tareas registradas.")
            return
        for task in self.tasks:
            status = "✅" if task["done"] else "❌"
            print(f"{task['id']}. {task['description']} [{status}]")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                print(f"Tarea completada: {task['description']}")
                return
        print("ID no encontrado.")
