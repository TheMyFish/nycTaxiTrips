import json
import pandas as pd

with open('C:\Code\processoSeletivo\dataSprints\data\dataTest2009.json') as f_input:
    df = pd.read_json(f_input)
df.to_csv('C:\Code\processoSeletivo\dataSprints\data\dataTest2009.csv')
