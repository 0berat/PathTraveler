import os #

#def list_files(startpath):
#    for root, dirs, files in os.walk(startpath):
#        level = root.replace(startpath, '').count(os.sep)
#        indent = ' ' * 4 * (level)
#        print('{}{}/'.format(indent, os.path.basename(root)))
#        subindent = ' ' * 4 * (level + 1)
#        for f in files:
#            print('{}{}'.format(subindent, f))


def list_files(startpath):#dizinleri listelemek icin kullanilan fonksiyon
    for entry in os.scandir(startpath):
        if entry.is_file():
            print(entry.name)
        elif entry.is_dir():
            print(entry.name)            

def go_back(path): #sanirim dizinler arasinda gezinmek icin kullanilacak fonksiyon
 a = path.rfind("/")
 new_path = path[0: a ]
 return new_path
 

# path = "C:/Users/RAKI/Desktop/server"
path = os.getcwd() #otomatik olarak dosyanin bulundugu konumu path degiskenine kaydeder.


list_files(path)

while(True):
    choose = input()

    if choose == "exit":
        break
    elif choose == "..":
        print("----------------")
        path = go_back(path)
        list_files(path)
    elif choose != "exit" and choose != "..":
     path = path + "/" + choose
     print("-------------------")
     list_files(path)
