# def hasil_tambah(nombor_1, nombor_2):
#     return nombor_1 + nombor_2

# print(hasil_tambah(10, 6))

# import dummy

# def lukis_piramid_90():
#     print("|")
#     print("|", "\\")
#     print("|", " \\")
#     print("|", "  \\")
#     print("|", "   \\")
#     print("|", "    \\")


# if __name__ == '__main__':
#     lukis_piramid_90()
#     dummy.lukis_piramid_90_star()

# import dummy

from dummy import SimbolUntukPiramid

def pyramid():
    symbol = SimbolUntukPiramid().dapatkan_simbol()
    print(symbol)
    print(symbol, symbol)
    print(symbol, " "+symbol)
    print(symbol, "  "+symbol)
    print(symbol, "   "+symbol)
    print(symbol, "    "+symbol)


if __name__ == '__main__':
    pyramid()
