"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    suma_columna = 0
    with open('data.csv','r') as f:
        for line in f:
            line = line.split('\t')
            suma_columna += int(line[1])
    
    return suma_columna


def pregunta_02():
    contador_letras={}
    with open('data.csv','r') as f:
        for line in f:
            line = line.split("\t")
            if line[0] in contador_letras:
                contador_letras[str(line[0])] += 1
            else:
                contador_letras[line[0]] = 1
    lista_contador_letras = sorted(contador_letras.items())

    return lista_contador_letras


def pregunta_03():
    sumador_letras={}
    with open('data.csv','r') as f:
        for line in f:
            line = line.split("\t")
            if line[0] in sumador_letras:
                sumador_letras[str(line[0])] += int(line[1])
            else:
                sumador_letras[line[0]] = int(line[1])
    lista_sumador_letras = sorted(sumador_letras.items())

    return lista_sumador_letras


def pregunta_04():
    from collections import Counter
    contador_meses={}
    with open('data.csv','r') as f:
        for line in f:
            line = str(line).split("\t")
            line2 = str(line[2]).split("-")
            if line2[1] in contador_meses:
                contador_meses[str(line2[1])] += 1
            else:
                contador_meses[str(line2[1])] = 1
    lista_contador_meses = sorted(list(Counter(contador_meses).items()))

    return lista_contador_meses



def pregunta_05():
    max_min_letras = {}
    with open('data.csv','r') as f:
        for line in f:
            line = line.strip().split("\t")
            letra = str(line[0])
            cantidad = int(line[1])
            if letra in max_min_letras:
                max_min_letras[letra][0] = max(max_min_letras[letra][0], cantidad)
                max_min_letras[letra][1] = min(max_min_letras[letra][1], cantidad)
            else:
                max_min_letras[letra] = [cantidad, cantidad]
    lista_max_min_letras = [(str(letra), max_min_letras[letra][0], max_min_letras[letra][1]) for letra in sorted(max_min_letras.keys())]
    
    return lista_max_min_letras


def pregunta_06():
    max_min_dict = {}
    with open('data.csv','r') as f:
        for line in f:
            fields = line.split("\t")
            column = fields[4]
            elements = column.split(',')
            values = [int(element.split(':')[1]) for element in elements]
            key_value_pairs = [tuple(element.split(':')) for element in elements]
            for key, value in key_value_pairs:
                value = int(value)
                if key in max_min_dict:
                    max_val, min_val = max_min_dict[key][0], max_min_dict[key][1]
                    max_min_dict[key] = (max(value, max_val), min(value, min_val))
                else:
                    max_min_dict[key] = (value, value)
    max_min_list = [(k, v[1], v[0]) for k, v in max_min_dict.items()]
    max_min_list.sort()
    
    return max_min_list


def pregunta_07():
    asociaciones = {}
    with open('data.csv', 'r') as f:
        for linea in f:
            columna = linea.split('\t')
            if columna[1] in asociaciones:
                asociaciones[columna[1]].append(columna[0])
            else:
                asociaciones[columna[1]] = [columna[0]]
                lista_asociaciones = [(int(k), v) for k, v in asociaciones.items()]
                lista_asociaciones.sort()
    
    return lista_asociaciones


def pregunta_08():
    asociaciones = {}
    with open('data.csv', 'r') as f:
        for linea in f:
            columna = linea.strip().split('\t')
            if columna[1] in asociaciones:
                asociaciones[columna[1]].append(columna[0])
            else:
                asociaciones[columna[1]] = [columna[0]]
    lista_asociaciones = [(int(k), sorted(set(v))) for k, v in asociaciones.items()]
    
    return sorted(lista_asociaciones)


def pregunta_09():
    count_dict = {}
    with open('data.csv','r') as f:
        for line in f:
            fields = line.split("\t")
            column = fields[4]
            elements = column.split(',')
            key_value_pairs = [tuple(element.split(':')) for element in elements]
            for key, value in key_value_pairs:
                if key in count_dict:
                    count_dict[str(key)] += int(1)
                else:
                    count_dict[str(key)] = int(1)
        
        count_dict_sorted = dict(sorted(count_dict.items()))

    return count_dict_sorted


def pregunta_10():
    result = []
    with open('data.csv', 'r') as f:
        for line in f:
            fields = line.strip().split("\t")
            col1 = fields[0]
            col4 = len(fields[3].split(","))
            col5 = len(fields[4].split(","))
            result.append((col1, col4, col5))
    return result


def pregunta_11():
    with open('data.csv','r') as f:
        sum_dict = {}
        for line in f:
            fields = line.split("\t")
            letter = fields[0]
            value = int(fields[1])
            column = fields[3]
            letters = column.split(",")
            for l in letters:
                if l in sum_dict:
                    sum_dict[l] += value
                else:
                    sum_dict[l] = value
    
    return dict(sorted(sum_dict.items()))


def pregunta_12():
    diccionario = {}
    with open("data.csv", "r") as archivo:
        for linea in archivo:
            fields = linea.split("\t")
            letra = fields[0]
            column = fields[4]
            elements = column.split(',')
            valores = [int(element.split(':')[1]) for element in elements]
            suma = sum(valores)
            if letra not in diccionario:
                diccionario[letra] = 0
            diccionario[letra] += suma
    return dict(sorted(diccionario.items()))
