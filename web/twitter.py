#just a BTW, the APi on twitter allows searching statements with a definite positive/negative. Look into it
#create table mem.twt(query, tweet, time)

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import MySQLdb
import time
import json



class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)        
        tweet = all_data["text"]
        username = all_data["user"]["screen_name"]
        
        c.execute("INSERT INTO taula (time, username, tweet) VALUES (%s,%s,%s)",
            (time.time(), username, tweet))

        conn.commit()

        print((username,tweet))
        
        return True

    def on_error(self, status):
        print status

def track(filtername):

	conn = MySQLdb.connect(user="root",passwd="aditya",db="mem")
	c = conn.cursor()

	auth = OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)

	twitterStream = Stream(auth, listener())
	twitterStream.filter(track=["car"])