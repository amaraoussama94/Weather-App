from tkinter import *
from PIL import ImageTk,Image
import json # decode data
import requests #for 3rd party api



root = Tk()
root.title("W_A")
root.iconbitmap('Coffee.ico')
root.geometry("400x90")


#https://docs.airnowapi.org/CurrentObservationsByZip/query
def ZipLookup():
    print(zip.get())
    try :
   

        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode= "+zip.get()+"&distance=5&API_KEY=7C6C2FB8-961A-4B39-8BAF-566E20BD8324")
        #print("ok")
        api_data =json.loads(api_request.content)
        #print(api_data)
        category = api_data[0]["AQI"]
        city= api_data[0]["ReportingArea"]
        quality = api_data[0]["Category"]["Name"]
        if  quality == "Good" :
            weather_color ="#0C0"
        elif  quality == "Moderate" :
            weather_color ="#FFFF00"
        elif  quality == "unhealthy for sensitive groups" :
            weather_color ="#FF9900"
        elif  quality == "unhealthy" :
            weather_color ="#FF0000"
        elif  quality == "very unhealthy" :
            weather_color ="#990066"
        elif  quality == "Hazardous" :
            weather_color  ="#660000"
        
        mylabel=Label(root,text=city + "    Air Quality   " + str( category  ) + "    "+  quality , font=("Helvetica",15) ,background = weather_color)
        mylabel.pack()
        root.configure(background = weather_color)


    except Exception as e :
         api_data= " Error "
      

zip= Entry(root)
zip.grid(row = 0 , column = 0,stick=  W+E+N+S)     

zip_button= Button (root,text="Lookup zipcode",command = ZipLookup)
zip_button.grid(row = 0 , column = 1,stick=  W+E+N+S)

root.mainloop()


