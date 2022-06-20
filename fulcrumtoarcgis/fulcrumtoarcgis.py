# purpose: to export fulcrum to csv
# create workflow with webhook to this code when changed or updated

import urllib2
url = 'https://web.fulcrumapp.com/shares/b711f907a8d42665.csv' #that string of characters is the 'view' from Fulcrum. Varies per app. 
u = urllib2.urlopen(url)
localFile = open('fulcrum_data.csv', 'w')
localFile.write(u.read())
localFile.close()

# purpose: to automate import of csv to arcgis