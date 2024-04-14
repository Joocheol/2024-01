from urllib.request import urlopen
import json

from pprint import pprint

url ="https://jsonplaceholder.typicode.com/todos/1"
with urlopen("https://www.example.com") as response:
    body = response.read()
    #pprint(dir(response))
    pass
pprint(response.headers.items())
pprint(response.getheader("Server"))

#todo_item = json.loads(body)
#print(todo_item)

print(body.decode("utf-8"))
print(response.headers.get_content_charset())