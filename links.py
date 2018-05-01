'''
Python script to scrap links from times of india archives.
Stores the links in a text file 
'''

import requests
from bs4 import BeautifulSoup
import os

#Starting to scrape from 31/12/2017 and decrements further till 1/1/2010
date_year = 2017 
date_month = 12
date_day = 31

year = 2017
month = 12
starttime = 43100

file_name = 1

while(year!=2009):
	url = 'https://timesofindia.indiatimes.com/'+str(date_year)+'/'+str(date_month)+'/'+str(date_day)+'/archivelist/year-'+str(year)+',month-'+str(month)+',starttime-'+str(starttime)+'.cms'
	result = requests.get(url)
	soup = BeautifulSoup(result.text,"html.parser")
	spans = soup.find_all("span")
	path_name = os.path.join('Desktop/newslinks',str(file_name)+'.txt') #Path to save the file
	f = open(path_name,"w+")
	f.write(str(date_day)+'/'+str(date_month)+'/'+str(date_year)+"\n") #Writes the date of the article 
	for span in spans:
		links = span.find_all('a')
		for link in links: 				
			f.write(link['href']+"\n")
	f.close()
	file_name+=1
	
	#If the article date has reached 1st January decrement year by one and set date_day to 31 and date_month to 12
	if date_day==1 and date_month==1:
		year-=1
		date_year-=1
		date_day=31
		date_month=12
		month=12
		starttime-=1
	
	#Check for months having number of days ie (31 or 30 or 29 or 28)days
	if date_day==1: 
		if date_month==5 or date_month==7 or date_month==8 or date_month==10 or date_month==12:
			date_day=30
			date_month-=1
			month-=1
			starttime-=1
		
		elif date_month==2 or date_month==4 or date_month==6 or date_month==9 or date_month==11:
			date_day=31
			date_month-=1
			month-=1
			starttime-=1
			
		elif date_month==3: 
			if date_year!=2012 or date_year!=2016:
				date_day=28
				date_month-=1
				month-=1
				starttime-=1 
			
			elif date_year==2012 or date_year==2016:
				date_day=29
				date_month-=1
				month-=1
				starttime-=1
			
	else:
		date_day-=1
		starttime-=1
