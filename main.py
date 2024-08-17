from gtts import gTTS
import os
import time
from requests.exceptions import ConnectionError

texts = ["der","die","das","und","sein","in","zu","haben","ich","werden","Sie","von","nicht","mit","es","sich","auf","dass","für","an","er","so","eine","auch","als","bei","aber","nach","wie","im","man","nur","noch","müssen","über","sagen","wollen","vor","aus","durch","all","wenn","gehen","schon","mehr","bis","wissen","Jahr","viel","gut","geben","hier","dies","jetzt","mein","doch","groß","kommen","können","wollen","Mensch","machen","Zeit","lassen","darüber","auch","gehen","Tag","Haus","Frau","Mann","immer","warum","ohne","weg","Stadt","das","Schule","Jahr","fahren","schnell","noch","Kinder","diese","dort","wie","Arbeit","brauchen","viele","Leute","Problem","leben","glauben","bisschen","gut","sagen","wollen","hier","dafür","immer","vielleicht","Kind","unser","wir","machen","dieser","wieder","dass","neu","Tag","sprechen","sollen","Mann","Frau","Welt","Abend","Land","Herr","leben","wenig","Jahr","unter","Auge","Nacht","jeder","nächst","einzig","erzählen","endlich","Name","Woche","gern","laut","einfach","recht","klar","Seite","hören","genug","daher","gar","fühlen","niemand","denken","trinken","Stunde","Art","Wasser","bleiben","leicht"]
def save_tts(text, lang='de', slow=False, retries=3, delay=2):
    for attempt in range(retries):
        try:
            tts = gTTS(text=text, lang=lang, slow=slow)
            ses_dosyasi = "de\\" + text + ".mp3"
            tts.save(ses_dosyasi)
            print(f"{ses_dosyasi} başarıyla oluşturuldu")
            break
        except ConnectionError as e:
            print(f"Bağlantı hatası: {e}. {attempt + 1}. deneme başarısız. Yeniden denenecek...")
            time.sleep(delay)
        except Exception as e:
            print(f"Başka bir hata oluştu: {e}")
            break

for metin in texts:
    save_tts(metin)