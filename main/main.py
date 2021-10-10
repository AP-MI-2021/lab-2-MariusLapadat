def printMenu():
    print("1.Cel mai mic numar prim mai mare decat n")
    print("2.Verifica daca n este palindrom")
    print("3.Verifica daca n este superprim")
    print("Pentru a inchide, introduce x")


def NrPrim(n):
    '''
    Functia determina daca un numar este prim sau nu
    :param n numar intreg:
    :return adevarat sau fals:
    '''
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def get_largest_prime_below(n):
    '''
    Functia determina cel mai mare numar prim mai mic decat n
    :param n - numar intreg:
    :return un numar intreg :
    '''
    for i in range(n - 1, 1, -1):
        if NrPrim(i) == True:
            return i


def test_get_largest_prime_below():
    assert get_largest_prime_below(10) == 7
    assert get_largest_prime_below(25) == 23
    assert get_largest_prime_below(18) == 17


def is_palindrome(n):
    '''
    Determina daca un numar este palindrom sau nu
    :param n numar intreg:
    :return True daca n este palindrom sau False daca nu:
    '''
    auxiliar = int(n)
    k = 0
    while auxiliar > 0:
        k = k * 10 + auxiliar % 10
        auxiliar = auxiliar // 10
    if n == k:
        return True
    else:
        return False


def test_is_palindrome():
    assert is_palindrome(189) is False
    assert is_palindrome(18981) is True
    assert is_palindrome(72) is False


def is_superprime(n):
    '''
    Determina daca numarul este superprim
    :param n numar intreg:
    :return True daca este superprim sau False daca nu:
    '''
    auxiliar = n
    NrCifre = 0
    putere = 1
    while auxiliar > 0:
        auxiliar = auxiliar // 10
        NrCifre = NrCifre + 1
    k = NrCifre
    while k > 1:
        putere = putere * 10
        k = k - 1
    while NrCifre > 0:
        if NrPrim(n // putere) is False:
            return False
        NrCifre = NrCifre - 1
        putere = putere // 10
    return True


def test_is_superprime():
    assert is_superprime(233) is True
    assert is_superprime(73) is True
    assert is_superprime(237) is False


test_get_largest_prime_below()
test_is_palindrome()
test_is_superprime()

while True:
    printMenu()
    optiune = input("Dati optiunea: ")
    if optiune == "1":
        n = int(input("Dati nr: "))
        print(get_largest_prime_below(n))
    elif optiune == "2":
        n = int(input("Dati nr: "))
        if is_palindrome(n) is True:
            print("Numarul este palindrom")
        else:
            print("Numarul nu este palindrom")
    elif optiune == "3":
        n = int(input("Dati nr: "))
        if is_superprime(n) is True:
            print("Numarul este superprim")
        else:
            print("Numarul nu este superprim")
    elif optiune == "x":
        break
