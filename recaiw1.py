import os





#      1-) mevcud dizini listelemek ve kaydetmek.


#path = "C:\\Users\\berat\\Desktop\\recai" #double backslash sebebi escape islmini iptal etmek.
path = os.getcwd()
print(path)
print(os.listdir(path)) #os.listdir() mevcud dizini listeler.   


# 2-) bir ust dizine gitmek

# 3-) bir alt dizine gitmek
#ilk asama amele yoluyla test ediliyor. sonrasinda  cd komutu gibi yapmaya calisicam.
path = input("gitmek istediginiz dizini giriniz.\n")
# C:\\Users\\berat\\Desktop
os.chdir(path) #os.chdir() girilen dizine gider.

print(path)
print(os.listdir(path))


def go_back(path): #sanirim dizinler arasinda gezinmek icin kullanilacak fonksiyon
 a = path.rfind("/")
 new_path = path[0: a ]
 return new_path





"""
Temel islevler ;

1-) mevcud dizini listelemek ve kaydetmek.
2-) bir ust dizine gitmek
3-) bir alt dizine gitmek
4-) seçilen dosyanın yolunu aktarım yapan fonksiyona gönderme
5-) dosya ve klosoleri renk olarak bir birinden ayir.

NOT:
dizin degistirildiginde bu islevi gerceklestirmek gerek. Mevcud dizin kontrolu saglanir.


"""