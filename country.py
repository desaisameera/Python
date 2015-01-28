#country.py which lists the countries with
#the maximum activity

#@author Amol Patil
#@author Sameera Desai 

import sys
import json
import codecs
from collections import OrderedDict

#Function that lists the three the countries with maximum activity
def getTweets(argFile):
    
    count=0		#Variable that counts the total number of tweets read. Initialize to 0
	notHere=0	#Variable that counts if the tweet contains a place or not. Initialize to 0
	country=dict()	#Initialize a dictionary that stores the countires as the key and their count as value
	p={}	#Dictinary to store the attributes of place
    p=None	#Initialize it to null
    fp=file(argFile,"r")	#Open the file for reading
    lines=fp.readlines()	#Read the twitter file line by line

    for eachLine in lines:
            try:
                tweet=json.loads(eachLine)	#Load the file which is in json format
                count=count+1	#calculate the number of tweets in the file

				#Check if the tweet contains a palce or not. If there is no place
				#increase notHere by 1 else copy the attributes of place to the dictionary place
                if not 'place' in tweet:
                    notHere=notHere+1
                else:
                    p=tweet['place']
					
					#Check if the place has value or not
                    if p!=None:
                        keys=p.keys()
						#for the value of 'country_code' copy the value of the country_code in the hashKey
                        for eachKey in keys:
                            if eachKey=='country':
                                hashKey=p[eachKey]
								
								#If the country is already present in the dictionary, increment the value
								#of that country by 1 otherwise add that country to the dictionary
                                if hashKey in country:
                                    country[hashKey]=country[hashKey]+1
                                else:
                                    country[hashKey]=1
                                
                                
                                
                        
                    
            except ValueError:
                pass
                print("Error occured")
    print("\nRead",count,"lines")
    
	
    sortedCountry=dict()	#A new dictionary for sorting and storing the dictionary of countries in reverse order
	
	#Sort the country dictionary in reverse order
    sortedCountry=sorted(country,key=country.get,reverse=True)

	#If there are less than 3 countries in the tweets, print all the countries
	#else print the first three countries
    if len(sortedCountry)<3:
        print("The countries are",sortedCountry)

    else:
        for i in range(0,3):
            print("The codes of the country with maximum activity are",sortedCountry[i])

    
def main():
    getTweets(sys.argv[1])
if __name__=='__main__':
    main()
    
