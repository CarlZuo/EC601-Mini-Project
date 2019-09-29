import tweepy

def getTwitterFeeds(searchQuery, lang, twitter_numbers, r_type):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)

	api = tweepy.API(auth)

	query = searchQuery + '-filter:retweets'
	language = lang
	tweetCount = twitter_numbers
	reselt_type = r_type

	results = api.search(q = query, lang = language, result_type = reselt_type, count = tweetCount)

	print ("...%s tweets downloaded so far" % (len(results)))

	#write tweet objects to JSON
	file = open('myResultsTweet.txt', 'w') 
	print ("Writing tweet objects to Text file please wait...")
	i = 1
	tweetList = []

	for status in results:
		#print each tweet to JSON
		tweetList.append(status.text)
		file.write(str(i) + ':')
		file.write(status.text)
		file.write('\n')
		i += 1

	#close the file
	print ("Done")
	file.close()
	return tweetList

if __name__ == '__main__':
	getTwitterFeeds("iphone", "en", 100, "recent")
