import geopandas as gpd
import matplotlib.pyplot as plt
import geodatasets
import numpy as np
world = gpd.read_file("https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip")
fig, ax = plt.subplots()
world.plot(ax=ax, color="BLUE", edgecolor="white")
world[world["CONTINENT"] == "Asia"].plot(ax=ax, color="red", edgecolor="white")
plt.title("Asia Highlighted")
plt.show()
