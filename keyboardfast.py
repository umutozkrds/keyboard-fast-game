import time
import random

while True:
    diff = input('''       Kolay için -> k
                 Zor için -> z
                 Oyundan çıkmak için -> q
                 ''')
    if diff != "q":
        start_time = time.time()
        if diff == "k":
            words = ["kalem", "masa", "sandalye", "bilgisayar", "kitap", "telefon", "kamera", "fare", "kulaklık", "hoparlör"]
        elif diff == "z":
            words = ["kahvaltı", "merhaba", "güneş", "kitaplık", "meyve", "yazılım", "kırmızı", "meydan", "anlamak", "öğrenci", "özgürlük", "bilgisayar", "mutluluk", "deniz", "çiçek", "havuz", "köprü", "orman", "aile", "yemek"]
            
        random.shuffle(words)
        
        for word in words:
            while True:
                enter = input(f"{word}:")
                if enter == word:
                    break
        
        end_time = time.time()
        print("Oyun süresi:", end_time - start_time, "saniye")
        
        devam = input("Baştan başlamak ister misiniz? (E/H): ")
        if devam.upper() != "E":
            break
        
    else: 
        break
