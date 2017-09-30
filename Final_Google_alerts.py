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
access_token = 'aYGqbBWFEzoAAAAAAAAADibvdDcTby6Pjgc8Bl4nZc4PASuecEG9isKWkWcd44o4'

dbx = dropbox.Dropbox(access_token)

def upload_file(self, file_from, file_to):
"""upload a file to Dropbox using API v2
 """
        dbx = dropbox.Dropbox(self.access_token)
             with open(file_from, 'rb') as f:
                 dbx.files_upload(f.read(), file_to)
         
print("The copiedName:",NameofFile)

file_from=NameofFile
file_to='/'+NameofFile

upload_file(file_from, file_to)
print(dbx.files_get_metadata( '/'+NameofFile).server_modified)
filetocopy.close()
