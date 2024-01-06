"""Скрипт для заполнения данными таблиц в БД Postgres."""
# import psycopg2

import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

# получаем пароль к базе данных из файла .env
load_dotenv()
PASSWORD = os.getenv("PASSWORD")

# создаём списки с названиями таблиц и файлов csv.
FILE_LIST = ["employees_data.csv", "customers_data.csv", "orders_data.csv"]
TABLE_LIST = ["employees_data", "customers_data", "orders_data"]

#  создаём строку подключения, содержащую учетные данные нашей базы данных.
engine = create_engine(f"postgresql+psycopg2://postgres:{PASSWORD}@localhost/north")

# Получение пути к текущему исполняемому файлу
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = current_dir[: -(len(current_dir.split("\\")[-1]) + 1)]

# запускаем цикл для заполнения таблиц данными из csv файлов поочерёдно
for path_name, table_name in zip(FILE_LIST, TABLE_LIST):
    # Создание относительного пути к файлу от текущего файла
    file_path = os.path.join(base_dir, "homework-1", "north_data", path_name)

    # создаём ДатаФрейм пандас из csv файла
    df = pd.read_csv(file_path)

    # экспортируем ДатаФрейм с данными в таблицу базы данных.
    df.to_sql(table_name, engine, if_exists="append", index=False)
