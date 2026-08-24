import requests

country = input("enter your country name for info : ")
responses = requests.get("https://raw.githubusercontent.com/mledoze/countries/master/countries.json")
data = responses.json()

for info in data:
    if country.lower() in info["name"]["common"].lower():
        print(info["name"]["common"])
        print(info["capital"][0])
        print(info["region"])
        try:
            print(info["population"])
        except:
            print("this does not exists")
        

        
