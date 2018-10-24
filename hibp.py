<<<<<<< HEAD
#!/usr/bin/env python3

"""
Building a connector to the Have I Been Pwned site to enable checking of CybserSure customer emails against that service.

Ben Finke
@benfinke
October 2018

General conventions for function naming:

get* - Performing a lookup against HIBP
check* - Look this up in the CyberSure DB
add* - Insert data into the CyberSure DB

"""

import json
import requests
from utils import *

baseUrl = "https://haveibeenpwned.com/api/v2"

userAgent = {'User-agent': 'GetCyberSure Breach Testing'}

def getAllBreachesForAccount(email):
    # Check all breaches for a single email account
    request = baseUrl + "/breachedaccount/" + email
    response = requests.get(request, headers=userAgent)
    if response.status_code == 200:
        data = json.loads(response.content)
        return data
        #friendlyView(data, email)

    else:
        print("Something went wrong, response status was: %d" % response.status_code)

def getBreachData(name):
    # Get info from a single breach (likely to show in the interface)
    request = baseUrl + "/breach/" + name
    response = requests.get(request, headers=userAgent)
    if response.status_code == 200:
        data = json.loads(response.content)
        return data
        #friendlyBreachView(data, name)
        #print(data)
    else:
        print("Something went wrong, response status was: %d" % response.status_code)





def main():
    # Step 1 - Get all the emails to check
    data = allCustomers()
    # Step 2 - One at a time, check them against HIBP

    # Step 3 - Compare those results with the stuff in our DB

    # Step 4 - If our DB is out of date, update it

    # Step 5 - Print Results by Breach with list of users
    #getAllBreachesForAccount("ben.finke@gmail.com")
    getBreachData('Sony')

if __name__ == "__main__":
    main()
=======
#!/usr/bin/env python3

"""
Building a connector to the Have I Been Pwned site to enable checking of CybserSure customer emails against that service.

Ben Finke
@benfinke
October 2018

General conventions for function naming:

get* - Performing a lookup against HIBP
check* - Look this up in the CyberSure DB
add* - Insert data into the CyberSure DB

"""

import json
import requests
from utils import *

baseUrl = "https://haveibeenpwned.com/api/v2"

userAgent = {'User-agent': 'GetCyberSure Breach Testing'}

def getAllBreachesForAccount(email):
    # Check all breaches for a single email account
    request = baseUrl + "/breachedaccount/" + email
    response = requests.get(request, headers=userAgent)
    if response.status_code == 200:
        data = json.loads(response.content)
        return data
        #friendlyView(data, email)

    else:
        print("Something went wrong, response status was: %d" % response.status_code)

def getBreachData(name):
    # Get info from a single breach (likely to show in the interface)
    request = baseUrl + "/breach/" + name
    response = requests.get(request, headers=userAgent)
    if response.status_code == 200:
        data = json.loads(response.content)
        return data
        #friendlyBreachView(data, name)
        #print(data)
    else:
        print("Something went wrong, response status was: %d" % response.status_code)





def main():
    # Step 1 - Get all the emails to check
    data = allCustomers()
    # Step 2 - One at a time, check them against HIBP

    # Step 3 - Compare those results with the stuff in our DB

    # Step 4 - If our DB is out of date, update it

    # Step 5 - Print Results by Breach with list of users
    #getAllBreachesForAccount("ben.finke@gmail.com")
    getBreachData('Sony')

if __name__ == "__main__":
    main()
>>>>>>> 3ea0d4bb6491210789cbe40ff787881803a3df65
