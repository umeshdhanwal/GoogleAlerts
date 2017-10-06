# -*- coding: utf-8 -*-
"""
The Below code would output the Google Alerts feed to the dropbox specified
in the access token and it would generate pdf file for it in another folder

Refer to the Fourth line of the alert for identifying the location of the saved pdf file in the text file

Created on Fri Oct 30 09:05:15 2017

@author: Hsemu
"""

#Muting the warnings
import warnings
warnings.filterwarnings("ignore")

import feedparser
import os
import subprocess
import dropbox
import unicodedata
import datetime
from weasyprint import HTML, CSS
import re
import requests, lxml.html

'''Please put the URL feed of the Google alerts which you want to feed'''
#URL_feed='https://www.google.com/alerts/feeds/03052694921060148104/10484262279899711572' #Alert for Donald Trump
URL_feed='https://www.google.ie/alerts/feeds/06782147434896058293/17777381263490192727' #Alert for Ryan Air
#URL_feed='https://www.google.ie/alerts/feeds/06782147434896058293/861461405236497894'  #Alert for Las Vegas
#URL_feed='https://www.google.com/alerts/feeds/06782147434896058293/8909055318872650373' #Alert for Trump
#URL_feed='https://www.google.com/alerts/feeds/14273445301609542014/8457109545342134256' #Alert for Itishtimes opinion of Newton Emerson

'''Please provide the username and password for Irishtimes'''
user='a.m.connolly@idiro.com'
passwd='Umesh123'

'''Here input the values which needs to be created for the home directory'''
os.chdir('/home/umeshdhanwal/GoogleAlerts') #Input the local directory to be created for storing the alerts
repo_dir = 'GoogleAlerts' #Directory for defining the starting folder for parsing to dropbox
txt_alert_dir='News_Alerts' #input the name of directory for storing text file
pdf_alert_dir='News_Alerts_pdf' #input the name of directory for storing pdf file

'''Putting the Drop box access token for running'''
#access_token = 'o2HubcOnjaAAAAAAAACGENE_EX_fTQ2h4dErQe0yjEO6jfRgtSiLjfFi-SvmZ67N'
access_token = 'aYGqbBWFEzoAAAAAAAAADibvdDcTby6Pjgc8Bl4nZc4PASuecEG9isKWkWcd44o4'

#Login for the website
def loginsite(nameofsite,username,password):
    s = requests.session()
    details = {
    'signin__email': username,
    'signin__password': password
    }

    response = s.post(nameofsite, data=details)
    print "Logged in NewSite:",response.url
    return s

site=loginsite('https://www.irishtimes.com/',user,passwd)

#Replace string in text
def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

#Defining the time of txt file
now = datetime.datetime.now().strftime("%Y-%m-%d:%H:%M")

#Create Directory for the files:
def createdir(value):
   script_dir = os.path.dirname(os.path.abspath(__file__))
   dest_dir = os.path.join(script_dir, value)
   try:
      os.makedirs(dest_dir)
   except OSError:
      pass # already exists
   return dest_dir

dest_dir=createdir(txt_alert_dir)
dest_dir_pdf=createdir(pdf_alert_dir)

#Write to  txt files and then use it for conversion
NameofFile=repo_dir+'_'+now+'.txt'
print("The Name of alert file created just now:",NameofFile)

path = os.path.join(dest_dir, NameofFile)
file = open(path,"w")

if 'google' in URL_feed:
    URL_feed=URL_feed.replace('google.ie', 'google.com')

d = feedparser.parse(URL_feed)

#Defining the blank url for extracting urls
url=[]

#Text to remove from the extracted links
reps = {'<b>':'', '</b>':'','&nbsp;':''}

print ("Extracting the %s feeds............."%len(d.entries))

for i,e in enumerate(d.entries):
     try:
       file.write(replace_all(unicodedata.normalize('NFKD',e.title).encode('ascii','ignore'),reps)+"\n")
       file.write(unicodedata.normalize('NFKD',e.link).encode('ascii','ignore')+"\n")
       if "irishtimes" in unicodedata.normalize('NFKD',e.link).encode('ascii','ignore'):
           pdffilename=str(os.path.join(dest_dir_pdf,"%s_%s_irishtimes.pdf"%(now,i)))
       else:
           pdffilename=str(os.path.join(dest_dir_pdf,"%s_%s.pdf"%(now,i)))
       url.extend(re.findall('url="?\'?([^"\'&]*)',unicodedata.normalize('NFKD',e.link).encode('ascii','ignore') ))
       file.write(replace_all(unicodedata.normalize('NFKD',e.description).encode('ascii','ignore'),reps)+"\n")
       file.write("Location of file in PythonAnywhere:%s"%pdffilename+"\n")
       file.write("\n") # 2 newlines
     except:
         pass

file.close
file.flush()

#Trying to convert to pdf
print(url)
for i in range(len(url)):
    try:
       if "irishtimes" in url[i]:
             pdf = HTML(url[i]).write_pdf(stylesheets=[CSS(string='@page { size: 26.9cm 300cm; margin: 0in 0in 0in 0in};'
                 '@media print { nav { display: none; } }')])
             f=open(os.path.join(dest_dir_pdf,"%s_%s_irishtimes.pdf"%(now,i)),"w")
             f.write(pdf)
       else:
            pdf=HTML(url[i]).write_pdf()
            f=open(os.path.join(dest_dir_pdf,"%s_%s.pdf"%(now,i)),"w")
            f.write(pdf)
    except:
        pass

#Accesing the dropbox
dbx = dropbox.Dropbox(access_token)

print ("Attempting to upload...")
# walk return first the current folder that it walk, then tuples of dirs and files not "subdir, dirs, files"
def uploadfile(rootdir):
   for dir, dirs, files in os.walk(rootdir):
       for file in files:
          try:
             #file_path = os.path.join(dir, file)
             file_path = os.path.join(dir, file)
             dest_path = os.path.join('/'+repo_dir,rootdir,file)
             print('Uploading %s to %s' % (file_path, dest_path))
             with open(file_path,'r') as f:
                dbx.files_upload(f.read(), dest_path, mode=dropbox.files.WriteMode.overwrite)
          except Exception as err:
             print("Failed to upload %s\n%s" % (file, err))

#Uploading the files
uploadfile(pdf_alert_dir)
uploadfile(txt_alert_dir)

print("Finished upload.")
