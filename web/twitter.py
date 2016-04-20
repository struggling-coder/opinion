#just a BTW, the APi on twitter allows searching statements with a definite positive/negative. Look into it
#create table mem.twt(query varchar(50), tweet varchar(150), time varchar(20)

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import MySQLdb
import time
import json

ckey='pTlSX6TKUaoHDVF67BgF3yHDY'
csecret='OVQelHvTtHuHlpmQa8IoSYKEABTAHHHYMtPN2DeqOVnJsdKLhD'
atoken='720586054223339521-Uo4T10dtKwUK7yp7OQFR51k0X9fxfeT'
asecret='wIWzrm3DmRw4yr6hb06KbmactF8HxC7fikpzhew5d9u26'

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)        
        tweet = all_data["text"]
        username = all_data["user"]["screen_name"]
        ts = all_data["timestamp_ms"]
        
        c.execute("insert into twt VALUES('"+qu+"','"+tweet+"','"+ts+"')")

        #print all_data
        #print '-------------------------------------------------------------'

        #c.execute("INSERT INTO taula (time, username, tweet) VALUES (%s,%s,%s)",
        #            (time.time(), username, tweet))

        conn.commit()

        return True

    def on_error(self, status):
        print status

def track(filtername):

	conn = MySQLdb.connect(user="root",passwd="aditya",db="test")
	c = conn.cursor()

	auth = OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)

	twitterStream = Stream(auth, listener())
	twitterStream.filter(track=[filtername])

def pr(filtername):
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    twitterStream = Stream(auth, _listener())
    twitterStream.filter(track=[filtername])

class _listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)        
        tweet = all_data["text"]
        print str(unicode(tweet).encode("utf-8"))
        #print all_data
        #print '-------------------------------------------------------------'

        #c.execute("INSERT INTO taula (time, username, tweet) VALUES (%s,%s,%s)",
        #            (time.time(), username, tweet))
        return True

    def on_error(self, status):
        print status
     