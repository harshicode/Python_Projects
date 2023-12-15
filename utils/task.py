

class TaskManager:
    def __init__(self, tasks=None):
        if tasks is None:
            self.tasks = []
        else:
            self.tasks = tasks

    def show_tasks(self):
        print("Tasks:")
        # iterate over the tasks
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")
        print()

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added task: {task}")
        self.show_tasks()
        print()

