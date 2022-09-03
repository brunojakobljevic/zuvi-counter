import re

pozdrav_brate = """Pozdrav brate, pozdrav brate, pozdrav brate
Pozdrav brate, pozdrav brate, pozdravljam te
Pozdrav brate, pozdrav brate, pozdrav brate
Pozdrav' oca, brata, sestru, pozdrav' mater
Čaša vode, kečap kruh, pozdrav brate, pozdrav brate
Namaz, dvopek, ćevap, luk, pozdrav brate, pozdrav brate
Zobene i voćni sok, pozdrav brate, pozdrav brate
FonTele, TikTok, pozdrav brate, pozdrav brate
Rizi bizi brate, zvizni viski brate
(Di si, s kim si brate)
Klizim niz klis brate zamisli ti si, brate
Zamisli nisi brate
Idi krispi jate i ne pizdi brate
U bus bez karte brate
Ponesi baklje brate el komandante, brate
Znaš me, znam te brate
Na te mudante, brate brate pujanke brate
Brate nema te brate brate jeba te brate
Splitska narav, dvista mana, bistra glava (bistra glava)
Sir salama, split banana nisam gladan (nisam gladan)
Brate svakog dana brate panorama jana brate
Ajde vamo s nama brate
Samo zdrava hrana
Fini maniri brate, niš' ti ne brini brate
Zimi eskimi brate liti picigin brate
Zdrav život zdrav duh
Daj rižot, daj luk, daj biškot, daj kruh, daj vino, daj šut
Voće, povrće, krumpiri, proteini, vitamini
Mi pingvini na sparini split, Karibi i Maldivi
A na rivi motorini
Berekini i dupini, u krivini Filipini
Briljantini cukarini
Avokado brate, samo hrabro brate
Cakum pakum brate, lako tako brate
Razbija si prozor brate šta'š učinit brate
Nemoj zvat mater, zovi Žuvija brate
Čaša vode, kečap kruh, pozdrav brate, pozdrav brate
Namaz, dvopek, ćevap, luk, pozdrav brate, pozdrav brate
Zobene i voćni sok, pozdrav brate, pozdrav brate
FonTele, TikTok, pozdrav brate, pozdrav brate
Pozdrav brate, pozdrav brate, pozdrav brate
Pozdrav brate, pozdrav brate, pozdravljam te
Pozdrav brate, pozdrav brate, pozdrav brate
Pozdrav' oca, brata, sestru, pozdrav' mater"""


brate_counter = len(re.findall("[bB]rat[ae\n ]", pozdrav_brate))

print(brate_counter)