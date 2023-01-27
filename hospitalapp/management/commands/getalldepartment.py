import djclick as click
import requests
import json
from django.urls import resolve, reverse
from django.http import HttpRequest
import os

@click.command()
def hello():
    # response = requests.get("http://localhost:8000/hospital/department/")
    print(reverse('hospital:get_all_department'))
    url = reverse('hospital:get_all_department')
    print(resolve(url).func)
    print(resolve(url))
    print(os.environ.get('HOSTNAME'))
    # myfunc = resolve(url)
    # mymodule = myfunc.__module__
    # print(mymodule)
    # formatted_response = json.loads(response.text)
    # print(json.dumps(formatted_response, indent=2))

# @click.command()
# def bye():
#     print("HELLO")


