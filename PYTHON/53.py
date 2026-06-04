from datetime import datetime

class Task:
    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.priority = priority

    def __str__(self):
        return f"{self.name} | Due: {self.due_date.date()} | Priority: {self.priority}"


class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_sorted_tasks(self):
        return sorted(self.tasks, key=lambda x: x.due_date)

    def get_overdue_tasks(self):
        now = datetime.now()
        return [task for task in self.tasks if task.due_date < now]

    def show_schedule(self):
        print("\n--- TASK SCHEDULE (Sorted by Due Date) ---")
        for task in self.get_sorted_tasks():
            print(task)

    def show_overdue(self):
        print("\n--- OVERDUE TASKS ---")
        overdue = self.get_overdue_tasks()

        if not overdue:
            print("No overdue tasks!")
            return

        for task in overdue:
            print(task)


# ---------------- Demo ----------------
scheduler = TaskScheduler()

scheduler.add_task(Task("Assignment", "2026-05-20", 2))
scheduler.add_task(Task("Project", "2026-06-01", 1))
scheduler.add_task(Task("Exam Prep", "2026-05-10", 3))
scheduler.add_task(Task("Report", "2026-05-01", 2))

scheduler.show_schedule()
scheduler.show_overdue()