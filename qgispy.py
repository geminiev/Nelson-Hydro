# Hello friends :) This is my repo for commands and explanations of what you can do in QGIS with Python. My estimate is it's probably pretty similar 
# to ArcGIS when you transition over - just maybe different commands. 
###################
# Add a layer
###################
uri = "E:/Geodata/NaturalEarth/vector_v4/natural_earth_vector.gpkg_v4.1.0/packages/natural_earth_vector.gpkg|layername=ne_10m_admin_0_countries"
# ^ give link to what you want to insert a name
iface.addVectorLayer(uri, "name to give new layer", "source (from layer properties)")
# ^iface.addVectorLayer is the function.
