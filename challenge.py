# answer submitted by James Borzillieri (jimmyb89@yahoo.com)
# You have to get dressed in the morning before going to work. Unfortunately, you only accept a space separated list of numbers to indicate article of clothing to don.
#
#     1 = hat
#     2 = pants
#     3 = shirt
#     4 = shoes
#     5 = socks
#
# Rules:
#
#     You must put your socks on before your shoes.
#     You must put your pants on before your shoes.
#     You must put your shirt on before your hat.
#     A hat is optional but all other articles of clothing are required.
#     You must leave the house when receiving the number 6. You must leave the house after getting dressed.
#     Any violation should output "fail" and stop immediately.


def get_dressed(a):
    s = []
    d = {1: 'hat', 2: 'pants', 3: 'shirt', 4: 'shoes', 5: 'socks'}
    for el in a:
        # socks before shoes
        if el == 5:
            s.append(el)
        elif el == 4 and 5 in s and 2 in s:
            s.append(el)
        # pants before shoes
        elif el == 2:
            s.append(el)
        # shirt before hat
        elif el == 3:
            s.append(el)
        elif el == 1 and 3 in s:
            s.append(el)
        # leave at 6
        elif el == 6 and {2, 3, 4, 5}.issubset(s):
            return ", ".join(d[x] for x in s) + ', leave'
        # violation
        else:
            s.append(el)
            return ", ".join(d[x] for x in s) + ', fail'


# driver function
def main():
    a1 = [2, 3, 4, 1, 5]
    a2 = [1, 2, 3, 4, 5]
    a3 = [5, 4, 3, 2, 1]
    a4 = [5, 2, 3, 4, 6]
    print(get_dressed(a1))
    print(get_dressed(a2))
    print(get_dressed(a3))
    print(get_dressed(a4))


if __name__ == '__main__':
    main()
