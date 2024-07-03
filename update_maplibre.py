import os
import shutil
import leafmap.maplibregl as leafmap

url = "https://github.com/giswqs/leafmap/archive/refs/heads/master.zip"
out_zip = "leafmap-master.zip"
leafmap.download_file(url, out_zip)

in_dir = "leafmap-master/docs/maplibre"
out_dir = "maplibre"

leafmap.execute_maplibre_notebook_dir(in_dir, out_dir, replace_api_key=True)

shutil.rmtree("leafmap-master")
os.remove("leafmap-master.zip")
