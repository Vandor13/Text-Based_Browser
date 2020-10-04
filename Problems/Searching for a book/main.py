import requests


def do_search(bookstore_url, params):
    response = requests.get(bookstore_url, params)
    return response
