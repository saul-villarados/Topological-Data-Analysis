import ripser
import matplotlib.pyplot as plt
import persim
from Config import TDA_CONFIG
from DataLoader import DataLoader
import numpy as np

class TDA:
    def __init__(self):
        self.rips = ripser.Rips(maxdim=TDA_CONFIG.MAX_DIM)
        
    def Persistance(self,A:DataLoader):
        top = self.rips.fit_transform(A.transform[0:50])
        self.diagrams = top
        return self.diagrams
    
    def save_plot(self):
        plt.figure(figsize=(5, 5), dpi=80)
        plt.rcParams.update({'font.size': 10})
        persim.plot_diagrams(self.diagrams, title="Persistence Diagram")

        plt.savefig("img/Persistance_Diagram.png", dpi='figure', format=None, metadata=None,
        bbox_inches=None, pad_inches=0.1,
        facecolor='white', edgecolor='auto')
        
    def wasserstein(self,A:DataLoader):
        ###r = np.divide CLEAN ...
        r = A.transform
        
        wasserstein_dists = np.zeros((TDA_CONFIG.TIME_SEGMENTS,1))
        for i in range(TDA_CONFIG.TIME_SEGMENTS):
            
            tops1 = self.rips.fit_transform(r[i:i+TDA_CONFIG.WINDOWS])
            tops2 = self.rips.fit_transform(r[i+TDA_CONFIG.WINDOWS+1:i+(2*TDA_CONFIG.WINDOWS)+1])
            wasserstein_dists[i] = persim.wasserstein(tops1[0], tops2[0], matching=False)
        return wasserstein_dists
        
    def plot_wasserstein(self,A:DataLoader):
        w = TDA_CONFIG.WINDOWS
        n = TDA_CONFIG.WASSERSTEIN_D #
        wasserstein_dists = self.wasserstein(A)

        plt.figure(figsize=(18, 8), dpi=80)
        plt.rcParams.update({'font.size': 16})

        plt.plot(A.data.index[w:n+w],wasserstein_dists)
        plt.plot(A.data.index[w:n+w],A.data['Close'].dropna(axis='rows').iloc[w:n+w,0]/max(A.data['Close'].dropna(axis='rows').iloc[w:n+w,0]))
       
        plt.plot([A.data.index[TDA_CONFIG.CRASH], A.data.index[TDA_CONFIG.CRASH]], [0, 1], 'r--')
        plt.legend(['Wasserstein distances', 'S&P 500 Normalized', '2020 Crash'])
        plt.xlabel('Date')
        plt.title('TDA-PLOT')

        plt.savefig("img/TDA-PLOT.png", dpi='figure', format=None, metadata=None,
                bbox_inches=None, pad_inches=0.1,
                facecolor='white', edgecolor='auto')