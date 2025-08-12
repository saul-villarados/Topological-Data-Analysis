import ripser

class Data_Config:
    INDEX_NAMES = ['^GSPC', '^DJI', '^IXIC', '^RUT']
    START_DATE_STRING = "2018-01-01"
    END_DATE_STRING = "2022-04-21"

class TDA_CONFIG:
    MAX_DIM = 2
    WINDOWS = 20
    TIME_SEGMENTS = 1041
    WASSERSTEIN_D = 1041
    RIPS = ripser.Rips(maxdim=2)    
    CRASH = 536