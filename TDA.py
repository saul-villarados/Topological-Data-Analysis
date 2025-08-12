from DataLoader import DataLoader
from TDA_Config import TDA

DATA = DataLoader()
TOP = TDA()

def Data(Data=DATA):
    DATA.Extract()
    DATA.Transform()
    DATA.Load()

def Pers(Top = TOP ):
    TOP.Persistance(DATA)
    TOP.save_plot()
    TOP.wasserstein(DATA)
    TOP.plot_wasserstein(DATA)

if __name__ == '__main__':
    Data()
    Pers()