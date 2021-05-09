import sqlite3

def update_employee_title(cursor, title, id):

    update_sql ='''
        UPDATE employees
        SET title = ?
        WHERE employeeid = ? '''

    cursor.execute(update_sql, (title, id))

def fetch_employee(cursor, id):

    fetch_sql =''' SELECT * FROM employees WHERE employeeid = ? '''

    cursor.execute(fetch_sql, (id,))

    return cursor.fetchall()


def main():
    database = r"./chinook.db" #sample db

    # create a database connection

    with sqlite3.connect(database) as conn:

        c = conn.cursor()
        
        empID = 4

        print('Employee with ID ' + str(empID) + ':\n')
        print (fetch_employee(c, empID))

        update_employee_title(c, 'Sales Manager', empID)

        print('Employee with ID ' + str(empID) + ', after update:')
        print (fetch_employee(c, empID))






if __name__ == '__main__':
    main()