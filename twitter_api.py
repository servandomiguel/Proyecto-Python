import tweepy
import auth_credentials as cred

def authenticate():
    auth = tweepy.OAuthHandler(cred.consumer_key, cred.consumer_secret)
    auth.set_access_token(cred.access_token, cred.access_token_secret)
    return tweepy.API(auth)

if __name__ == '__main__':
    api = authenticate()
    # Prueba de autenticación con tweepy
    user = api.me()
    print(user.name)
    print('@' + api.me().screen_name)
