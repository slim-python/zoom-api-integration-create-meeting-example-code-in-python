import jwt
import requests
import json
from time import time

API_KEY = 'YOUR API KEY'
API_SEC = 'YOUR API SECRET'

# your zoom live meeting id, it is optional though
meetingId = 83781439159

userId = 'you can get your user Id by running the getusers()'

# create a function to generate a token using the pyjwt library
def generateToken():
    token = jwt.encode(
        # Create a payload of the token containing API Key & expiration time
        {'iss': API_KEY, 'exp': time() + 5000},
        # Secret used to generate token signature
        API_SEC,
        # Specify the hashing alg
        algorithm='HS256'
        # Convert token to utf-8
    )
    return token
    # send a request with headers including a token

#fetching zoom meeting info now of the user, i.e, YOU
def getUsers():
    headers = {'authorization': 'Bearer %s' % generateToken(),
               'content-type': 'application/json'}

    r = requests.get('https://api.zoom.us/v2/users/', headers=headers)
    print("\n fetching zoom meeting info now of the user ... \n")
    print(r.text)


#fetching zoom meeting participants of the live meeting

def getMeetingParticipants():
    headers = {'authorization': 'Bearer %s' % generateToken(),
               'content-type': 'application/json'}
    r = requests.get(
        f'https://api.zoom.us/v2/metrics/meetings/{meetingId}/participants', headers=headers)
    print("\n fetching zoom meeting participants of the live meeting ... \n")

    # you need zoom premium subscription to get this detail, also it might not work as i haven't checked yet(coz i don't have zoom premium account)

    print(r.text)


# this is the json data that you need to fill as per your requirement to create zoom meeting, look up here for documentation
# https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/meetingcreate


meetingdetails = {"topic": "The title of your zoom meeting",
                  "type": 2,
                  "start_time": "2019-06-14T10: 21: 57",
                  "duration": "45",
                  "timezone": "Europe/Madrid",
                  "agenda": "test",

                  "recurrence": {"type": 1,
                                 "repeat_interval": 1
                                 },
                  "settings": {"host_video": "true",
                               "participant_video": "true",
                               "join_before_host": "False",
                               "mute_upon_entry": "False",
                               "watermark": "true",
                               "audio": "voip",
                               "auto_recording": "cloud"
                               }
                  }

def createMeeting():
    headers = {'authorization': 'Bearer %s' % generateToken(),
               'content-type': 'application/json'}
    r = requests.post(
        f'https://api.zoom.us/v2/users/{userId}/meetings', headers=headers, data=json.dumps(meetingdetails))

    print("\n creating zoom meeting ... \n")
    print(r.text)

getUsers()
# getMeetingParticipants()
createMeeting()

###################################
# hire me pls ;(
###################################