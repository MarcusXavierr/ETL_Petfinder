import os
import pymysql.cursors
from dotenv import load_dotenv

load_dotenv()

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
    connection = pymysql.connect(host=os.getenv('DB_HOST'),
                                 port=int(os.getenv('DB_PORT') or 0),
                                 user=os.getenv('DB_USER'),
                                 password=os.getenv('DB_PASSWORD') or '',
                                 db=os.getenv('DB_NAME'),
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        for categoryAge in categoryAges:
            print(f'inserindo {categoryAge["age"]}')
            cursor.execute("INSERT INTO category_ages (age, wp_term_id) VALUES (%s, %s)", (categoryAge['age'], categoryAge['wp_term_id']))
        connection.commit()

    with connection.cursor() as cursor:
        for physicalSize in physicalSizes:
            print(f'inserindo {physicalSize["size"]}')
            cursor.execute("INSERT INTO physical_sizes (size, wp_term_id) VALUES (%s, %s)", (physicalSize['size'], physicalSize['wp_term_id']))
        connection.commit()

    connection.close()
