# EC601-Mini-Project
First Mini Project

Target User(s):

1. Marketing Director/Product manager of business company

2. President candidate

3. Singer fans

User stories:

1. Marketing Director of Venmo want to see the users feedback through specific tags

2. A company want to set up their main third party account by seeing the evaluation of apple pay and google pay 

3. A president candidate want to see the sentiment of people to his campaign policy through related tag or text 

4. A fan of Jay Chou, want to know how others think about the upcoming tour by this singer through the tour tag

5. The product manager of WeChat want to know users feedback to their new version feature

MVP:

1. Users input search query

2. Grab feeds from twitter by search query(tags or specific words)

3. Send the feeds to Google NLP API to analyse the total sentiment of query

4. Give the feedback to users
 
System Structure Graph:

https://github.com/CarlZuo/EC601-Mini-Project/blob/master/EC601-Mini-Project.jpg

System Design and how the design addresses our user stories:

Because the user needs our product to analyse the customer feelings, we can separate our task into two main part. One is grabbing feeds from twitter, and the other is analysing feeds sentiment. In the front-end, we design a user interface for user to input the tags or specific words which they want to search. Data processing center which is main function handles the input and request the GetTwitterFunction to grab twitter feeds. When the GetTwitterFunction get the result by using Twitter Service API, Data processing center pass the feeds to google part and analyse each text by google NLP API, then collect and calculate the total marks of sentiment. The final result will be print out and show on the user interface.

The API we used:

1. Twitter API:

https://developer.twitter.com/en/docs/api-reference-index

2. Tweepy API:

https://tweepy.readthedocs.io/en/latest/api.html#

3. Google NLP API:

https://cloud.google.com/natural-language/

The testing doc link is here:


Lessons learned:

1. What we liked doing:

It is a magic to see how the twitter API and google NLP API actually working, and using powerful tools to make the big disorder data becomes the useful satistics which could help to improve the products and life!

2. What we could have done better:

Mini project has very limit weeks to achieve the goals, so we couldn't filter the feeds properly and we just filter out all retweets. We may filter out spam tweets or the irrelevant tweets in the future.

3. What we will avoid in the future:

At the beginning, we built repositry on github, and we used the fork to create two different repositry which is safe but it was hard to compare and merge. For the future, we will create different branches for different teammates.

