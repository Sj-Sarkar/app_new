from django.shortcuts import render,HttpResponse
import requests
# Create your views here.
def index(request):
    api_key = '37bca6691ab9b60b74ebf2833db1cb81'

    user_input = request.POST.get('city')

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

    def f2c(farienhiet):
        c=5*(farienhiet-32)/9
        return round(c)

    #print(weather_data.status_code)  #200 means Connected 401 means not connected/authenticated
    #print(weather_data.json())       #returns every data and infprmaion of the City but with a extension .json is necesssary to give 
    #print(weather_data.json()['weather'][0]['main'])
    #print(weather_data.json()['main']['temp'])


    if weather_data.json()['cod'] == '404':      #['cod'] is basically the status code. So if it returns 404 mena sthe city is not found
        print("No City Found")
    else:
        
        print(weather_data.json())
        weather = weather_data.json()['weather'][0]['main']
        farienhiet=weather_data.json()['main']['temp']
        feelslike=weather_data.json()['main']['feels_like']
        press=weather_data.json()['main']['pressure']
        humid=weather_data.json()['main']['humidity']
        wind=weather_data.json()['wind']['speed']
        print(f"The Temperature at {user_input} is {f2c(farienhiet)}ºC")
        print(f"Feelss like {f2c(feelslike)}ºC")
        print(f"The weather in {user_input} is: {weather}")
        print(f"and it's in {weather_data.json()['sys']['country']}")
        print(f"Wind speed is {wind}")
        print(f"Wind speed is {press}")

    data={
        'city':user_input,
        'temp':f2c(farienhiet),
        'feels':f2c(feelslike),
        'wind':weather,
        'press':press,
        'humid':humid,
        'wind':wind
    }
    return render(request,'Output.html',data)
def lime(request):
    return render(request,'City.html')
def sub(request):
    return HttpResponse("Thanks for Submitting")