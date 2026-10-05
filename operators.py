import numpy as np

def start():
    print("--- Python Arithmatic Operators ---\n")
    a = 10
    b = 3
    print(a + b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a % b) # 10 % 3 = 1
    print(a ** b)

    c = np.array([
            [1,2,3],
            [3,4,5],
            [6,7,8]
        ])
    d = np.array([
            [3,4,5],
            [6,7,8],
            [9,10,11]
        ])
    print(c @ d)

    print("--- Python Comparison Operators ---\n")
    print(10 == 10)
    print(a != b)
    print(a > b)
    print(a < b)
    print(a >= 11)
    print(4 <= b)
    e = True
    f = False
    print(e == True)
    print(e == f)

    g = "Python"
    h = "Python"
    print(g == h)

    print("---Logical Operators---")
    print((a == 11 or b == 3) and (g == "Python"))
    print(not(a<b))

    print("---Assignment Operators---")
    x = 10
    x += 5
    print(x)
    x -=5
    print(x)
    x *= 5
    print(x)
    x /=5
    print(x)
    x //=3
    print(x)
    x %= 1
    print(x)
    x = 10
    x **=3
    print(x)

    print("---Bitwise Operators---")
    p = 5 #101
    q = 3 #011
    print(p & q)
    print(p | q)
    print(p ^ q)
    print(~p)
    print(-6 << 1)
    print(-6 >> 1)
    p >>= 5
    print(p)
    # 010
    # 011
    # ---
    # 001
    # 1 -> 001, 2 -> 010, 3 -> 011, 4 -> 100, 5 -> 101, 6 -> 110, 7 -> 111
    # 8 -> 1000, 9 -> 1001, 10 -> 1010, 11 -> 1011, 12 -> 1100
    # 5  0000 0101
    # ~5 (-6)1111 1010
    # -6 << 1 -> 1111 0100
    # -6 >> 1 -> 0111 1101
    print("---Membership Operators---")
    language = ["python", "ruby", "groovy", "java"]
    print('python' not in language)
    print("python" in language)

def end():
    print("---End of Program---")

if __name__ == "__main__":
    start()
    end()