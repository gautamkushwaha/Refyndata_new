#python program to merge two mails
# names are in the names.txt and 
# body of the mail is in the body.txt file

#open names.txt for opening
with open("names.txt", 'r') as names_files:
    with open("body.txt", 'r') as body_files:
        
        # read body of the email ferom the body fiels
        body = body_files.read()
        
        # iterate over names
        for name in names_files:
           mail = "Hello" + name.strip() + "\n" + body
           
           
           # write the eamil to individual files
           with open(name.strip()+ ".txt","w") as mail_file:
               mail_file.write(mail)