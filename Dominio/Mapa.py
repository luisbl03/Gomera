from Persistencia.gestorHDF5 import MYh5py
import numpy as np

#Clase Mapa para almacenar los datos de cada mapa
class Mapa:
    def __init__(self, noDataValue, sizeCell, filename):
        self.noDataValue = noDataValue  # Float. Valor para datos faltantes
        self.sizeCell = sizeCell  # Float. Tamaño en metros de un lado de la celda.
        self.filename = filename  # Filename del mapa
        self.hdf5 = MYh5py(filename)
    
    
    def downRight(self):
        
        maxX = 0
        minY = 0
        
        datasets = self.hdf5.readDatasets()
        
        for dataset in datasets:
            x = self.hdf5.readAtributos(dataset,'xsup')
            y = self.hdf5.readAtributos(dataset,'yinf')
            if maxX == 0 and minY == 0:
                maxX = x
                minY = y
            else:
                if x > maxX:
                    maxX = x
                if y < minY:
                    minY = y
        return (maxX,minY)
        
        
        
        
        
    
