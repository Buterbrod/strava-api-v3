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

# Build the API url to get activities data
activities_url = f"https://www.strava.com/api/v3/athlete/activities?" \
          f"access_token={access_token}"
print('RESTful API:', activities_url)

# Get the response in json format
response = requests.get(activities_url)
activity = response.json()[5]

# Print out the retrieved information
print('='*5, 'SINGLE ACTIVITY', '='*5)
print('Athlete:', athlete['firstname'], athlete['lastname'])
print('Name:', activity['name'])
print('Date:', activity['start_date'])
print('Disance:', activity['distance'], 'm')
print('Average Speed:', activity['average_speed'], 'm/s')
print('Max speed:', activity['max_speed'], 'm/s')
print('Moving time:', round(activity['moving_time'] / 60, 2), 'minutes')
print('Location:', activity['location_city'], 
      activity['location_state'], activity['location_country'])