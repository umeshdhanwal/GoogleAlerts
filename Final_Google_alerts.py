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

app_key = 'ez341m6npdgliwh'
app_secret = 'aYGqbBWFEzoAAAAAAAAADibvdDcTby6Pjgc8Bl4nZc4PASuecEG9isKWkWcd44o4'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
authorize_url = flow.start()

# Have the user sign in and authorize this token
authorize_url = flow.start()
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
code = raw_input("Enter the authorization code here: ").strip()

# This will fail if the user enters an invalid authorization code
access_token, user_id = flow.finish(code)

client = dropbox.client.DropboxClient(access_token)
print 'linked account: ', client.account_info()



f = open('testfile.txt', 'rb')
response = client.put_file('/magnum-opus.txt', f)
print "uploaded:", response
