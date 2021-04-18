# def lukis_piramid_90_star():
#     print("*")
#     print("*", "*")
#     print("*", " *")
#     print("*", "  *")
#     print("*", "   *")
#     print("*", "    *")


# if __name__ == '__main__':
#     lukis_piramid_90_star()


class SimbolUntukPiramid:

    def __init__(self):
        self.simbol = ""
        # self.simbol = input("Masukkan symbol yang nak digunakan: ")
        print("")

    def dapatkan_simbol(self, simbol='%'):
        self.simbol = simbol
        return self.simbol
