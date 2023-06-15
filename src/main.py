from os import environ

name = environ.get('INPUT_name', 'aks-update-gha')
print(name)
