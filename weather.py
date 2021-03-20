from flask import Flask,render_template,request

import json

import urllib.request

import math

app = Flask(__name__)

def tocelcius(temp):
    return str(math.ceil(float(temp) - 273.15))


@app.route('/', methods =['POST', 'GET']) 
def weather(): 
    if request.method == 'POST': 
        city = request.form['city'] 
    else: 
        # for default name Kolkata 
        city = 'Kolkata'
  
    # your API key will come here 
    api = ''
  
    # source contain json data from api 
    try:
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+api).read() 
        list_of_data = json.loads(source) 

        data = {
            'Description': (list_of_data['weather'][0]['description']),
            'temp': tocelcius(list_of_data['main']['temp']) + '°C',
            'time':str(list_of_data['timezone']),
            'cityname': str(city),
        }
        return render_template('index.html',data=data)
    except Exception:
        
        data = {
            'Description': 'Sorry',
            'temp': 'Not Found',
            'cityname': 'Type a Valid City Name',
        }
        return render_template('index.html',data=data)



if __name__ == '__main__':
    app.run(debug=True)