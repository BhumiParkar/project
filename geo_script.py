Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
===================== RESTART: C:/Users/admin/geopandas.py =====================
Traceback (most recent call last):
  File "C:/Users/admin/geopandas.py", line 2, in <module>
    import geopandas as gpd
  File "C:\Users/admin\geopandas.py", line 5, in <module>
    world= gpd.read-file.datasets.gpd("https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip")
AttributeError: partially initialized module 'geopandas' from 'C:\Users/admin\geopandas.py' has no attribute 'read' (most likely due to a circular import)
>>> 
===================== RESTART: C:/Users/admin/geopandas.py =====================
Traceback (most recent call last):
  File "C:/Users/admin/geopandas.py", line 8, in <module>
    import geopandas as gpd
  File "C:\Users/admin\geopandas.py", line 13, in <module>
    world = gpd.read_file(url)
AttributeError: partially initialized module 'geopandas' from 'C:\Users/admin\geopandas.py' has no attribute 'read_file' (most likely due to a circular import)
