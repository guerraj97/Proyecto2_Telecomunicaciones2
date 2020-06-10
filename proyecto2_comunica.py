import numpy as np
#from tabulate import tabulate
import requests
import matplotlib.pyplot as plt
from graphviz import Graph
from graphviz import Digraph
import threading #importando la libreria de multi-hilos

ip = '8.8.8.8'


dot = Graph('AS', format='png', strict = True, size="25.7,8.3!", resolution=100)

temp_mat_as = []

def RIPE(ip):
        url = 'https://stat.ripe.net/data/ris-peerings/data.json?resource={}'.format(ip)
        resp = requests.get(url)
        matriz_as = []
        matriz_final_as = []
        matriz_peers = []
        global temp_mat_as
        #print(len(resp.json()['data']['peerings'][0]['peers'][0]['routes'][0]['as_path']))
        #print(resp.json()['data']['peerings'][k]['peers'][0]['routes'][0]['as_path'])
        
        cantidad_peerings=len(resp.json()['data']['peerings'])
        #print ("hay" ,cantidad,"AS paths")
        print('esta ip tiene: ', cantidad_peerings, ' RRCs')
        #print ("cantidad de peers para este peering: ", cantidad_peers)
        
        for c in range (0,cantidad_peerings):
            cantidad_peers=len(resp.json()['data']['peerings'][c]['peers'])
            for a in range (0,cantidad_peers):
                
                cantidad_routes = len(resp.json()['data']['peerings'][c]['peers'][a]['routes'])
                if cantidad_routes == 0:
                    a = a + 1
                else:
                        cantidad_as = len(resp.json()['data']['peerings'][c]['peers'][a]['routes'][0]['as_path'])
                       # matriz_as.append(',')
                        for i in range(cantidad_as):
                            matriz_as.append(resp.json()['data']['peerings'][c]['peers'][a]['routes'][0]['as_path'][(cantidad_as-1)-i])
             
        primer_valor = matriz_as[0]
        temp_mat_as.append(primer_valor)
        contador_aspath = 1
        cont_control = 0
        list_control = []
        for x in range(0, len(matriz_as)):
            if matriz_as[x]==primer_valor:  
                list_control.append(cont_control)
                matriz_final_as.append(temp_mat_as)
                temp_mat_as = []
                contador_aspath = contador_aspath+1
                print('AS Path: ', contador_aspath)
            temp_mat_as.append(matriz_as[x])    
            print(matriz_as[x])
        return matriz_final_as, list_control, matriz_as
    
matriz, listcont, matriz_real = RIPE(ip)

        
lista = []


for i in range (1, len(matriz)):
    lista = matriz[i]
    for x in range(1,len(lista)):
        dot.edge(str(lista[x-1]), str(lista[x]))
dot.view()





