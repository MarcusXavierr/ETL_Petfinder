from create_connection import get_mysql_connection

categoryAges = [
    {'age':"Filhote", 'wp_term_id': 11},
    {'age':"Adulto", 'wp_term_id': 12},
    {'age':"Sênior", 'wp_term_id': 13}
]

physicalSizes = [
    {'size':"Pequeno Porte", 'wp_term_id': 8},
    {'size':"Médio Porte", 'wp_term_id': 9},
    {'size':"Grande Porte", 'wp_term_id': 10}
]

def seed_data():
    connection = get_mysql_connection(False)
    print('entrei')

    with connection.cursor() as cursor:
        for categoryAge in categoryAges:
            print(f'inserindo {categoryAge["age"]}')
            cursor.execute("INSERT INTO category_ages (category, wp_term_id) VALUES (%s, %s)", (categoryAge['age'], categoryAge['wp_term_id']))
        connection.commit()

    with connection.cursor() as cursor:
        for physicalSize in physicalSizes:
            print(f'inserindo {physicalSize["size"]}')
            cursor.execute("INSERT INTO physical_sizes (size, wp_term_id) VALUES (%s, %s)", (physicalSize['size'], physicalSize['wp_term_id']))
        connection.commit()

    connection.close()

seed_data()
