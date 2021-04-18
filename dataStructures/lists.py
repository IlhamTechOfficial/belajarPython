def main():

    # dapatkan index element dalam array/list
    duit_RM = [0.05, 0.1, 0.2, 0.5, 1, 5, 10, 50, 100]
    print(duit_RM.index(50))


    # tambah element dalam array/list
    duit_RM = [0.05, 0.1, 0.2, 0.5, 1, 5, 10, 50, 100]
    duit_RM.append(60)
    print(duit_RM)


    # tambah element dalam array/list pada spesifik index
    duit_RM = [0.05, 0.1, 0.2, 0.5, 1, 5, 10, 50, 100]
    duit_RM.insert(8, 60)
    print(duit_RM)


    # kira element dalam array/list
    duit_RM = [0.05, 0.1, 0.2, 0.5, 1, 5, 10, 50, 50, 50, 100]
    print(duit_RM.count(50))


    # reverse sorting element dalam array/list
    duit_RM = [0.05, 0.1, 0.2, 0.5, 1, 5, 10, 50, 100]
    duit_RM.reverse()
    print(duit_RM)


    # sorting element dalam array/list (ascending element order)
    duit_RM = [0.05, 0.1, 0.2, 0.5, 1, 5, 10, 50, 100, 60]
    duit_RM.sort()
    print(duit_RM)


    # sorting element dalam array/list (ascending element order)
    duit_RM = [0.05, 0.1, 0.2, 0.5, 1, 5, 10, 50, 100]
    duit_RM_buffer = duit_RM
    duit_RM_buffer.append(60)
    print(duit_RM)
    print(duit_RM_buffer)


    duit_RM = [0.05, 0.1, 0.2, 0.5, 1, 5, 10, 50, 100]
    duit_RM_buffer = duit_RM.copy()
    duit_RM_buffer.append(60)
    
    print(duit_RM)
    print(duit_RM_buffer)


    # gabungkan dua list dalam satu array/list
    duit_RM = [0.05, 0.1, 0.2, 0.5, 1, 5, 10, 50, 100]
    duit_NAMA = ['RM', 'MYR']
    duit_RM.extend(duit_NAMA)
    print(duit_RM)


    # buang element pada spesifik index
    duit_RM = [0.05, 0.1, 0.2, 0.5, 1, 5, 10, 50, 100]
    duit_RM.pop(1)
    print(duit_RM)


    # buang element dalam array/list berdasarkan nama element tu sendiri
    duit_RM = [0.05, 0.1, 0.2, 0.5, 1, 5, 10, 10, 50, 50, 100]
    duit_RM.remove(10)
    print(duit_RM)


    # reset element dalam array/list jadi kosong
    duit_RM = [0.05, 0.1, 0.2, 0.5, 1, 5, 10, 50, 100]
    duit_RM.clear()
    print(duit_RM)

    print("main END")


def huha():
    print("huha END")


if __name__ == '__main__':
    main()