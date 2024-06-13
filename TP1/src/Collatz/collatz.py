def collatz(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def main():
    for i in range(1, 10001):
        collatz_sequence = collatz(i)
        print(f"Número: {i}, Longitud de la secuencia: {len(collatz_sequence)}, Secuencia: {collatz_sequence}")

if __name__ == "__main__":
    main()
