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
from weasyprint import HTML, CSS


#Defining the time of txt file
now = datetime.datetime.now().strftime("%Y-%m-%d:%H:%M")


##Pull the latest file from git
#subprocess.check_output('git reset --hard', shell=True)
#subprocess.check_output('git clean -df', shell=True)
#subprocess.check_output('git stash', shell=True)
#subprocess.check_output('git pull origin master', shell=True)

repo_dir = 'GoogleAlerts'
#URL_feed='https://www.google.com/alerts/feeds/03052694921060148104/10484262279899711572'
URL_feed='https://www.google.ie/alerts/feeds/06782147434896058293/17777381263490192727'
#URL_feed='https://www.google.ie/alerts/feeds/06782147434896058293/861461405236497894'
#URL_feed='https://www.google.com/alerts/feeds/06782147434896058293/8909055318872650373'

if 'google' in URL_feed:
    URL_feed=URL_feed.replace('google.ie', 'google.com')

d = feedparser.parse(URL_feed)

#Trying to convert to pdf
url='https://www.irishtimes.com/news/politics/liam-cosgrave-former-taoiseach-and-fine-gael-leader-dies-aged-97-1.3244509'

if "irishtimes" in url:
   pdf = HTML(url).write_pdf('google.pdf',stylesheets=[CSS(string='@page { size: 26.9cm 300cm; margin: 0in 0in 0in 0in};'
           '@media print { nav { display: none; } }')])
else:
    pdf=HTML(url).write_pdf('google.pdf')


#pdf = HTML(url).write_pdf('google.pdf',stylesheets=[CSS(string='@page {size: 27cm 300cm;margin: 0in 0.44in 0.2in 0.44in;}')])
#open('google.pdf', 'w').write(pdf)
#print(url.text)


#Create Directory for the files:
def createdir(value):
   script_dir = os.path.dirname(os.path.abspath(__file__))
   dest_dir = os.path.join(script_dir, value)
   try:
      os.makedirs(dest_dir)
   except OSError:
      pass # already exists
   return dest_dir

dest_dir=createdir('News_Alerts')

#Write to  txt files and then use it for conversion
NameofFile='Google_Alerts_'+now+'.txt'
print("The startingName:",NameofFile)

os.chdir('/home/umeshdhanwal/GoogleAlerts')

path = os.path.join(dest_dir, NameofFile)
file = open(path,"w")

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
#access_token = 'o2HubcOnjaAAAAAAAACGENE_EX_fTQ2h4dErQe0yjEO6jfRgtSiLjfFi-SvmZ67N'
access_token = 'aYGqbBWFEzoAAAAAAAAADibvdDcTby6Pjgc8Bl4nZc4PASuecEG9isKWkWcd44o4'

dbx = dropbox.Dropbox(access_token)
rootdir = 'News_Alerts'

print ("Attempting to upload...")
# walk return first the current folder that it walk, then tuples of dirs and files not "subdir, dirs, files"
def uploadfile(rootdir):
   for dir, dirs, files in os.walk(rootdir):
       for file in files:
          try:
             #file_path = os.path.join(dir, file)
             file_path = os.path.join(dir, file)
             dest_path = os.path.join('/GoogleAlerts',rootdir,file)
             print('Uploading %s to %s' % (file_path, dest_path))
             with open(file_path,'r') as f:
                dbx.files_upload(f.read(), dest_path, mute=True)
          except Exception as err:
             print("Failed to upload %s\n%s" % (file, err))

#Uploading the files
uploadfile(rootdir)
print("Finished upload.")
