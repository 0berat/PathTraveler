import os
#dosya aktif oldugu anda yapilacak islemler.
path = os.getcwd()
print(path)
print(os.listdir(path)) #os.listdir() mevcud dizini listeler.   

def go_back(path): #bir ust dizine gitmeye yariyor.
  a = path.rfind("\\")
  new_path = path[0: a ]
  return new_path

#print(go_back(path))


while(True):
    choose = input("\nAlt dizine gecmek icin 'Dizin ismi'.\nUst dizine gecmek icin '..'.\nCikmak icin 'exit'.\n")

    if choose == "exit":
        break
    elif choose == "..":
        print("----------------")
        path = go_back(path)
        print(path)
        print(os.listdir(path)) 
    elif choose != "exit" and choose != "..": #bir alt dizine gitmek.
     path = path + "\\" + choose
     print("-------------------")
     print(os.listdir(path)) 
