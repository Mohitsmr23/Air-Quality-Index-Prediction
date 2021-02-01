#FRONT END
from tkinter import *
from tkinter import ttk
import requests
import tkinter.messagebox
from PIL import Image, ImageTk
import time
import pickle
from flask import Flask, request, jsonify, render_template
from datetime import datetime, timedelta
global f,citylist,mintemp,maxtemp,day,hour,temp,child3,child4,title,l1,mylist,loc1,mylist1,child5,child6,flag,fh,fd,flaghourly,flagdaily
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
f=0
fh=0
fd=0
flaghourly=0
flagdaily=0
flag=0
citylist=[]
mintemp=[]
maxtemp=[]
day=[]
hour=[]
temp=[]
def history():
    global citylist    
    tkinter.messagebox.showinfo('History','Your most recent searches are '.join(map(str, citylist)) )

def change():
    global child3,child4,title,l1,mylist,loc1,f,flag,flaghourly,flagdaily
    flaghourly=0
    flagdaily=0
    if f==1:
        loc1.destroy()
    if flag==1:
        child3.destroy()
        child4.destroy()
    title.destroy()
    l1.destroy()
    if fh==1:
        child5.destroy()
    monthchoosen.set('')
    if fd==1:
        child6.destroy()
    
def exit1():
    exit()
    
def mode():
    child1.config(bg='blue')
    child2.config(bg='blue')
    tkinter.messagebox.showinfo('Theme','Theme may strain your Eyes. Change theme according to surrounding lighting')
    
def loc():
    monthchoosen.set('')
    global f,loc1
    f=1
    import geocoder
    from geopy.geocoders import Nominatim
    g = geocoder.ip('me')
    geocoder = Nominatim(user_agent = 'your_app_name')
    location = geocoder.reverse(tuple(g.latlng))
    loc1=Label(parent,text='Address = '+location[0],wraplength=500)
    parent.add(loc1)
    global city,citylist
    city=location[0][-13:-7]
    citylist.append(city)
def abt():
    window=Tk()
    window.title('Information')
    l=Label(window,text='Weather forecast app fetching data via API and predicting PM2.5 using ANN. Developed by Rohan, Aayuesh, Yash and Mohit',wraplength=300,justify='left').pack()
    l.place(x=0,y=0)
    window.geometry("300x100")
    mainloop()

def current():
    global citylist
    citylist.append(cityname.get())
    global f,city,child3,child4,title,l1,mylist,flag
    child3=PanedWindow(parent,orient=VERTICAL)
    flag=1
    if f==0 or cityname.get()!='':
        city=cityname.get()
    l1=Label(child3,bg='slategray',text='Current weather of '+city)
    l1.config(fg='white')
    child3.add(l1)
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=cc97f396b726ec1d0e7aa66d98c56cd8'
    json_data = requests.get(url).json()
    format_add = json_data['main']
    
    #child3.config(height=100)
    child31=PanedWindow(child3)
    temp=Label(child31,text=str(int(format_add['temp']-273))+'°C')
    temp.config(font=("Courier", 50))
    if int(time.strftime("%H"))>6 and int(time.strftime("%H"))<18:
        temp.config(bg='light sky blue1')
    else:
        temp.config(bg='dark slate gray')
        temp.config(fg='white')

    child31.add(temp)
    #parent.add(child3)
    child4=PanedWindow(child31,orient=VERTICAL)
    mintemp=Label(child4,text='Min Temp = '+str(int(format_add['temp_min']-273)-13)+'°C')
    mintemp.config(font=("Courier", 12))
    if int(time.strftime("%H"))>6 and int(time.strftime("%H"))<18:
        mintemp.config(bg='light sky blue1')
    else:
        mintemp.config(bg='dark slate gray')
        mintemp.config(fg='white')

    child4.add(mintemp)
    maxtemp=Label(child4,text='Max Temp = '+str(int(format_add['temp_max']-273))+'°C')
    maxtemp.config(font=("Courier", 12))
    if int(time.strftime("%H"))>6 and int(time.strftime("%H"))<18:
        maxtemp.config(bg='light sky blue1')
    else:
        maxtemp.config(bg='dark slate gray')
        maxtemp.config(fg='white')
    child4.add(maxtemp)
    feelslike=Label(child4,text='Feels like '+str(int(format_add['feels_like'])-273)+'°C'+'\n'+'The current weather has/is '+json_data['weather'][0]['main']+'.')
    child4.add(feelslike)
    if int(time.strftime("%H"))>6 and int(time.strftime("%H"))<18:
        feelslike.config(bg='light sky blue1')
    else:
        feelslike.config(bg='dark slate gray')
        feelslike.config(fg='white')
    child31.add(child4)
    limg = Label(child31)
    limg.config(width=170)
    
    if int(time.strftime("%H"))>6 and int(time.strftime("%H"))<18:
        if json_data['weather'][0]['main']=='Mist':
            img = Image.open(r"C:\Users\admin\Desktop\mist day.jpg")
        elif json_data['weather'][0]['main']=='Smoke' or json_data['weather'][0]['main']=='Haze':
            img = Image.open(r"C:\Users\admin\Desktop\smoke-day.jpg")
        elif json_data['weather'][0]['main']=='Clouds':
            img = Image.open(r"C:\Users\admin\Desktop\day-clouds.jpg")
        elif json_data['weather'][0]['main']=='Rain':
            img = Image.open(r"C:\Users\admin\Desktop\rain-day.jpg")   
        else:
            img = Image.open(r"C:\Users\admin\Desktop\clear-day.jpg")


    else:
        if json_data['weather'][0]['main']=='Mist':
            img = Image.open(r"C:\Users\admin\Desktop\mist night.jpg")
        elif json_data['weather'][0]['main']=='Smoke' or json_data['weather'][0]['main']=='Haze':
            img = Image.open(r"C:\Users\admin\Desktop\smoke-night.jpg")
        elif json_data['weather'][0]['main']=='Clouds':
            img = Image.open(r"C:\Users\admin\Desktop\night-clouds.jpg")
        elif json_data['weather'][0]['main']=='Rain':
            img = Image.open(r"C:\Users\admin\Desktop\rain-night.jpg")   
        else:
            img = Image.open(r"C:\Users\admin\Desktop\clear-night.jpg")
            
    limg.img = ImageTk.PhotoImage(img)
    limg['image'] = limg.img
    limg.pack()
    if int(time.strftime("%H"))>6 and int(time.strftime("%H"))<18:
        limg.config(bg='light sky blue1')
    else:
        limg.config(bg='dark slate gray')
        limg.config(fg='white')

    child31.add(limg)
    
    child3.add(child31)
    child4 = PanedWindow(child3,orient='vertical')
    title = Label(child4, text='Pressure         Humidity         Visibility         Wind Speed         PM2.5 ',relief='solid',justify=LEFT)
    #response = requests.get( 'http://5cb818282303.ngrok.io ',  data={'a':,'b':,'c':,'d':,'e':}).json()
    a=format_add['temp']-273
    b=json_data['main']['pressure']
    c=json_data['main']['humidity']
    d=json_data['visibility']/1000.0
    e=json_data['wind']['speed']

    url = "http://f9f28231d877.ngrok.io"
    payload="{\r\n    \"a\":"+str(format_add['temp']-273)+",\r\n    \"b\":"+str(json_data['main']['pressure'])+",\r\n    \"c\":"+str(json_data['main']['humidity'])+",\r\n    \"d\":"+str(json_data['visibility']/1000.0)+",\r\n    \"e\":"+str(json_data['wind']['speed'])+"\r\n}"
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload).json()
    result = Label(child4, text=str(json_data['main']['pressure'])+' millibar            '+str(json_data['main']['humidity'])+'%            '+str(json_data['visibility']/1000.0)+' km            '+str(json_data['wind']['speed'])+' kmph            '+response['Prediction'][1:-1],justify=LEFT)
    child4.add(title)
    child4.add(result)
    child3.add(child4)
    parent.add(child3)


def hourly():
    global citylist,flaghourly
    flaghourly=1
    citylist.append(cityname.get())
    global f,city,temp,hour,child3,child4,title,l1,mylist,mylist1,child5,fh
    child5=PanedWindow(parent,orient=VERTICAL)
    fh=1
    if f==0 or cityname.get()!='':
        city=cityname.get()
    l1=Label(child5,bg='slategray',text='Hourly weather of '+city)
    l1.config(fg='white')
    child5.add(l1)
    title = Label(child5,text='Time(Hourly)               Temperature               Pressure               Humidity               Visibility               Wind Speed               Weather               PM2.5 ',relief='solid',justify='left')
    child5.add(title)
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/hourly"
    url1 = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=cc97f396b726ec1d0e7aa66d98c56cd8'
    json_data = requests.get(url1).json()
    querystring = {"lat": str(json_data['coord']['lat']), "lon": str(json_data['coord']['lat']), "hours": "48"}
    headers = {
        'x-rapidapi-key': "f538519bddmshdd875603384a825p11fd5bjsn0639eb1a04a7",
        'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    mylist1 = Listbox(child5)
    scrollbar = Scrollbar(mylist1)
    scrollbar.pack(side=RIGHT, fill=Y)
    for i in range(24):
        #if response['data'][i]['weather']['description']=='Clear Sky':
        url = "http://f9f28231d877.ngrok.io"
        payload="{\r\n    \"a\":"+str(response['data'][i]['temp'])+",\r\n    \"b\":"+str(json_data['main']['pressure'])+",\r\n    \"c\":"+str(json_data['main']['humidity'])+",\r\n    \"d\":"+str(json_data['visibility']/1000.0)+",\r\n    \"e\":"+str(json_data['wind']['speed'])+"\r\n}"
        headers = {
                'Content-Type': 'application/json'
                }   
        response2 = requests.request("GET", url, headers=headers, data=payload)
        response1=response2.json()
        print(response1)
        mylist1.insert(END, response['data'][i]['timestamp_utc'].replace('T',' ') + '         ' + str(response['data'][i]['temp']) + '°C               ' + str(response['data'][i]['pres']) + ' millibar               ' + str(response['data'][i]['rh']) + '%               ' + str(response['data'][i]['vis'] / 10.0) + 'km            ' + str(response['data'][i]['wind_gust_spd']) + ' kmph           '+response['data'][i]['weather']['description']+'         '+response1['Prediction'][1:-1])
        #response2.close()

        if int(response['data'][i]['timestamp_utc'].replace('T',' ')[-8:-6])<6 or int(response['data'][i]['timestamp_utc'].replace('T',' ')[-8:-6])>19:
            mylist1.itemconfig(END,bg='dark slate grey')
            mylist1.itemconfig(END,fg='white')
        elif int(response['data'][i]['timestamp_utc'].replace('T',' ')[-8:-6])<8 or int(response['data'][i]['timestamp_utc'].replace('T',' ')[-8:-6])>=18:
            mylist1.itemconfig(END,bg='light grey')
        else:
            mylist1.itemconfig(END,bg='light sky blue1')            
        hour.append(response['data'][i]['timestamp_utc'].replace('T',' '))
        temp.append(response['data'][i]['temp'])
    mylist1.pack(side=LEFT, fill=BOTH)
    mylist1.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=mylist1.yview)
    child5.add(mylist1)
    parent.add(child5)
    
def daily():
    global citylist,flagdaily
    flagdaily=1
    citylist.append(cityname.get())
    global f,city,mintemp,maxtemp,day,l1,child6,title,fd
    child6=PanedWindow(parent,orient=VERTICAL)
    fd=1
    if f==0 or cityname.get()!='':
        city=cityname.get()
    l1=Label(child6,bg='slategray',text='Daily weather of '+city)
    l1.config(fg='white')
    child6.add(l1)
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/daily"
    url1 = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=cc97f396b726ec1d0e7aa66d98c56cd8'
    json_data = requests.get(url1).json()
    querystring = {"lat": str(json_data['coord']['lat']), "lon": str(json_data['coord']['lon'])}
    headers = {
        'x-rapidapi-key': "f538519bddmshdd875603384a825p11fd5bjsn0639eb1a04a7",
        'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    title = Label(child6, text='Date         Min Temp         Max Temp         Pressure         Humidity         Visibility         Wind Speed         Weather         PM2.5 ',relief='solid',justify='left')
    child6.add(title)
    mylist = Listbox(child6)
    scrollbar = Scrollbar(mylist)
    scrollbar.pack(side=RIGHT, fill=Y)
    x = '2021-01-11' 
    for i in range(15):
        x=(datetime.strptime(x, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
        
        url = "http://f9f28231d877.ngrok.io"
        payload="{\r\n    \"a\":"+str(response['data'][i]['temp'])+",\r\n    \"b\":"+str(json_data['main']['pressure'])+",\r\n    \"c\":"+str(json_data['main']['humidity'])+",\r\n    \"d\":"+str(json_data['visibility']/1000.0)+",\r\n    \"e\":"+str(json_data['wind']['speed'])+"\r\n}"
        headers = {
            'Content-Type': 'application/json'
        }
        response3 = requests.request("GET", url, headers=headers, data=payload)
        response1=response3.json()
        
        mylist.insert(END, '    '+x+'         '+str(response['data'][i]['min_temp']) + '°C         '+str(response['data'][i]['max_temp']) + '°C         ' + str(response['data'][i]['pres']) + ' millibar         ' + str(response['data'][i]['rh']) + '%         ' + str(response['data'][i]['vis'] / 10.0) + 'km         ' + str(response['data'][i]['wind_gust_spd']) + ' kmph         '+response['data'][i]['weather']['description']+'         '+response1['Prediction'][1:-1])
        #response2.close()
        if i%2==0:
            mylist.itemconfigure(END, background="lightgray")
        mintemp.append(response['data'][i]['min_temp'])
        maxtemp.append(response['data'][i]['max_temp'])
        day.append(x)
    mylist.pack(side=LEFT, fill=BOTH)
    mylist.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=mylist.yview)
    child6.add(mylist)
    parent.add(child6)

def analytics():
    global day,hour,maxtemp,mintemp,temp,city,flaghourly,flagdaily
    #hour=[]
    #day=[]
    #temp=[]
    #maxtemp=[]
    #mintemp=[]
    #hourly()
    #daily()
    if flaghourly==1:
        fig = Figure(figsize=(16,4)) 
        analysis=Tk()
        analysis.title('Analysis')
        plot1=fig.add_subplot(111)
        hr=[]
        for h in hour:
            hr.append(h[-8:-3])
        plot1.plot(hr,temp,'-o')
        plot1.set_title('Hourly Temperature of '+city)
        plot1.set_ylabel('Temperature in °C')
        plot1.set_xlabel('Time (Hourly)')
        canvas=FigureCanvasTkAgg(fig,master=analysis)
        canvas.draw()
        canvas.get_tk_widget().pack()
        toolbar=NavigationToolbar2Tk(canvas,analysis)
        toolbar.update()
        canvas.get_tk_widget().pack()
    if flagdaily==1:
        fig=Figure(figsize=(16,4))
        plot2=fig.add_subplot(111)
        d1=[]
        for d in day:
            d1.append(d[-5:])
        plot2.plot(d1,maxtemp,'-o')
        plot2.plot(d1,mintemp,'-o')
        plot2.set_title('Daily Temperature of '+city)
        plot2.set_ylabel('Temperature in °C')
        plot2.set_xlabel('Date')
        plot2.legend(["Max temp", "Min temp"]) 
        canvas=FigureCanvasTkAgg(fig,master=analysis)
        canvas.draw()
        canvas.get_tk_widget().pack()
        toolbar=NavigationToolbar2Tk(canvas,analysis)
        toolbar.update()
        canvas.get_tk_widget().pack()
    mainloop()
root=Tk()
flag=0

root.title('Weather Information')
parent=PanedWindow(root,orient=VERTICAL)
parent.pack(fill = BOTH, expand = 1)
child1=PanedWindow(parent)
child1.pack(fill = BOTH, expand = 1)
lcity=Label(child1,text='City Name')
child1.add(lcity)
location=Button(parent,text='Detect Current Location',command=loc)
parent.add(location)

cityname=StringVar()
monthchoosen = ttk.Combobox(child1, width = 27, textvariable = cityname) 
monthchoosen['values'] = ('ahmedabad','jaipur','delhi','lucknow','kanpur','bangalore','mumbai','pune','london','moscow','tokyo','chicago') 
child1.add(monthchoosen)
parent.add(child1)
child2=PanedWindow(parent)
bcurrent=Button(child2,text='Current Weather/Refresh',command=current)
child2.add(bcurrent)
bhourly=Button(child2,text='Hourly Weather',command=hourly)
child2.add(bhourly)
bdaily=Button(child2,text='Daily Weather',command=daily)
child2.add(bdaily)
banalytics=Button(child2,text='Analytics',command=analytics)
child2.add(banalytics)
anothercity=Button(child2,text='Another city',command=change)
child2.add(anothercity)
parent.add(child2)
menu=Menu(root)
root.config(menu=menu)
subm1=Menu(menu)
menu.add_cascade(label='File',menu=subm1)
subm1.add_command(label='Exit',command=exit1)
subm1.add_command(label='Dark/Light mode',command=mode)
subm2=Menu(menu)
menu.add_cascade(label='About',menu=subm2)
subm2.add_command(label='Description',command=abt)
subm2.add_command(label='History',command=history)
mainloop()