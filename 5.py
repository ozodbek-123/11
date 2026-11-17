tadbir_1 = {"Ali", "Vali", "Sami", "Lola"}
tadbir_2 = {"Ali", "Sami", "Nodir"}
tadbir_3 = {"Ali", "Lola", "Nodir"}

barchasida = tadbir_1 & tadbir_2 & tadbir_3
kamida_ikkitasida = (tadbir_1 & tadbir_2) | (tadbir_1 & tadbir_3) | (tadbir_2 & tadbir_3)
barcha_ishtirokchilar = tadbir_1 | tadbir_2 | tadbir_3
faqat_bittasida = barcha_ishtirokchilar - kamida_ikkitasida

print("Barcha tadbirlarda:", ", ".join(barchasida))
print("Faqat bitta tadbirda:", ", ".join(faqat_bittasida))
print("Kamida ikkita tadbirda:", ", ".join(kamida_ikkitasida))
