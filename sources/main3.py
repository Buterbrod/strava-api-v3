import json
import os
import requests
import time

# Read the token from the saved file
with open('strava_token.json', 'r') as token:
  data = json.load(token)

# Get the access token
access_token = data['access_token']

# Build the API url to get athlete info
athlete_url = f"https://www.strava.com/api/v3/athlete?" \
              f"access_token={access_token}"

# Get the response in json format
response = requests.get(athlete_url)
athlete = response.json()

# Print out the retrieved information
print('RESTful API:', athlete_url)
print('='* 5, 'ATHLETE INFO', '=' * 5)
print('Name:', athlete['firstname'], '"' + str(athlete['username'] or '') + '"', athlete['lastname'])
print('Gender:', athlete['sex'])
print('City:', athlete['city'], athlete['country'])
print('Strava athlete from:', athlete['created_at'])