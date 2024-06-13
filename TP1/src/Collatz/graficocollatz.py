import matplotlib.pyplot as plt

def collatz(n):
    iterations = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        iterations += 1
    return iterations

def main():
    n_values = []
    iterations_values = []

    for i in range(1, 10001):
        iterations = collatz(i)
        n_values.append(i)
        iterations_values.append(iterations)

    plt.scatter(iterations_values, n_values, marker='o', s=5)
    plt.xlabel('Número de iteraciones para converger')
    plt.ylabel('Número inicial de la secuencia')
    plt.title('Número de Collatz: Número inicial vs Iteraciones')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()