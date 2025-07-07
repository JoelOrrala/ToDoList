from behave import given, when, then
import subprocess
import os
import json

TASKS_FILE = "tasks.json"

# Helper functions
def clear_tasks_file():
    if os.path.exists(TASKS_FILE):
        os.remove(TASKS_FILE)

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

@given('the to-do list is empty')
def step_impl(context):
    clear_tasks_file()

@when('the user adds a task "{task}" with description "{description}"')
def step_impl(context, task, description):
    subprocess.run(["python", "todo_list.py"], input=f"1\n{task}\n{description}\n7\n", text=True)

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    tasks = load_tasks()
    assert any(t["nombre"] == task for t in tasks), f"No se encontró la tarea '{task}'"

@given('the to-do list contains tasks')
def step_impl(context):
    clear_tasks_file()
    for row in context.table:
        descripcion = row['Description'] if 'Description' in row.headings else 'Descripción generada'
        subprocess.run(["python", "todo_list.py"], input=f"1\n{row['Task']}\n{descripcion}\n7\n", text=True)

@when('the user lists all tasks')
def step_impl(context):
    context.result = subprocess.run(["python", "todo_list.py"], input="2\n7\n", capture_output=True, text=True).stdout

@then('the output should contain')
def step_impl(context):
    for line in context.text.strip().splitlines():
        assert line.strip() in context.result, f"'{line.strip()}' no encontrado en la salida."

@given('the to-do list contains a task "{task}" with description "{description}" and status "{status}"')
def step_impl(context, task, description, status):
    clear_tasks_file()
    subprocess.run(["python", "todo_list.py"], input=f"1\n{task}\n{description}\n7\n", text=True)
    if status.lower() == "completada":
        tasks = load_tasks()
        id_tarea = None
        for t in tasks:
            if t["nombre"] == task:
                id_tarea = t["id"]
                break
        assert id_tarea is not None, f"No se encontró la tarea '{task}' para marcarla como completada."
        subprocess.run(["python", "todo_list.py"], input=f"3\n{id_tarea}\n7\n", text=True)

@when('the user marks the task "{task}" as completed')
def step_impl(context, task):
    tasks = load_tasks()
    id_tarea = None
    for t in tasks:
        if t["nombre"] == task:
            id_tarea = t["id"]
            break
    assert id_tarea is not None, f"No se encontró la tarea '{task}' para marcarla como completada."
    subprocess.run(["python", "todo_list.py"], input=f"3\n{id_tarea}\n7\n", text=True)

@then('the task "{task}" should have status "{status}"')
def step_impl(context, task, status):
    tasks = load_tasks()
    for t in tasks:
        if t["nombre"] == task:
            assert t["estado"].lower() == status.lower(), f"Esperado '{status}', pero se obtuvo '{t['estado']}'"
            return
    assert False, f"Tarea '{task}' no encontrada."

@when('the user clears the to-do list')
def step_impl(context):
    subprocess.run(["python", "todo_list.py"], input="4\n7\n", text=True)

@then('the to-do list should be empty')
def step_impl(context):
    tasks = load_tasks()
    assert tasks == [], "La lista de tareas no está vacía."

@when('the user edits the task "{task}" to have description "{description}"')
def step_impl(context, task, description):
    subprocess.run(["python", "todo_list.py"], input=f"5\n{task}\n{description}\n7\n", text=True)

@then('the task "{task}" should have description "{description}"')
def step_impl(context, task, description):
    tasks = load_tasks()
    for t in tasks:
        if t["nombre"] == task:
            assert t["descripcion"] == description, f"Esperado '{description}', pero se obtuvo '{t['descripcion']}'"
            return
    assert False, f"Tarea '{task}' no encontrada."

@when('the user views the task "{task}"')
def step_impl(context, task):
    context.result = subprocess.run(["python", "todo_list.py"], input=f"6\n{task}\n7\n", capture_output=True, text=True).stdout

@then('the output should contain:')
def step_impl(context):
    for line in context.text.strip().splitlines():
        assert line.strip() in context.result, f"'{line.strip()}' no encontrado en la salida."
