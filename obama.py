import sys
import json
import codecs
from collections import OrderedDict

def getTweets(argFile):
    # counter to keep track of number of tweets containing obama
    count=0
    fp=file(argFile,"r")
    lines=fp.readlines()
    for eachLine in lines:
	try:
	    tweet=json.loads(eachLine)
	    if 'text' in tweet:
		#copies text of the tweet in a variable named text
		text=tweet['text']
	        
		#condition to check whether the text contains obama
		if 'Obama' in text or 'obama' in text:
		    #increments counter
		    count = count+1

	except ValueError:
       	    pass
	    print("Error occurred")
    #prints number of tweets containing obama
    print("Number of tweets mentioning Obama is ")
    print(count)
    
def main():
    getTweets(sys.argv[1])
if __name__=='__main__':
    main()
