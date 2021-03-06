import time
import tweepy
from tweepy import api
import datetime

key_file = "Keys.txt"
file = "file_name.txt"
def getAllKeys():
    with open(key_file) as f:
        keys = [s.strip() for s in f.readlines()]

    consumer_key = keys[0]
    consumer_secret = keys[1]
    access_token = keys[2]
    access_token_secret = keys[3]
    print(consumer_key)
    return consumer_key,consumer_secret,access_token,access_token_secret

def get_progress(file_name,char_num):
    with open(file_name,'r',encoding="utf-8_sig") as f:
        character_all = f.read()
    num_diff = len(character_all) - char_num
    char_num = len(character_all)
    return char_num, num_diff

if __name__=='__main__':
    with open(file) as f:
        file_name = f.read()
    char_num = 0
    num_diff = 0
    consumer_key,consumer_secret,access_token,access_token_secret = getAllKeys()
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)
    wait_time = 1200 
    dt_now = datetime.datetime.now()
    tweet_first = str(dt_now.hour) +  "時" + str(dt_now.minute) + "分開始"
    api.update_status(tweet_first)

    while True:
        char_num,num_diff = get_progress(file_name,char_num)
        tweet_content = "二十分間の進捗は"+str(num_diff)+"字です."
        api.update_status(tweet_content)
        print(tweet_content)
        time.sleep(wait_time)
