import sys
import glob
import os.path

def scriptFile():
    
    options = {
            '1' : list,
            '2' : write,
            '3' : display,
            '4' : excecute,            
            'b' : back
        }
    
    choice_text = '''
[script file] enter your choice:
 1. list existing files
 2. write a script file
 3. display a script file
 4. excecute a script file
 b. back
> '''
    while True:
       choice = input(choice_text)
       if choice in options:
           if choice == 'b':
               break
           else :
               options[choice]()
       else:
           print ('Option unavailable\n')  
           
#list existing files
def list():
    #print('\n list goes here ')
    print ("list of files in '../faly_files/script/' : ")
    for nomfich in glob.glob("../faly_files/script/*.*"):
        nomfich = nomfich.split("\\")
        print (nomfich[1])
#FIN list existing files       
                 
#write a script file
def write():
    #print('\n### write goes here ###')
    line=''
    prg=''
    fileName = input("File name?:")
    print("'wx' : to save the file."
          +"\n 'q' : to quit without saving the file.")
    while True:
        line = input("line to write in the file :")
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
    if os.path.isfile("../faly_files/script/" + fileName):
        overwrite = input("The file exists already, overwrite it? [Y/N]:")
        if overwrite.lower()=='y':
            try:
                file = open("../faly_files\/script\/"+fileName, "w")
                file.write(prg)
                file.close
                print("file saved")
            except:
                print("Unexpected error:", sys.exc_info()[0]) 
        else:
            print("file not saved!")
    else:
        file = open("../faly_files/script/"+fileName, "w")
        file.write(prg)
        file.close
        print("file saved")        
              
#FIN write a script file    
    
#display a script file
def display():
    path = input('Which file to display? :')
    path = "../faly_files/script/"+path
    try:
        file = open(path, "r")
           # go through the lines and treat them
        print("contents of "
              +path+
              "\n ----------------------------------------------------")
        for ligne in file:
            print(ligne)   
        file.close()
        print("----------------------------------------------------")
    except FileNotFoundError:
        print("File not found!")
    except:
        print("Unexpected error:", sys.exc_info()[0])
#FIN display a script file                    
    
def excecute():
    #print('\n### excecute goes here ###')
    path = input('Which file to run? :')
    path = "../faly_files/script/"+path
    try:
        file = open(path, "r")
           # go through the lines and treat them
        for ligne in file:
            print(ligne)#######################################################   
        file.close()        
    except FileNotFoundError:
        print("File not found!")
    except:
        print("Unexpected error:", sys.exc_info()[0])    
     
    
def back():
    print('\ngo back\n')       
    
                