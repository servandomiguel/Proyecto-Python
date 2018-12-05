#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
import auth_credentials as cred
import json

def authenticate():
    auth = tweepy.OAuthHandler(cred.consumer_key, cred.consumer_secret)
    auth.set_access_token(cred.access_token, cred.access_token_secret)
    return tweepy.API(auth)

def getAllTweets(account_name):
    return [tweet for tweet in tweepy.Cursor(api.user_timeline,id=account_name).items()]

def dumpTweetToJson(tweet):
    return json.dumps(tweet._json)
if __name__ == '__main__':
    api = authenticate()
    # Prueba de autenticación con tweepy
    user = api.me()
    print(user.name)
    print('@' + api.me().screen_name)
    l = getAllTweets('espnmx')
    print dumpTweetToJson(l[0])
    print 
