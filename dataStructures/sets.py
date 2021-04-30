def main():
    
    contoh_set = {"Merah", "Jingga", "Kuning", "Hijau", "Biru", "Indigo", "Ungu"}
    print(len(contoh_set))
    print(type(contoh_set))


    # nak akses item dalam set
    for item in contoh_set:
        print(item)


    # tambah item dalam set
    contoh_set.add("Pink")
    print(contoh_set)


    # kembalikan set dengan element kedua-duanya
    contoh_set_2 = {"Hitam", "Putih"}
    contoh_set.update(contoh_set_2)
    print(contoh_set_2)
    print(contoh_set)


    # buang item dalam set (akan keluar error kalau item tak wujud)
    contoh_set.remove("Merah")
    print(contoh_set)


    # buang item dalam set (takkan keluar error kalau item tak wujud)
    contoh_set.discard("Merah")
    print(contoh_set)


    # buang item (set ialah tidak tersusun jadi akan random)
    contoh_set.pop()
    print(contoh_set)


    # clear-kan/kosongkan item dalam set
    contoh_set.clear()
    print(contoh_set)


    # delete set
    del contoh_set
    print(contoh_set)


    # kembalikan set yang baru dengan element kedua-dua set
    contoh_set = {"Merah", "Jingga", "Kuning", "Hijau", "Biru", "Indigo", "Ungu"}
    contoh_set_2 = {"Hitam", "Putih", "Merah"}
    result = contoh_set.union(contoh_set_2)
    print(result)


    # kembalikan set dengan element yang sama dari kedua-dua set
    contoh_set = {"Merah", "Jingga", "Kuning", "Hijau", "Biru", "Indigo", "Ungu"}
    contoh_set_2 = {"Hitam", "Putih", "Merah"}
    contoh_set.intersection_update(contoh_set_2)
    print(contoh_set)
    print(contoh_set_2)


    # kembalikan set yang baru dengan element yang sama dari kedua-dua set
    contoh_set = {"Merah", "Jingga", "Kuning", "Hijau", "Biru", "Indigo", "Ungu"}
    contoh_set_2 = {"Hitam", "Putih", "Merah"}
    result = contoh_set.intersection(contoh_set_2)
    print(result)


    # kembalikan set dengan element yang berbeza dari kedua-dua set
    contoh_set = {"Merah", "Jingga", "Kuning", "Hijau", "Biru", "Indigo", "Ungu"}
    contoh_set_2 = {"Hitam", "Putih", "Merah"}
    contoh_set.symmetric_difference_update(contoh_set_2)
    print(contoh_set)


    # kembalikan set yang baru dengan element yang berbeza dari kedua-dua set
    contoh_set = {"Merah", "Jingga", "Kuning", "Hijau", "Biru", "Indigo", "Ungu"}
    contoh_set_2 = {"Hitam", "Putih", "Merah"}
    result = contoh_set.symmetric_difference(contoh_set_2)
    print(result)
    
    print("END")


if __name__ == '__main__':
    main()