matn = "Python dasturlash qiziqarli. Python imkoniyatlari keng."

toza_matn = matn.replace(".", "").replace(",", "")
sozlar = toza_matn.split()

eng_uzun_soz = max(sozlar, key=len)
harflar = [harf for harf in matn.lower() if harf.isalpha()]
eng_kop_harf = max(harflar, key=harflar.count)

kichik_sozlar = [s.lower() for s in sozlar]
takrorlanmaydigan = [s for s in sozlar if kichik_sozlar.count(s.lower()) == 1]

print("Sozlar soni:", len(sozlar))
print("Eng uzun soz:", eng_uzun_soz)
print("Eng kop uchragan harf:", eng_kop_harf)
print("Takrorlanmaydigan sozlar:", ", ".join(takrorlanmaydigan))

