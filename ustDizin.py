import os

# cikti = input("degisken degeri girinizi\n")
# print(cikti)
path = "C:\\Users\\berat\\Desktop\\recai"

def go_back(): #bir ust dizine gitmeye yariyor.
  a = path.rfind("\\")
  new_path = path[0: a ]
  return new_path

print(go_back())
 
# def selamla():
#     a= "zort"
#     return a
# print(selamla())