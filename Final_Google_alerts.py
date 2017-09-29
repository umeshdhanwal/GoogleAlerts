from git import Repo
import feedparser
import subprocess

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

#Reading the Pdf already stored on local drive and
#then reading it for writing
print subprocess.check_output('git add testfile.txt', shell=True)
print subprocess.check_output('git commit -m "This is test file"', shell=True)
#print subprocess.check_output('git push origin master', shell=True)
#print subprocess.check_output('git init', shell=True)
#print subprocess.check_output('git commit', shell=True) 
