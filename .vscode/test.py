from os import read
from speachrec import Take
from speachrec import speak
from os import path
import os



f=open("notes.txt","a+")

print('''\nwhat do you want to do: 
-add a new file
-append
-read
-delete file
-deleted last line

ans:
''')
speak('''\nwhat do you want to do,
-add a new file
-append
-read
-delete file
-delete last line

''')


query=Take().lower()
def file_han(query):
    
    if "new file"in query:
        c1=name=input("what should I name the file?")
        if path.isfile(f'./{c1}.txt'):
            print("\n file already exists")
            
        else:
            nfile=open(name+".txt","a+")
            print("what should I add to this note:\n")
            nfile.write(input()+"\n")
            nfile.close()
            
    if "append in file" in query or "append file" in query:
        n=input("\nif which file should I append: ")
        if path.isfile(f'./{n}.txt')==False:
            print("\n file does not exists")
        else:
            b=open(f"{n}.txt","a")
            b.write(input("\nwhat should I add\n")+"\n")
            print("\nyour final file is:-\n")
            b=open("notes.txt")
            print(b.read())
            b.close()
        
    elif "read file"==query:
        c=input("\nwhat file would you like me to read?:")
        if path.isfile(f'./{c}.txt'):
            v=open(c+".txt", "r")
            print(v.read())
            v.close()
            
        else :
            print("\nno such file exists")
            
    elif "delete last line"in query:
        n1=input("what file would you like to delete the last line from")
        if path.isfile(f'./{n1}.txt')==False:
            print("\n file does not exists")
        else:
            a=open(f"{n1}.txt","a+")
            d=a.read()
            m=d.split("\n")
            s="\n".join(m[:-1])
            print(s)
            ad=open("notes.txt","w+")
            for i in range(len(s)):
                ad.write(s[i])
            ad.close()
            a.close()
        
    elif "delete file" in query:
        name=input("what file would you like me to delete:-")
        if path.isfile(f'./{name}.txt')==False:
            print("\n file dose not exists")
            
        else:
            os.remove(f"{name}.txt")
    else:
        print("no such command")
        
file_han(query)
    

