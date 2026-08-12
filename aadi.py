import pandas as pd
import numpy as np
dict={"first score":[100,90,95,np.nan],
      "second score":[30,45,56,np.nan],
      "third score":[np.nan,40,80,98]}
df=pd.DataFrame(dict)
df_filled=df.ffill()
print(df_filled)
