from Presentacion.IMain import IMain
from Persistencia.gestorHDF5 import MYh5py
from Dominio.Control import Control
from Dominio.Mapa import Mapa

if __name__ == '__main__':
    #IMain()
    #Control.loadFicheros()
    
    mapa = Mapa(0,0,'data/LaGomera.hdf5')
    print(mapa.downRight())