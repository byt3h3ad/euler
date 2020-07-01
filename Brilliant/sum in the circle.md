[Problem](https://brilliant.org/daily-problems/circle-fill-8/)
```python
# 2 indicates multiplication arrow and 1 indicates addition arrow

graph = [[0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0], 
         [2, 2, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0], 
         [0, 0, 1, 1, 0, 0], 
         [0, 0, 2, 0, 2, 0]]

# coeff indicates in order [x^2 coefficient, x coefficient, constant term]        

coeff = [[0, 1, 0], [0, 0, 2], [0, 0, 0], [0, 0, 6], [0, 0, 0], [0, 0, -16]] # -16 as it will come to left side

i = 0

while i <= 5:
    x1 = 1
    x2 = 1
    st = 0
    r = coeff[i][2]
    for j in range(0, 6):
        if graph[i][j] == 1:
            for k in range(0, 3):
                coeff[i][k] += coeff[j][k]
            r = 0

        elif graph[i][j] == 2:
            if x1 == 1:
                for k in range(0, 3):
                    coeff[i][k] = 1

                coeff[i][1] = 0

            coeff[i][0] *= coeff[j][1] # coefficient of x^2 = coefficient of x * coefficient of x
            coeff[i][2] *= coeff[j][2] # constant term = constant term * constant term

            if st == 0:
                x1 *= coeff[j][2]
            else:
                coeff[i][1] += x1 * coeff[j][1] # coefficient of x += coefficient of x * constant term

            if st == 0:
                x2 *= coeff[j][1]
            else:
                coeff[i][1] += x2 * coeff[j][2]

            st += 1

    if st > 0:
        coeff[i][2] += r
    i += 1

for i in range(0, 6):
    print("value is: %sx^2 + %sx + %s" % (coeff[i][0], coeff[i][1], coeff[i][2]))

print("\n Sum is - b/a = %s" % (-1 * coeff[5][1] / coeff[5][0]))
