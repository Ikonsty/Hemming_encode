"""
Задано повідомлення. Закодувати його (7, 4)- кодом Геммінга.
(Скористатися породжувальною матрицею; див підручник, стор. 292).
"""

def hamm_coder(bits):
    """
    Encode 4 bits with (7, 4)-Hamming code
    Matrix for this code is:
    [0001111]
    [0110011]
    [1010101]
       ^ ^^^
    """
    # Parity bits numbers are taken from matrix for this code
    b1 = find_parity(bits, [0,1,3])
    b2 = find_parity(bits, [0,2,3])
    b4 = find_parity(bits, [1,2,3])
    return b1 + b2 + bits[0] + b4 + bits[1:]


def find_parity(bits, posittions):
    """
    Find parity of ine but based on 7,4-positions
    Takes positions
    """
    sum = ""
    for i in posittions:
        sum += bits[i]
    return str(str.count(sum, "1") % 2)


def encoder(mass):
    """
    Encode massage with (7, 4)-Hamming code
    """
    answer = ''
    while len(mass) >= 4:
        bits = mass[0:4]
        answer += hamm_coder(bits)
        mass = mass[4:]
    return answer


def check_valid(mass):
    """
    Check if input massage is code that divides on 4
    """
    try:
        int(mass)
    except ValueError:
        print("Massage must be integer bits\n")
        return False
    if int(mass) < 0:
        print("Bits can`t be negative\n")
        return False
    for i in mass:
        if int(i) > 1:
            print("Every bit can be only 0 or 1\n")
            return False
    if not len(mass) % 4 == 0:
        print("Massage`s length must divides on 4\n")
        return False
    return True


if __name__ == "__main__":
    mass = input("Enter bits to encode: ").strip()
    while not check_valid(mass):
        mass = input("Enter bits to encode: ").strip()
    answ = encoder(mass)
    print("Output: " + answ)
