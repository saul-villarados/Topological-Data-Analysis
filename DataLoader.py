import yfinance as yf
import numpy as np

from Config import Data_Config


class DataLoader:
    def __init__(self):
        self.index_names = Data_Config.INDEX_NAMES
        self.start_start_date_string = Data_Config.START_DATE_STRING
        self.end_date_string = Data_Config.END_DATE_STRING
        self.transform = None
        self.data = None

    def Extract(self):
        raw_data = yf.download(self.index_names,start=self.start_start_date_string,end=self.end_date_string)
        self.data = raw_data
        return self.data
    
    def Transform(self):
        ARRAY = self.data['Close'].dropna(axis='rows')
        self.Clean = ARRAY.to_numpy()     
        self.transform = self.Clean  

        ratio = np.log(np.divide(self.Clean[1:],self.Clean[:len(self.Clean)-1]))
        self.transform = ratio
        return self.transform

    def Load(self):
        return self.transform
    


