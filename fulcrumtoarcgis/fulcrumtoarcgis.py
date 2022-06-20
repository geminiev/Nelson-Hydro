#overall - to export Fulcrum and publish it as a local file geodatabase as a hosted feature layer to ArcGIS
#eve sankar, june 2022

# BEGIN CODE
# purpose: to export fulcrum to csv
# create workflow with webhook to this code when changed or updated

# imports

import urllib.request as urllib2 #fix for importing urllib2 in python3
import urllib.error
import urllib.parse
import csv, os, arcpy, arcgis
from arcgis.gis import GIS 

def fulcrum_to_csv():

    field_view = 'b711f907a8d42665' #view from fulcrum. varies per app & view setup.

    url = 'https://web.fulcrumapp.com/shares/' + field_view + '.csv'
    u = urllib2.urlopen(url)
    localFile = open('fulcrum_data.csv', 'w')
    localFile.write(u.read())
    localFile.close()

def csv_to_gdb():

    newFile = r"C:\\Users\\fulcrum_data.csv" #change for Tim's computer
    out_gdb = r"C:\Data\\temp.gdb" #ibid
    arcpy.TableToTable_conversion(newFile, out_gdb, 'tempTable')

# probably wobbly. might need to modify for headers

def gdb_to_GIS():
    g = arcgis.gis.GIS("https://www.arcgis.com", "USER", "PASSWORD")

    fgdb =  r"C:\\Data\\temp.gdb" #change for Tim's computer
    serviceProp = {}
    serviceProp['type'] = 'File Geodatabase'
    serviceProp['itemType'] = "file"
    serviceProp['tags'] = "sometag"

    pubProps = {}
    pubProps["hasStaticData"] = 'true'
    pubProps["name"] ="temp"
    pubProps["maxRecordCount"] = 2000 #up for discussion
    pubProps["layerInfo"] = {"capabilities":"Query"}

    fgdb1 = g.content.add(item_properties=serviceProp, data = fgdb)
    fgdb2 = fgdb1.publish(publish_parameters = pubProps, file_type = 'filegeodatabase', overwrite=True)
