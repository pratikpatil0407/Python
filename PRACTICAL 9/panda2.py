import pandas as pd
import numpy as np

ser=pd.Series()
print("Panda Series: ",ser)

data=np.array(["Pratik","Aditya","Prathamesh","Tejas"])
ser=pd.Series(data)

print("Panda Series:\n",ser)