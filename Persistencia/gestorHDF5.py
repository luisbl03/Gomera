from h5py import *

class MYh5py:
    
    #constructor de la clase
    def __init__(self,filename):
        self.filename =filename #contructor de la clase
    
    #crar un archivo
    def create_file(self):
        self.file = File(self.filename,'w')
        self.file.close()
        
    #metodo para crear un grupo
    def create_group(self,groupname):
        self.file = File(self.filename,'a')
        self.file.create_group(groupname)
        self.file.close()
    
    #metodo para crear un dataset
    def create_dataset_grupo(self,groupname,datasetname,data):
        self.file = File(self.filename,'a')
        self.file[groupname].create_dataset(datasetname,data=data)
        self.file.close()
    
    def create_dataset_raiz(self,datasetname,data):
        self.file = File(self.filename,'a')
        self.file.create_dataset(datasetname,data=data)
        self.file.close()
        
    #metodo para leer un dataset desde el directorio raiz
    def readDataset_raiz(self,datasetName):
        with File(self.filename,'r') as f:
            data = f[datasetName][:]
        f.close()
        return data
    
    #metodo para leer un dataset desde un grupo
    def readDataset_grupo(self,groupname,datsetname):
        with File(self.filename,'r') as f:
            group = f[groupname]
            data = group[datsetname][:]
        f.close()
        return data

    #metodo para leer los atributos
    def readAtributos(self,datasetName,atributoName):
        with File(self.filename,'r') as f:
            data = f[datasetName].attrs
            atributo = data[atributoName]
        f.close()
        return atributo

    #metodo que devuelve los datsets de un fichero
    def readDatasets(self):
        with File(self.filename,'r') as f:
            data = list(f.keys())
            datasets = [key for key in data if isinstance(f[key],Dataset)]
        f.close()
        return datasets
    
    