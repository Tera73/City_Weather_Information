from flask import Flask, render_template, request
import json
import urllib.request 

app= Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/index.html')
def gotoindex():
	return render_template('index.html')


@app.route('/', methods=['POST'])
def getw_data():
	try:
		city=request.form['city']
		api_key="bb4156998a0c5b59919f2242e6ad24d7" 
		base_url = "http://api.openweathermap.org/data/2.5/weather?"
		complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"
		url = complete_url.replace(" ","+")
		source = urllib.request.urlopen(url).read()
		w_data = json.loads(source) 
		  
		temperature=w_data['main']['temp']
		pressure=w_data['main']['pressure']
		humidity=w_data['main']['humidity']
		windspeed=w_data['wind']['speed']
		clouds=w_data['clouds']['all']
		weather=w_data['weather'][0]['main']
		description=w_data['weather'][0]['description']
		icon=w_data['weather'][0]['icon']

	except requests.exceptions.RequestException as e:
		return messagebox.showinfo("error", "No such city")
	
	return render_template("output.html",cty=city.upper(), wea=description, temp=temperature, press=pressure,humid=humidity,winds=windspeed, clo=clouds, icon_code=icon)

@app.errorhandler(Exception)
def server_error(err):
    app.logger.exception(err)
    return "Error: There is no such city. Please try again!", 500

if __name__=="__main__":
	app.run()

