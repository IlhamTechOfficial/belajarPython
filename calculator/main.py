from calculatorLibrary import CalculatorLibrary


def main():

    while True:
        print("Pilih operasi yang ada:")
        print("1. tambah")
        print("2. tolak")
        print("3. darab")
        print("4. bahagi")
        print("5. modulo")
        pilihan = input('Pilihan operasi: ')
        if pilihan in ('1', '2', '3', '4', '5'):
            nom_1 = float(input("masukkan nombor pertama: "))
            nom_2 = float(input("masukkan nombor kedua: "))

            if pilihan == '1':
                print(nom_1, '+', nom_2, '=', CalculatorLibrary().tambah(nom_1, nom_2))
            elif pilihan == '2':
                print(nom_1, '-', nom_2, '=', CalculatorLibrary().tolak(nom_1, nom_2))
            elif pilihan == '3':
                print(nom_1, '*', nom_2, '=', CalculatorLibrary().darab(nom_1, nom_2))
            elif pilihan == '4':
                print(nom_1, '/', nom_2, '=', CalculatorLibrary().bahagi(nom_1, nom_2))
            elif pilihan == '5':
                print(nom_1, '%', nom_2, '=', CalculatorLibrary().modulo(nom_1, nom_2))
            else:
                print("Pilihan operasi yang salah!")
            # break
        else:
            print("Pilihan operasi yang salah!")

    # print("print", CalculatorLibrary().tambah(2, 4))
    print("END")

if __name__ == '__main__':
    main()