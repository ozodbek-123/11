natijalar = [
    {"ism": "Aziza", "ball": 82},
    {"ism": "Jasur", "ball": 64},
    {"ism": "Madina", "ball": 91},
    {"ism": "Sardor", "ball": 70}
]

yuqori = list(filter(lambda x: x["ball"] > 70, natijalar))

oshirilgan = list(map(lambda x: round(x["ball"] * 1.1, 1), natijalar))

saralangan = sorted(natijalar, key=lambda x: x["ball"], reverse=True)

print("70 dan yuqori:", ", ".join(x["ism"] for x in yuqori))
print("10% oshirilgan ballar:", oshirilgan)
print("Saralangan:", ", ".join(x["ism"] for x in saralangan))
