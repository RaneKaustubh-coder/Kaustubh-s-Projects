import mysql.connector


db_pass = '*************' 
db_name = 'To_Do_List'


def connection_to_mysql():
    
    try:
        connect = mysql.connector.connect(
            host='localhost',
            user='root',
            password=db_pass,
            database=db_name
        )
        print('Successfully Connected to MySQL!!')
        return connect
    except mysql.connector.Error as err:
        print(f'Error connecting to MySQL: {err}')
        return None



def add_task(cursor, conn):
    
    print("\n--- Add New Task ---")
    try:
        task_description = input('Enter task description: ')
        sql_query = "INSERT INTO tasks (description, completed) VALUES (%s, %s)"
        values = (task_description, 0) 
        cursor.execute(sql_query, values)
        conn.commit() 
        print('Task added successfully!')
    except mysql.connector.Error as err:
        print(f'Error adding task: {err}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

def view_tasks(cursor):
    
    print("\n--- Your To-Do List ---")
    try:
        sql_select_query = "SELECT id, description, completed FROM tasks" 
        cursor.execute(sql_select_query)
        tasks = cursor.fetchall()

        if tasks:
            for task in tasks:
                task_id = task[0]         
                description = task[1]     
                completed = task[2]      
                status = "[X]" if completed else "[ ]" 
                print(f'{task_id}. {status} {description}')
        else:
            print('No tasks found in your To-Do List.')
        print('--------------------------------------\n')
    except mysql.connector.Error as err:
        print(f'Error viewing tasks: {err}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

def update_task(cursor, conn):
   
    print('\n--- Update Task ---')
    try:
        task_id_to_update = int(input('Enter the ID of the Task to Update: '))
        new_status_input = input('Mark as (d) Completed or (n) Incomplete? Enter d or n: ').lower()

        new_status_value = None
        if new_status_input == 'd':
            new_status_value = 1
        elif new_status_input == 'n':
            new_status_value = 0
        else:
            print("Invalid status. Please enter 'd' for completed or 'n' for incomplete.")
            return

        if new_status_value is not None:
            sql_update_query = "UPDATE tasks SET completed = %s WHERE id = %s"
            data_to_update = (new_status_value, task_id_to_update)
            cursor.execute(sql_update_query, data_to_update) 
            conn.commit()

            if cursor.rowcount > 0:
                print(f'Task ID {task_id_to_update} updated successfully!')
            else:
                print(f'No task found with ID {task_id_to_update}.')

    except ValueError:
        print("Invalid input. Please enter a number for the task ID.")
    except mysql.connector.Error as err:
        print(f'Error updating task: {err}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

def delete_task(cursor, conn):
    
    print('\n--- Delete Task ---')
    try:
        task_id_to_delete = int(input('Enter the ID of the task to delete: '))

        sql_delete_query = "DELETE FROM tasks WHERE id = %s" 
        data_to_delete = (task_id_to_delete,)

        cursor.execute(sql_delete_query, data_to_delete) 
        conn.commit()

        if cursor.rowcount > 0:
            print(f'Task ID {task_id_to_delete} deleted successfully!')
        else:
            print(f'No task found with ID {task_id_to_delete}.')

    except ValueError:
        print("Invalid input. Please enter a number for the task ID.")
    except mysql.connector.Error as err:
        print(f'Error deleting task: {err}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')


conn = None    
cursor = None 

try:
    conn = connection_to_mysql() 

    if conn: 
        cursor = conn.cursor()
        print("Welcome to your To-Do List Application!")

        while True: 
            print("\n--- Menu ---")
            print("1. Add New Task")
            print("2. View All Tasks")
            print("3. Update Task Status")
            print("4. Delete Task")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                add_task(cursor, conn)
            elif choice == '2':
                view_tasks(cursor)
            elif choice == '3':
                update_task(cursor, conn)
            elif choice == '4':
                delete_task(cursor, conn)
            elif choice == '5':
                print("Exiting To-Do List Application. Goodbye!")
                break 
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

except mysql.connector.Error as err:
    print(f"Database connection error: {err}")
except Exception as e: 
    print(f"An unexpected error occurred: {e}")
finally:
    
    if 'cursor' in locals() and cursor: 
        cursor.close()
    if conn and conn.is_connected(): 
        conn.close()
        print("MySQL connection closed.")