import re

def regex(padrao, string):
    get = re.match(padrao, string)
    if bool(get):
        return get.group()
    return False

def verify_adresses(path):
    with open(path, 'r') as archive:
        for line in archive:
            adresses = line.strip()
            if adresses == '0.0.0.0':
                print(adresses + ' Endereço Válido')
            elif regex('^(([1-9]\.|[1-9][0-9]\.|1[0-9][0-9]\.|2[0-4][0-9]\.|25[0-5]\.)([0-9]\.|[1-9][0-9]\.|1[0-9][0-9]\.|2[0-4][0-9]\.|25[0-5]\.)([0-9]\.|[1-9][0-9]\.|1[0-9][0-9]\.|2[0-4][0-9]\.|25[0-5]\.)([0-9]\.|[1-9][0-9]\.|1[0-9][0-9]\.|2[0-4][0-9]\.|25[0-5]\.))$', adresses + '.'):
                print(adresses + ' Endereço Válido')
            else:
                print(adresses + ' Endereço Inválido')

verify_adresses(r'enderecos.txt')