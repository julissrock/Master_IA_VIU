import requests
def main():
    try:
        location = input(str("Enter your location: "))
        url = 'http://api.weatherapi.com/v1/current.json?key=08a512ec1a254237a2c180126231905&q='+location+'&aqi=no'
        response = requests.get(url)
        weather = response.json()
        temp = weather['current']['temp_c']
        description = weather['current']['condition']['text']

        print("Today the weather in", location, "is", description, "and", temp, "degrees Celsius.")
    except: 
        print("Please enter a valid location.")    
    
main()