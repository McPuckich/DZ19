l1 = [5, 9, 6, 7]
l2 = [3, 11, 8]
l3 = [2, 4]
l4 = [10, 1, 12]
l5 = l1 + l2 + l3 + l4
print(l5)

print("1 - сортировка по уюбыванию")
print("2 - сортировка по возрастанию")
sortirovka = int(input("-> "))
zn = int(input("Введите значение для поиска: "))

def seq_search(s, item):
    found = False
    pos = 0
    stop = False
    while pos < len(s) and not found and not stop:
        if s[pos] == item:
            found = True
        else:
            if s[pos] > item:
                stop = True
            else:
                pos += 1
    if found == True:
        print("Значение ", item, " найдено")
    else:
        print("Значение ", item, " не найдено")


def quick_sort(a):
    if sortirovka == 1:
        if len(a) > 1:
            x = a[(len(a) - 1) // 2]
            low = [i for i in a if i < x]
            eq = [i for i in a if i == x]
            hi = [i for i in a if i > x]
            a = quick_sort(hi) + eq + quick_sort(low)

        return a
    elif sortirovka == 2:
        if len(a) > 1:
            x = a[(len(a) - 1) // 2]
            low = [i for i in a if i < x]
            eq = [i for i in a if i == x]
            hi = [i for i in a if i > x]
            a = quick_sort(low) + eq + quick_sort(hi)

        return a

match sortirovka:
    case 1:
        print(quick_sort(l5))
        seq_search(l5, zn)
    case 2:
        print(quick_sort(l5))
        seq_search(l5, zn)

