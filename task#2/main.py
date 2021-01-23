#!/usr/bin/python

import csv
import json


USERS_JSON_FILE_PATH = "./files/users.json"
BOOKS_CSV_FILE_PATH = "./files/books-39204-271043.csv"
USERS_WITH_BOOKS_JSON_FILE = "./files/users_with_books.json"


def read_json_file(file_path):
    with open(file_path, "r") as users_file:
        users = json.loads(users_file.read())
    return users


def get_list_from_csv_file(file_path):
    with open(file_path, newline='') as books_file:
        books = csv.DictReader(books_file)
        books = list(books)
    return books


def get_list_users_with_books(users, books):
    list_users_with_books = []
    for i, user in enumerate(users):
        if len(books) > i + 1:
            user_book = books[i]
            new_book = {'title': user_book['Title'], 'Author': user_book['Author'], 'Height': user_book['Height']}
            users_books = [new_book]
        else:
            users_books = []
        new_user = {'name': user['name'], 'gender': user['gender'], 'address': user['address'], 'books': users_books}
        list_users_with_books.append(new_user)
    return list_users_with_books


def get_json_file_users_with_books(file_path, data):
    with open(file_path, "w") as users_with_books:
        users_with_books_data = json.dumps(data, indent=4)
        return users_with_books.write(users_with_books_data)


USERS = read_json_file(USERS_JSON_FILE_PATH)
BOOKS = get_list_from_csv_file(BOOKS_CSV_FILE_PATH)
DATA = get_list_users_with_books(USERS, BOOKS)

get_json_file_users_with_books(USERS_WITH_BOOKS_JSON_FILE, DATA)
