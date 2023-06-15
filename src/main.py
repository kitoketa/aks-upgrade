#!/usr/bin/env python

from os import environ

def main():
    name = environ.get('INPUT_NAME', 'aks-update-gha')
    print(name)


if __name__ == '__main__':
    main()
