import sys
import os
import click
from sqlalchemy.orm import sessionmaker
#from models.base import engine, Base
#from models.user import User
#from models.task import Task

# Ensure the models directory is in the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Create the database tables
#Base.metadata.create_all(engine)

# Set up the session
#Session = sessionmaker(bind=engine)
#session = Session()

@click.group()
def cli():
    """Simple CLI for managing a to-do list."""
    pass

@click.command()
@click.option('--name', prompt='User name', help='The name of the user.')
def create_user(name):
    """Create a new user."""
    #user = User(name=name)
   # session.add(user)
   # session.commit()
    click.echo(f'User {name} created.')

@click.command()
def list_users():
    """List all users."""
    #users = session.query(User).all()
   # for user in users:
       # click.echo(f'{user.id}: {user.name}')

@click.command()
@click.option('--description', prompt='Task description', help='The description of the task.')
@click.option('--user_id', prompt='User ID', type=int, help='The ID of the user the task belongs to.')
def create_task(description, user_id):
    """Create a new task for a user."""
    #user = session.query(User).get(user_id)
    #if not user:
        #click.echo(f'User with ID {user_id} does not exist.')
        #return
    #task = Task(description=description, user_id=user_id)
    #session.add(task)
    #session.commit()
    #click.echo(f'Task "{description}" created for user {user.name}.')

@click.command()
def list_tasks():
    """List all tasks."""
    #tasks = session.query(Task).all()
    #for task in tasks:
       # status = 'Completed' if task.completed else 'Not completed'
       # click.echo(f'{task.id}: {task.description} (User: {task.user.name}, Status: {status})')

@click.command()
@click.option('--task_id', prompt='Task ID', type=int, help='The ID of the task to complete.')
def complete_task(task_id):
    """Mark a task as complete."""
    #task = session.query(Task).get(task_id)
   # if not task:
        #click.echo(f'Task with ID {task_id} does not exist.')
        #return
    # task.completed = True
    # session.commit()
    # click.echo(f'Task "{task.description}" marked as complete.')

@click.command()
@click.option('--task_id', prompt='Task ID', type=int, help='The ID of the task to delete.')
def delete_task(task_id):
    """Delete a task."""
    # task = session.query(Task).get(task_id)
    # if not task:
    #     click.echo(f'Task with ID {task_id} does not exist.')
    #     return
    # session.delete(task)
    # session.commit()
    # click.echo(f'Task "{task.description}" deleted.')

# Add commands to the CLI group
cli.add_command(create_user)
cli.add_command(list_users)
cli.add_command(create_task)
cli.add_command(list_tasks)
cli.add_command(complete_task)
cli.add_command(delete_task)

if __name__ == '__main__':
    cli()