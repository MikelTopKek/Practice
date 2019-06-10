import requests


if __name__ == '__main__':
    r = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    print(r.json())
