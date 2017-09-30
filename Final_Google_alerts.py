# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 09:05:15 2017

@author: Hsemu
"""

#from git import Repo
import feedparser
#import git
import os
import subprocess
import dropbox
import unicodedata
import datetime

now = datetime.datetime.now()
now=now.strftime("%Y-%m-%d:%H:%M")

##Pull the latest file from git
print subprocess.check_output('git stash', shell=True)
print subprocess.check_output('git pull origin master', shell=True)

repo_dir = 'GoogleAlerts'
URL_feed='https://www.google.com/alerts/feeds/03052694921060148104/10484262279899711572'

d = feedparser.parse(URL_feed)

#Write to  txt files and then use it for conversion 
NameofFile='Google_Alerts_'+now+'.txt'
print("The startingName:",NameofFile)

file = open(NameofFile,"w") 

for e in d.entries:
     try:
       file.write(unicodedata.normalize('NFKD',e.title).encode('ascii','ignore')+"\n")
       file.write(unicodedata.normalize('NFKD',e.link).encode('ascii','ignore')+"\n")
       file.write(unicodedata.normalize('NFKD',e.description).encode('ascii','ignore')+"\n")
       file.write("\n") # 2 newlines
     except:
       pass

file.close

#Drop box keys     
app_key = 'ez341m6npdgliwh'
app_secret = 'aYGqbBWFEzoAAAAAAAAADibvdDcTby6Pjgc8Bl4nZc4PASuecEG9isKWkWcd44o4'

dbx = dropbox.Dropbox(app_secret)

print(os.getcwd())

filetocopy=open(NameofFile,'r')
print("The copiedName:",NameofFile)
data = filetocopy.read()      # copy to a string
print(data)

dbx.files_upload('This is the one I was talking', '/'+NameofFile, mute=True)
print(dbx.files_get_metadata( '/'+NameofFile).server_modified)
filetocopy.close()
