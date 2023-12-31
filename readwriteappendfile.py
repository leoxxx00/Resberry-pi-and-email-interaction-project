#want to read a file but make sure the file exit
import os
if os.path.exists("/home/pi/Documents/Test/text_file"):
    print("File exits")
    os.remove("/home/pi/Documents/Test/text_file")#remove a file
#read file
#with open("/home/pi/Documents/Test/text_file","r") as f:
    #print(f.read())
    #for line in f:
        #print(line)
        
#write a file
#with open("/home/pi/Documents/Test/text_file","w") as f:
#    f.write("new text\n")
    
#append a file
#with open("/home/pi/Documents/Test/text_file","a") as f:
#    f.write("new text\n")




