from flask import Flask, request
import requests, json
from fulcrum.exceptions import NotFoundException
from area_find import area_find
from grid_find import grid_find
from veg_area_find import veg_area_find

from time import sleep

app = Flask(__name__)

#Main url message testing
@app.route('/')
def api_root():
    return 'Welcome guys'

@app.route('/webhooks', methods=['POST'])
def api_ful():
        #Server friendliness
        sleep(3)
        if request.is_json:
            try:
                #Parse the Json into a Python dictionary
                my_info = request.get_json()


                #print (my_info.headers)
                #Print the imported data record id and T&T Value
                #print(my_info['data'])
                #print(my_info['data']['form_values']['lat_test'])

                #evtest

                # If record being sent was created...
                if my_info['type'] == "record.create":
                    #Print Latitude and Longitude Values
                    print("Lat and Lon are: ", my_info['data']['latitude'], my_info['data']['longitude']) #evdits

#issue - latitude and longitude are empty to this script. how did he pass it over before???

                    #Assign lat, lon, and id values
                    lat = my_info['data']['latitude']
                    lon = my_info['data']['longitude']
                    record_id = my_info['data']['id']
                    form_id = my_info['data']['form_id']

                    url = "https://api.fulcrumapp.com/api/v2/records/" + record_id + ".json"

                    #Use lat and lon values in area function
                    area = area_find(lat, lon)
                    grid = grid_find(lon, lat)
                    veg_area = veg_area_find(lon, lat)

                    #Fulcrum Key
                    api_token = 'e94521d89112b27b780441c02f6c3f1d2775e4c3075ed0c6aa8e0ab2c3916d129a30931a218ae75e'

                    #Update Record

                    #Update Veg Management Area Location
                    if '087a' in my_info['data']['form_values']:
                        my_info['data']['form_values']['087a'] = veg_area
                        print(my_info['data']['form_values']['087a'])

                    else:
                        print("Unknown veg area variable")

                    #Find area variable location depending on app
                    #Veg Tracking
                    if '33da' in my_info['data']['form_values']:
                        my_info['data']['form_values']['33da'] = area
                        print(my_info['data']['form_values']['33da'])

                    elif '419b' in my_info['data']['form_values']:
                        my_info['data']['form_values']['419b'] = area
                        print(my_info['data']['form_values']['419b'])

                    elif 'a03a' in my_info['data']['form_values']:
                        my_info['data']['form_values']['a03a'] = area
                        print(my_info['data']['form_values']['a03a'])

                    #Add more area locations as shown above here to add more apps in

                    else:
                        print("Unknown area variable")
                        #return "Unknown area variable", 400

                    #Find grid variable location dpending on app
                    if '3d8' in my_info['data']['form_values']:
                        my_info['data']['form_values']['a3d8'] = grid
                        print(my_info['data']['form_values']['a3d8'])

                    #Veg Tracking
                    elif '7453' in my_info['data']['form_values']:
                        my_info['data']['form_values']['7453'] = grid
                        print(my_info['data']['form_values']['7453'])

                    elif 'ba94' in my_info['data']['form_values']:
                        my_info['data']['form_values']['ba94'] = grid
                        print(my_info['data']['form_values']['ba94'])

                    elif 'b16a' in my_info['data']['form_values']:
                        my_info['data']['form_values']['b16a'] = grid
                        print(my_info['data']['form_values']['b16a'])

                    #Add more area locations as shown above here to add more apps in

                    else:
                        print("Unknown grid variable")
                        return "Unknown grid variable", 200

                    form_values = my_info['data']['form_values']
                    print("Form Values: ", form_values)
                    unloaded_values = json.dumps(form_values, separators=(',', ':'))
                    print("Unloaded Values: ", unloaded_values)
                    updated_values = json.loads(unloaded_values)
                    print("Updated Values: ", updated_values)

                    updated_record = {"record": {record_id: form_id, "form_values": updated_values}}
                    print("Updated Record: ", updated_record)
                    payload = updated_record

                    headers = {
                        "Accept": "application/json",
                        'Content-Type': 'application/json',
                        'X-ApiToken': api_token
                    }
                    response = requests.request("PUT", url, json=payload, headers=headers)

                    #Debug
                    print("T&T area is: ", area)
                    print(response.json())
                    print(response.text)
                    print(response.status_code)
                    print(response.reason)
                    print('Record successfully updated!')

                    return "Json received!", 200

                #If record being sent was updated... this will create an ifinite loop, only use with the test webhook function
                elif my_info['type'] == "record.update":
                    # #Print Latitude and Longitude Values
                    # print("Lat and Lon are: ", my_info['data']['created_location']['latitude'], my_info['data']['created_location']['longitude'])

                    # #Assign lat, lon, and id values
                    # lat = my_info['data']['created_location']['latitude']
                    # lon = my_info['data']['created_location']['longitude']
                    # record_id = my_info['data']['id']
                    # form_id = my_info['data']['form_id']

                    # url = "https://api.fulcrumapp.com/api/v2/records/" + record_id + ".json"

                    # #Use lat and lon values in area function
                    # area = area_find(lat, lon)
                    # grid = grid_find(lon, lat)

                    # #Fulcrum Key
                    # api_token = 'e94521d89112b27b780441c02f6c3f1d2775e4c3075ed0c6aa8e0ab2c3916d129a30931a218ae75e'

                    # #Update Record

                    # #Find area variable location depending on app
                    # if '33da' in my_info['data']['form_values']:
                    #     my_info['data']['form_values']['33da'] = area
                    #     print(my_info['data']['form_values']['33da'])

                    # elif '419b' in my_info['data']['form_values']:
                    #     my_info['data']['form_values']['419b'] = area
                    #     print(my_info['data']['form_values']['419b'])

                    # elif 'a03a' in my_info['data']['form_values']:
                    #     my_info['data']['form_values']['a03a'] = area
                    #     print(my_info['data']['form_values']['a03a'])

                    # #Add more area locations as shown above here to add more apps in

                    # else:
                    #     print("Unknown area variable")
                    #     #return "Unknown area variable", 400

                    # #Find grid variable location dpending on app
                    # if '3d8' in my_info['data']['form_values']:
                    #     my_info['data']['form_values']['a3d8'] = grid
                    #     print(my_info['data']['form_values']['a3d8'])

                    # elif '7453' in my_info['data']['form_values']:
                    #     my_info['data']['form_values']['7453'] = grid
                    #     print(my_info['data']['form_values']['7453'])

                    # elif 'ba94' in my_info['data']['form_values']:
                    #     my_info['data']['form_values']['ba94'] = grid
                    #     print(my_info['data']['form_values']['ba94'])

                    # elif 'b16a' in my_info['data']['form_values']:
                    #     my_info['data']['form_values']['b16a'] = grid
                    #     print(my_info['data']['form_values']['b16a'])

                    # #Add more area locations as shown above here to add more apps in

                    # else:
                    #     print("Unknown grid variable")
                    #     return "Unknown grid variable", 200

                    # form_values = my_info['data']['form_values']
                    # print("Form Values: ", form_values)
                    # unloaded_values = json.dumps(form_values, separators=(',', ':'))
                    # print("Unloaded Values: ", unloaded_values)
                    # updated_values = json.loads(unloaded_values)
                    # print("Updated Values: ", updated_values)

                    # updated_record = {"record": {record_id: form_id, "form_values": updated_values}}
                    # print("Updated Record: ", updated_record)
                    # payload = updated_record

                    # headers = {
                    #     "Accept": "application/json",
                    #     'Content-Type': 'application/json',
                    #     'X-ApiToken': api_token
                    # }
                    # response = requests.request("PUT", url, json=payload, headers=headers)

                    # #Debug
                    # print("T&T area is: ", area)
                    # print(response.json())
                    # print(response.text)
                    # print(response.status_code)
                    # print(response.reason)
                    # print('Record successfully updated!')

                    return "Json received!", 200

                #Non-normal record type handling
                else:
                    #Return a string along with an HTTP status code
                    return "Json received!", 200

            #Record not found exception handling
            except NotFoundException:
                print('Not found error')
                return "Unknown Error", 400

        #Intital payload was not json handling
        else:
            #Request was not Json so return an error HTTP status code
            return "Request was not Json", 400
