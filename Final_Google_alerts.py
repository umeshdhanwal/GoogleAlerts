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

##Pull the latest file from git
print subprocess.check_output('git stash', shell=True)
print subprocess.check_output('git pull origin master', shell=True)

repo_dir = 'GoogleAlerts'
URL_feed='https://www.google.com/alerts/feeds/03052694921060148104/10484262279899711572'

d = feedparser.parse(URL_feed)

#Write to  txt files and then use it for conversion 

file = open("testfile.txt","w") 

for e in d.entries:
     file.write(e.title+"\n")
     file.write(e.link+"\n")
     #file.write(str(e.description))
     file.write("\n") # 2 newlines

file.close

#Drop box keys     
app_key = 'ez341m6npdgliwh'
app_secret = 'aYGqbBWFEzoAAAAAAAAADibvdDcTby6Pjgc8Bl4nZc4PASuecEG9isKWkWcd44o4'

dbx = dropbox.Dropbox(app_secret)

with open('testfile.txt') as f:
    dbx.files_upload(f, dest_path, mute=True)

print(dbx.files_get_metadata('/story.txt').server_modified)
