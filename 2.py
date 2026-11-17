buyurtmalar = [
    {"mahsulot": "Kitob", "narx": 45000, "miqdor": 2},
    {"mahsulot": "Ruchka", "narx": 5000, "miqdor": 10},
    {"mahsulot": "Sumka", "narx": 180000, "miqdor": 1},
]

eng_qimmat_nomi = ""
eng_qimmat_qiymat = 0

for item in buyurtmalar:
    qiymat = item["narx"] * item["miqdor"]
    print(f"{item['mahsulot']}: {qiymat} som")

    if qiymat > eng_qimmat_qiymat:
        eng_qimmat_qiymat = qiymat
        eng_qimmat_nomi = item["mahsulot"]

print(f"Eng qimmat buyurtma: {eng_qimmat_nomi} — {eng_qimmat_qiymat} som")
