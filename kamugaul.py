meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "'Rolling on the floor' tertawa terbahak bahak sampai jatuh ke lantai berguling",
            "SHEESH": "Rasa takjub dan kagum",
            "CREEPY": "Menakutkan, tidak menyenangkan",
            "AGGRO": "Seseorang yang agresif, marah"
            }
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Nggak ada")
