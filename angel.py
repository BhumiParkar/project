import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import geodatasets  # 1. Imported the modern dataset manager
world = gpd.read_file(geodatasets.get_path('naturalearth.land'))
print(world.head())
world.plot()
plt.title("World Map")
plt.show()
