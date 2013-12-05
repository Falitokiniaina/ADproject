import sys
import glob
import os.path

           
#list existing files
def listScript():
    #print('\n list goes here ')
    print ("List of files in 'script_files' folder: ")
    for nomfich in glob.glob("script_files/*.*"):
        nomfich = nomfich.split("\\")
        print (nomfich[1])
#FIN list existing files       
                 
   
                 
#write a script file
def writeScript():
    #print('\n### write goes here ###')
    line=''
    prg=''
    fileName = input("Enter new file name\n> ")
    print("'wx' : to save the file."
          +"\n 'q' : to quit without saving the file.")
    while True:
        line = input("line to write in the file:")
        if line == "wx":
            writeFile(fileName,prg)                        
            break
        else:
            if line == "q":
                break
            else:
                prg = prg + line + "\n"    

def writeFile(fileName,prg):
    print("saving file")
    #check if the file exists already
    if os.path.isfile("script_files/" + fileName):
        overwrite = input("The file exists already, overwrite it? [Y/N]:")
        if overwrite.lower()=='y':
            try:
                file = open("script_files/"+fileName, "w")
                file.write(prg)
                file.close
                print("file saved")
            except:
                print("Unexpected error:", sys.exc_info()[0]) 
        else:
            print("file not saved!")
    else:
        file = open("script_files/"+fileName, "w")
        file.write(prg)
        file.close
        print("file saved")        
              
#FIN write a script file    
    
    
    
#display a script file
def displayScript():
    path = input('Enter file to display\n> ')
    path = "script_files/"+path
    try:
        file = open(path, "r")
           # go through the lines and treat them
        print("Contents of '"
              +path+
              "'\n----------------------------------------------------")
        for ligne in file:
            print(ligne)   
        file.close()
        print("----------------------------------------------------")
    except FileNotFoundError:
        print("File not found!")
    except:
        print("Unexpected error:", sys.exc_info()[0])
#FIN display a script file                    
                