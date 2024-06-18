# seed.py
import json
from models import User, Task

# Create some users
users = [
    {"username": "user1", "email": "user1@example.com"},
    {"username": "user2", "email": "user2@example.com"},
    {"username": "user3", "email": "user3@example.com"},
]

for user_data in users:
    user = User(**user_data)
    user.save()

# Create some tasks
tasks = [
    {"title": "Task 1", "description": "This is task 1", "user_id": 1, "completed": False},
    {"title": "Task 2", "description": "This is task 2", "user_id": 1, "completed": False},
    {"title": "Task 3", "description": "This is task 3", "user_id": 2, "completed": False},
    {"title": "Task 4", "description": "This is task 4", "user_id": 3, "completed": False},
]

for task_data in tasks:
    task = Task(**task_data)
    task.save()

print("Database seeded successfully!")