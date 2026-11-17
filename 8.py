fayllar = ["Hisobot 2026.pdf", "profil rasmi.jpg",
           "video.mp4", "jadval.xlsx", "diagramma.png"]
ruxsat_etilgan = (".pdf", ".jpg", ".png")

yaroqli = []
yaroqsiz = []

for fayl in fayllar:
    if fayl.lower().endswith(ruxsat_etilgan):
        yangi_nom = fayl.replace(" ", "_")
        yaroqli.append(yangi_nom)
    else:
        yaroqsiz.append(fayl)

print("Yaroqli:", " ".join(yaroqli))
print("Yaroqsiz:", " ".join(yaroqsiz))
