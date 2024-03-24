from flask import Flask, request, make_response, jsonify
import requests

app = Flask(__name__)
## TODO: STEP 1 
APIKEY = "??" # Place your API KEY Here... 
#"8a81d247d650cb16469c4ba3ceb7d265"

# **********************
# UTIL FUNCTIONS : START
# **********************

def getjson(url):
    resp =requests.get(url)
    return resp.json()

def getWeatherInfo(location):
    API_ENDPOINT = f"http://api.openweathermap.org/data/2.5/weather?APPID={APIKEY}&q={location}"
    data = getjson(API_ENDPOINT)
	
    return ???
# **********************
# UTIL FUNCTIONS : END
# **********************

# *****************************
# Intent Handlers funcs : START
# *****************************


def getWeatherIntentHandler(req):
    """
    Get location parameter from dialogflow and call the util function `getWeatherInfo` to get weather info
    """
  
    
    return f"Currently in  , its "

# ***************************
# Intent Handlers funcs : END
# ***************************


# *****************************
# WEBHOOK MAIN ENDPOINT : START
# *****************************
@app.route('/', methods=['POST'])
def webhook():
	req = request.get_json(silent=True, force=True)
	intent_name = req["queryResult"]["intent"]["displayName"]
   
   
	resp_text = "Unable to find a matching intent. Try again."
	
	return make_response(jsonify({'fulfillmentText': respose_text}))

# ***************************
# WEBHOOK MAIN ENDPOINT : END
# ***************************

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)