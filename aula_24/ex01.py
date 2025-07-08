from datetime import datetime
import polars as pl

ENEDERECO_DAD0S = r'../../dados/'

try
    print('obtendo os dados...')
    inicio = datetime.now()
    
except Exception as e:
    print (f'Erro ao obter os dados')