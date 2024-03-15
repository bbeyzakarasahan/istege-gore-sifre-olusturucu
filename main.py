import random
import string


while True:
    password_len = int(input("Parolanız kaç basamaklı olsun? :"))
    if password_len==0 or password_len <=0:
        print("Parola uzunluğu 0 veya 0'dan küçük bir sayı olamaz.Lütfen tekrar deneyin.")
    elif password_len >=0:
        break
while True:
    password_count = int(input("Kaç adet parola oluşturulsun? :"))
    if password_count==0 or password_count <=0:
        print("Parola sayısı 0 veya 0'dan küçük bir sayı olamaz.Lütfen tekrar deneyin.")
    elif password_len >=0:
        break

numbers = string.digits
symbols = string.punctuation
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
all_characters = [numbers, symbols, lowercase_letters, uppercase_letters]


for i in range(password_count):
    password = ""
    while len(password) < password_len:
        character_set = random.choice(all_characters)
        password += random.choice(character_set)
    print(f"Random şifreniz: {password}")