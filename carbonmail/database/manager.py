# Onde estarão todas as funções deste pacote
# Ele é quem vai cooderndar este pacote (gerenciador)

# SELECT contact.name, contact.email FROM contact
# SELECT list.name FROM list
# INSERT INTO contact (name, email, list_id) VALUES ('Pedro', 'pedro@gmail.com', 1)
# INSERT INTO list (name) VALUES ('Administradores')
# DELETE FROM list WHERE list.id = 2
# DELETE FROM list WHERE list.name = 'Alunos'
# SELECT contact.name, contact.email FROM contact, list WHERE contact.list_id = list.id AND list.name = 'Administradores'
from carbonmail.database.connector import connect, close_connection
from carbonmail.database.operations import insert, select, delete


def create_list(list_name):
    connection = connect()

    sql = f"INSERT INTO list (name) VALUES('{list_name}');"
    insert(connection, sql)

    close_connection(connection)

def create_contact(name, email, list_id):
    connection = connect()

    sql = f"INSERT INTO contact (name, email, list_id) \
            VALUES ('{name}', '{email}', '{list_id}');"
    insert(connection, sql)

    close_connection(connection)

def delete_list(list_name):
    connection = connect()

    sql = f"DELETE FROM list WHERE list.name = '{list_name}';"
    insert(connection, sql)

    close_connection(connection)

def search_list():
    connection = connect()

    sql = 'SELECT * FROM list'
    lists = select(connection, sql)

    if not lists:
        create_list('Padrão')
        lists = [(1, 'Padrão')]

    close_connection(connection)

    return lists

def search_contacts(list_name):
    connection = connect()

    sql = f"SELECT contact.name, contact.email from contact, list \
        WHERE contact.list_id = list.id and list.name = '{list_name}';"
    contacts = select(connection, sql)

    close_connection(connection)

    return contacts



    

