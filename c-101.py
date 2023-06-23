import random

response = input("Você quer rolar o dado?(y/n)")

while response == "y":
    n = random.randint(1,6)

    if n == 1:
        print("[=====]")
        print("[     ]")
        print("[  *  ]")
        print("[     ]")
        print("[=====]")
    if n == 2:
        print("[=====]")
        print("[*    ]")
        print("[     ]")
        print("[    *]")
        print("[=====]")
    if n == 3:
        print("[=====]")
        print("[*    ]")
        print("[  *  ]")
        print("[    *]")
        print("[=====]")
    if n == 4:
        print("[=====]")
        print("[*   *]")
        print("[     ]")
        print("[*   *]")
        print("[=====]")
    if n == 5:
        print("[=====]")
        print("[*   *]")
        print("[  *  ]")
        print("[*   *]")
        print("[=====]")
    if n == 6:
        print("[=====]")
        print("[* * *]")
        print("[     ]")
        print("[* * *]")
        print("[=====]")

    print(n)
    response = input("Você quer rolar o dado novamente?(y/n)")
