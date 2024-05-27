import numpy as np

def u_cal(u, n):
    temp = u
    for i in range(1, n):
        temp *= (u - i)
    return temp

def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def forward_interpolation(x, y, x_val):
    n = len(x)
    p = np.zeros((n, n))

    # Filling the first column of the difference table
    for i in range(n):
        p[i][0] = y[i]

    # Calculating the forward difference table
    for i in range(1, n):
        for j in range(n - i):
            p[j][i] = p[j + 1][i - 1] - p[j][i - 1]

    # Calculating the interpolated value
    result = p[0][0]
    u = (x_val - x[0]) / (x[1] - x[0])
    for i in range(1, n):
        result += (u_cal(u, i) * p[0][i]) / factorial(i)

    return result

def get_user_input():
    x_str = input("Enter x values separated by space: ")
    y_str = input("Enter y values separated by space: ")
    x_val = float(input("Enter the value of x for interpolation: "))

    x = [float(val.strip()) for val in x_str.split()]
    y = [float(val.strip()) for val in y_str.split()]

    return x, y, x_val

def main():
    print("Newton's Forward Interpolation")
    print("------------------------------")

    x, y, x_val = get_user_input()

    interpolated_value = forward_interpolation(x, y, x_val)
    print(f"\nInterpolated value at x = {x_val}: {interpolated_value}")

if __name__ == "__main__":
    main()
