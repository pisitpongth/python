import numpy as np


def printline():
    print("-" * 100)


def main():
    row1 = np.array([1, 2, 3])
    row2 = np.array([4, 5, 6])
    matrix1 = np.array([row1, row2])
    printline()
    print("========== Matrix 1 ==========")
    print(matrix1)
    printline()
    matrix2row1 = np.array([7, 8, 9])
    matrix2row2 = np.array([10, 11, 12])
    matrix2row3 = np.array([13, 14, 15])
    matrix2 = np.array([matrix2row1, matrix2row2, matrix2row3])
    print("========== Matrix 2 ==========")
    print(matrix2)
    printline()
    print("========== Dot Product ==========")
    print(np.dot(matrix1, matrix2))


if __name__ == "__main__":
    main()
