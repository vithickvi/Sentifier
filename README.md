
# Sentifier 
	A Sentiment Analysis Tool for Twitter

## Prerequisites
Get Twitter Keys and Access Tokens from https://apps.twitter.com/

1. CONSUMER_KEY = ''
2. CONSUMER_SECRET =''
3. OAUTH_TOKEN = ''
4. OAUTH_SECRET = ''

## Usage
It uses Python-Django platform .Whenever the user searches the tweets are pulled from twitter based on the search keyword using Twitter API2.0 .The Sentiment analysis is performed based on the user criteria as syntactic or semantic analysis. Syntactic analysis uses Bing Liu's Positive and Negative Keyword set with rules to segregate Positve,Negative and Neutral categories. Semantic analysis uses Naive Bayes classifier with training set of .7 million and test set of .3 million with the accuracy of 73%.It segregates into two categories of Positive and Negative where us the Neutral is also classified as Negative. Once the tweets are classified the respective flags are assigned before passing to the front end and displayed


## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

