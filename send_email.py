import yagmail

password=""

with open("/home/pi/.local/share/.email_password","r") as f:
    password=f.read()

yag = yagmail.SMTP('resberrypi@gmail.com',password)

yag.send(to='leoxxx00@gmail.com',
         subject="first email",
         contents="IOT, AI and Cyber with Ethical hacking skills are coming",
         attachments="/home/pi/file_to_join.txt")
print("Email sent")