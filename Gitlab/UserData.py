##############################################################################################################
# Author: Bhavya Bojanapalli
# This is a simple program which returns the user information by taking input as username of github
#################################################################################################################

import requests
from pprint import pprint

# github username
username = "BhavyaBojanapalli"
# url to request
url = "https://api.github.com/users/"+username
# make the request and return the json
user_data = requests.get(url)
print(dir(user_data))
pprint(user_data.json())
