import numpy as np

def backward_interpolation(x, y, x_val):
    n = len(x)
    p = np.zeros((n, n))

    # Filling the first column of the difference table
    for i in range(n):
        p[i][0] = y[i]

    # Calculating the backward difference table
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            p[j][i] = p[j][i - 1] - p[j - 1][i - 1]

    # Calculating the interpolated value
    result = p[n - 1][0]
    u = (x_val - x[n - 1]) / (x[1] - x[0])
    for i in range(1, n):
        result += (u_cal(u, i) * p[n - 1][i]) / factorial(i)

    return result

def u_cal(u, n):
    temp = u
    for i in range(1, n):
        temp *= (u + i)
    return temp

def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def get_user_input():
    x_str = input("Enter x values separated by space: ")
    y_str = input("Enter y values separated by space: ")
    x_val = float(input("Enter the value of x for interpolation: "))

    x = [float(val.strip()) for val in x_str.split()]
    y = [float(val.strip()) for val in y_str.split()]

    return x, y, x_val

def main():
    print("Newton's Backward Interpolation")
    print("--------------------------------")

    x, y, x_val = get_user_input()

    interpolated_value = backward_interpolation(x, y, x_val)
    print(f"\nInterpolated value at x = {x_val}: {interpolated_value}")

if __name__ == "__main__":
    main()
