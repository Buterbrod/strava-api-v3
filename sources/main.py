import json
import os
import requests
import time

STRAVA_TOKEN_FILE = 'strava_token.json'
URL_BASE = 'https://www.strava.com/api/v3'
URL_GET_AUTH_TOKEN = f'{URL_BASE}/oauth/token'
URL_GET_LOGGED_IN_ATHLETE = f'{URL_BASE}/athlete?access_token={access_token}'
URL_GET_LOGGED_IN_ATHLETE_ACTIVITIES = f'{URL_BASE}/athlete/activities?access_token={access_token}'
URL_GET_LOGGED_IN_ATHLETE_ZONES = f'{URL_BASE}/athlete/zones?access_token={access_token}'
URL_GET_LOGGED_IN_ATHLETE_ZONES =
GET_ZONES_BY_ACTIVITY_ID
	get_activity_by_id / activities/{id}
    get_laps_by_activity_id '/activities/{id}/laps'
    

class StravaAPI: 
    def get_strava_token(client_id, client_secret, code):
        token = requests.post(
            url = URL_GET_AUTH_TOKEN,
            data = {
                'client_id': client_id,
                'client_secret': client_secret,
                'code': code,
                'grant_type': 'authorization_code'
            })
        strava_token = token.json()
        return strava_token

    def save_strava_token(auth_token):
        with open(STRAVA_TOKEN_FILE, 'w') as out_file:
            json.dump(auth_token, out_file)

    def load_strava_token():
        with open(STRAVA_TOKEN_FILE, 'r') as in_file:
            strava_token = json.load(in_file)
        return strava_token
        
    def get_access_token(strava_token):
        return strava_token['access_token']

    def get_refresh_token(strava_token):
        return strava_token['refresh_token']

stravaAPI = StravaAPI()

# Initial Settings
client_id = '74167'
client_secret = '7ac23a78f1042dcd183437aec28cbfe076448512'
code = '300a70cc06b16e2f5e095ec53202bd7f310813d3'

# -------------------------------------------------------------------------------------
# At the first time - get token
# -------------------------------------------------------------------------------------
# auth_token = stravaAPI.get_auth_token(client_id, client_secret, code)
# stravaAPI.save_auth_token(auth_token)

# -------------------------------------------------------------------------------------
# At the next time - load & use the saved token
# -------------------------------------------------------------------------------------
auth_token = stravaAPI.load_auth_token()
access_token = stravaAPI.get_access_token(auth_token)
refresh_token = stravaAPI.get_refresh_token(auth_token)

# Build the API url to get athlete info
athlete_url = "https://www.strava.com/api/v3/athlete?access_token={access_token}"

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


