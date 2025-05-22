import json
from pathlib import Path
from datetime import datetime

class ReminderEngine:
    def __init__(self, file_path="reminders.json", alarm_path="alarms.json"):
        self.reminders_file = Path(file_path)
        self.alarms_file = Path(alarm_path)
        self.reminders = self.load_file(self.reminders_file)
        self.alarms = self.load_file(self.alarms_file)

    def load_file(self, path):
        return json.loads(path.read_text()) if path.exists() else []

    def save_file(self, data, path):
        path.write_text(json.dumps(data, indent=2))

    # ----- Reminder Logic -----
    def set_reminder(self, task, time):
        reminder = {"task": task, "time": time}
        self.reminders.append(reminder)
        self.save_file(self.reminders, self.reminders_file)
        return f"🔔 Reminder set to '{task}' at {time}."

    def list_reminders(self):
        if not self.reminders:
            return "🔕 No reminders set."
        return "🔔 Reminders:\n" + "\n".join([f"- {r['task']} at {r['time']}" for r in self.reminders])

    def delete_reminder(self, task):
        initial = len(self.reminders)
        self.reminders = [r for r in self.reminders if r["task"].lower() != task.lower()]
        self.save_file(self.reminders, self.reminders_file)
        return "🗑️ Reminder deleted." if len(self.reminders) < initial else "⚠️ Reminder not found."

   
