import dropbox, sys, os

dbx = dropbox.Dropbox('aYGqbBWFEzoAAAAAAAAADibvdDcTby6Pjgc8Bl4nZc4PASuecEG9isKWkWcd44o4')
rootdir = 'News_Alerts' 

print ("Attempting to upload...")
# walk return first the current folder that it walk, then tuples of dirs and files not "subdir, dirs, files"
for dir, dirs, files in os.walk(rootdir):
    for file in files:
        try:
            #file_path = os.path.join(dir, file)
            file_path = os.path.join(dir, file)
            dest_path = os.path.join('/GoogleAlerts', file)
            print 'Uploading %s to %s' % (file_path, dest_path)
            with open(file_path,'r') as f:
                dbx.files_upload(f.read(), dest_path, mute=True)
        except Exception as err:
            print("Failed to upload %s\n%s" % (file, err))

print("Finished upload.")
