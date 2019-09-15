import tweepy
import json

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

query = "#wechat"
language = "en"
tweetCount = 2

results = api.search(q = query, lang = language, count = tweetCount)

print ("...%s tweets downloaded so far" % (len(results)))

#write tweet objects to JSON
file = open('tweet.json', 'w') 
print ("Writing tweet objects to JSON please wait...")
for status in results:
    json.dump(status._json,file,sort_keys = True,indent = 4)

#close the file
print ("Done")
file.close()