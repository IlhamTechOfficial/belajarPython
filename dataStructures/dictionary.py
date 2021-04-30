def main():

    dict_buffer = {
        "Nama": "Night Owl",
        "NamaBapa": "Darkness",
        "Bekerja": True, 
        "Birthday": [2021, 4,30, 23, 59],
        "DateCategory": ('Year', 'Month', 'Day', 'Hour', 'Minute'),
        "Asal": {
            "Negara": "Malaysia",
            "Negeri": "Putrajaya",
            "Alamat": "IOI Conezion"
        }
    }

    # Dapatkan data type
    print(type(dict_buffer))

    # Dapatkan length of data
    print(len(dict_buffer))

    # Dapatkan value daripada dict key
    print(dict_buffer['Asal']['Negara'])

    # Dapatkan semua keys
    print(dict_buffer.keys())

    # Dapatkan semua values
    print(dict_buffer.values())

    # Dapatkan semua items (Keys dan values)
    print(dict_buffer.items()) # bagi result sebagai tuples dalam list

    # Tukar value dalam dictionary
    dict_buffer['Nama'] = "Morning Lark"
    dict_buffer.update({'Nama': 'Morning Lark'})
    print(dict_buffer)

    # Tambah value baru dalam dictionary
    dict_buffer['Single'] = True
    dict_buffer.update({'Single': 'True'})
    print(dict_buffer)

    # Buang value dalam dictionary
    dict_buffer.pop("Nama")
    del dict_buffer["Nama"]
    print(dict_buffer)


    # Copy dictionary
    dict_buffer_2 = dict_buffer.copy()
    print(dict_buffer_2)
    del dict_buffer["Nama"]
    print(dict_buffer_2)

    # Semak jika key ada dalam dictionary
    if "NamaBapa" in dict_buffer:
        print("Yes NamaBapa ada sebenarnya")

    # Dictionary tak boleh exist dengan key yang sama
    new_buffer = {
        "Nama": "Night Owl",
        "Nama": "Morning Lark"
    }
    print(new_buffer)


    # Kosongkan dictionary
    dict_buffer.clear()
    print(dict_buffer)

    # Delete dictionary
    del dict_buffer
    print(dict_buffer)

    print("END")


if __name__ == '__main__':
    main()