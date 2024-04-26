import os
from pymysql import Connection, connect
from pymysql.cursors import DictCursor
from dotenv import load_dotenv


def get_mysql_connection(isLegacy: bool) -> Connection:
    load_dotenv()

    if isLegacy:
        return _get_legacy_connection()

    return _get_connection()


def _get_legacy_connection() -> Connection:
    return connect(
        host=os.getenv('LEGAGY_DB_HOST'),
        port=int(os.getenv('LEGAGY_DB_PORT') or 0),
        user=os.getenv('LEGAGY_DB_USER'),
        password=os.getenv('LEGAGY_DB_PASSWORD') or '',
        db=os.getenv('LEGAGY_DB_NAME'),
        charset='utf8mb4',
        cursorclass=DictCursor
    )

def _get_connection() -> Connection:
    return connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT') or 0),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD') or '',
        db=os.getenv('DB_NAME'),
        charset='utf8mb4',
        cursorclass=DictCursor
    )
