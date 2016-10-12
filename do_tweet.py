import sys, os, csv
import tweepy
import optparse

def do_api(config):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def get_tweet(txt): 
	if type(txt) == str: 
		return txt
	else: 
		return "Well, someone fucked up!"

def main(txt):
  cfg = { 
    "consumer_key"        : "VALUE",
    "consumer_secret"     : "VALUE",
    "access_token"        : "VALUE",
    "access_token_secret" : "VALUE" 
    }

  api = do_api(config)
  tweet = get_tweet(txt) 
  status = api.update_status(status=tweet) 
	print "Thing done!"
	return None

#command line arguments

parser = optparse.OptionParser()

parser.add_option('-t', '--tweet',
  action="store", dest="tweet",
  help="query string", default="spam")

options, args = parser.parse_args()
print 'Tweet string:', options.tweet


main(options.tweet)
