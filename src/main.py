from os import environ

name = environ.get('INPUT_NAME', 'aks-update-gha')
print(name)
