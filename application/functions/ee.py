import os
import json

# Path to the Earth Engine credentials file on Windows
credentials_path = os.path.expanduser("~\\.config\\earthengine\\credentials")

# Read the file
with open(credentials_path, 'r') as file:
    credentials = json.load(file)

# The token will be in the credentials dictionary
# token = credentials['access_token']
print(credentials)


# AIzaSyBWqUl-HlAe-bbl_jNiFdrFu5gEcLe7Bes

# google maps platform api key
# AIzaSyD2PNX7zW8Q33ls4lT7juiO9g2cng9Yd7I