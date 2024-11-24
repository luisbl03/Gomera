from Persistencia.gestorHDF5 import MYh5py
import numpy as np
import h5py

class Control:
    
    #cargamos los ficheros asc dentro del hdf5
    def loadFicheros():
        archivo = MYh5py('data/mapa.hdf5')
        archivo.create_file()
        
        #creamos los grupos correspondientes dentro del hdf5
        archivo.create_group('arriba') #mapa 1-2
        archivo.create_group('abajo izquierda') #mapa 1
        archivo.create_group('abajo derecha') #mapa 2
        archivo.create_group('medio izquierda') #mapa 3
        archivo.create_group('medio derecha') #mapa 4
        
        #
        #leemos los ficheros asc (borro skiprows=6)
        #arriba_asc = np.loadtxt('Data/MDT02-REGCAN95-HU28-1095-1-2-COB2.asc') #leemos mapa de arriba
        #abajo_izquierda_asc = np.loadtxt('Data/MDT02-REGCAN95-HU28-1101-1-COB2.asc') #leemos mapa de abajo izquierda
        #abajo_derecha_asc = np.loadtxt('Data/MDT02-REGCAN95-HU28-1101-2-COB2.asc') #leemos mapa de abajo derecha
        #medio_izquierda_asc= np.loadtxt('Data/MDT02-REGCAN95-HU28-1095-3-COB2.asc') #leemos mapa de medio izquierda
        #medio_derecha_asc = np.loadtxt('Data/MDT02-REGCAN95-HU28-1095-4-COB2.asc') #leemos mapa de medio derecha
        
        ficheros = ['data/MDT02-REGCAN95-HU28-1095-1-2-COB2.asc','data/MDT02-REGCAN95-HU28-1101-1-COB2.asc','data/MDT02-REGCAN95-HU28-1101-2-COB2.asc',
                    'data/MDT02-REGCAN95-HU28-1095-3-COB2.asc','data/MDT02-REGCAN95-HU28-1095-4-COB2.asc']
        informacion_ficheros = []
        datos_fichero = []
        informacion_numeros = []
        contador = 0
        for nombre_fichero in ficheros:
            with open(nombre_fichero, 'r') as f: 
                while contador < 6:
                    linea = f.readline()
                    datos_fichero.append(linea.rstrip())
                    contador += 1  
                informacion_ficheros.append(datos_fichero)
                texto_restante = f.read()
                informacion_numeros.append(texto_restante)

        #insertamos los datasets dentro del hdf5

        archivo.create_dataset_grupo('arriba','Rectangulo',informacion_numeros[0])
        archivo.create_dataset_grupo('abajo izquierda','Rectangulo',informacion_numeros[1])
        archivo.create_dataset_grupo('abajo derecha','Rectangulo',informacion_numeros[2])   
        archivo.create_dataset_grupo('medio izquierda','Rectangulo',informacion_numeros[3])
        archivo.create_dataset_grupo('medio derecha','Rectangulo',  informacion_numeros[4])

        for i in range(informacion_ficheros.__len__()):
            nombre_grupo = archivo.split('/')[-1].split('.')[0]
            print(nombre_grupo)
            for j in range(datos_fichero.__len__()):
                info=informacion_ficheros[i][j].split()[0] 
                if 'arriba' in archivo:
                    grupo = archivo['arriba']
                    nombre_grupo = grupo.name
                    nombre_grupo.attrs[info] = int(informacion_ficheros[i][j].split()[1])
                elif 'abajo izquierda' in archivo:
                    grupo = archivo['abajo izquierda']
                    nombre_grupo = grupo.name
                    nombre_grupo.attrs[info] = int(informacion_ficheros[i][j].split()[1])                
                elif 'abajo derecha' in archivo: 
                    grupo = archivo['abajo derecha']
                    nombre_grupo = grupo.name
                    nombre_grupo.attrs[info] = int(informacion_ficheros[i][j].split()[1])
                elif 'medio izquierda' in archivo:
                    grupo = archivo['medio izquierda']
                    nombre_grupo = grupo.name
                    nombre_grupo.attrs[info] = int(informacion_ficheros[i][j].split()[1])   
                elif 'medio derecha' in archivo:
                    grupo = archivo['medio derecha']
                    nombre_grupo = grupo.name
                    nombre_grupo.attrs[info] = int(informacion_ficheros[i][j].split()[1])
        print("HECHO")

    #Método que devuelve el par de coordenadas Y-UMT y X-UMT de la esquina superior izquierda del mapa.
    def downRight(filename):
        
        maxX = 0
        minY = 0
        
        file = MYh5py(filename)
        datasets = file.readDatasets()
        
        for dataset in datasets:
            x = file.readAtributos(dataset,'xsup')
            y = file.readAtributos(dataset,'yinf')
            if maxX == 0 and minY == 0:
                maxX = x
                minY = y
            else:
                if x > maxX:
                    maxX = x
                if y < minY:
                    minY = y
        return (maxX,minY)