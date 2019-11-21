# fibonacci.py

def fib():
    fibs = [1, 2]

    for i in range(1,100):

        new = fibs[i] + fibs[i-1]
        fibs.append(new)

    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()