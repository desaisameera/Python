#hashtags.py
#Program that lists the top ten words with maximum hash tags
#@author Amol Patil
#@author Sameera Desai

import sys
import json
import codecs
from collections import OrderedDict

#Function that reads the file and finds out the tweets
#with maximun hashtags
def getTweets(argFile):
    count=0		#Variable that counts the total number of tweets read. Initialize to 0
	attributes=0 	#list that contains the attributes of entities 
    hashText=dict ()		#Dictionary that contains the hashtags as the key and their count as value
    notHere=0		#Variable that counts if the tweet contains a hashtag or not. Initialize to 0
    
    fp=file(argFile, "r")	#Open the file for reading
    lines=fp.readlines()	#Read the twitter file line by line

    for eachLine in lines:
        try:
            tweet=json.loads(eachLine)	#Load the file which is in json format
            count=count+1;	#calculate the number of tweets in the file

            entity={}	#Dictionary that contains the entity and its attributes
            entity=None	#Initialize the dictionary to null

            hashTag={}	#Dictionary that contains the hashtag and its attributes
            hashTag=None	#Initialize the dictionary to null
            
			
			#Check if the entity is present or not. If the entity is not present
			#increment notHere by one
            if not 'entities' in tweet:
                notHere=notHere+1
			#copy the attributes if entities to the entity dictionary
            else:
                entity=tweet['entities']
				
				#Check if the entity contains values copy the key as a list 
                if entity!=None:
                    attributes=entity.keys()
                   
				   #If the hashtag is present, copy the attributes of the hashtag
				   #in the dictionary hashTag
                    for eachAttribute in attributes:
                        if eachAttribute=='hashtags':
                            hashTag=entity['hashtags']

                            hashTagLength=len(hashTag)
							
							#If the hashTag contains any text, copy the text in a variable
                            for i in range(0,hashTagLength):
                                data=hashTag[i]['text']
                                
								#If the hashtag data is already contained in the dictionary,
								#increment the value of the text by 1 else add the text to 
								#the dictionary
                                if data in hashText:
                                    hashText[data]=hashText[data]+1
                                else:
                                    hashText[data]=1

                          
                                   
        except ValueError:
            pass
            print("Error occurred")
    print("\n Read", count,"lines")
	
	#Dictionary that stores the hashtag in reverse order after sorting
    sortedHashTags=dict()

	#Sort the dictionary in reverse order
    sortedHashTags=sorted(hashText,key=hashText.get,reverse=True)
	
	#If the number of hashtags are less than 10, print all the hashtags
	#else print the first 10 hashtags
    if len(sortedHashTags)<10:
        print("The top tweets are",sortedHashTags)

    else:
        for i in range(0,10):
            print("The top ten tweets are",sortedHashTags[i])
    
    

def main():
    getTweets(sys.argv[1])
    

if __name__ == '__main__':
    main()
