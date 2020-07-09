[Link](https://brilliant.org/daily-problems/sum-power-2/)

```python
def conversion(n, base, result):
    if n < base:
        result.append(n)
    else:
        conversion(n//base, base, result)
        result.append(n % base)
    return result

for i in [11, 26, 65, 127]:
    print(f"{i:3} : {' '.join([str(c) for c in conversion(i, 2, [])])}")
```
