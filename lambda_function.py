import json
import tweepy
from datetime import date
from os import environ

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

def lambda_handler(event, context):
    message = create_tweet()
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }

def create_tweet():
    dt1stRound = date(2022, 10,2)
    dt2ndRound = date(2022, 10,30)
    dtTenure = date(2023, 1,1)
    today = date.today()
    daysTo1stRound = abs(dt1stRound - today).days
    daysTo2ndRound = abs(dt2ndRound - today).days
    daysToTenure = abs(dtTenure - today).days
    
    message = '{} dias até o 1º turno.\n{} dias até o 2º turno (se houver).\n{} dias até a posse de @LulaOficial.'.format(daysTo1stRound, daysTo2ndRound, daysToTenure)
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(message)
    return message
