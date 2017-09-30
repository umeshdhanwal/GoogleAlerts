import feedparser
#import git
import os
#import subprocess
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

f = open('testfile.txt', 'rb')
response = client.put_file('/magnum-opus.txt', f)
print "uploaded:", response

#Reading the Pdf already stored on local drive and
#then reading it for writing

#print subprocess.check_output('git add .', shell=True)
#print subprocess.check_output('git commit -m "This"', shell=True)
#print subprocess.check_output('git push origin master', shell=True)
#print subprocess.check_output('git init', shell=True)
#print subprocess.check_output('git commit', shell=True) 
