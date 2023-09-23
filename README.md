# MathFox

A library with math functions to help **Python** developers with their projects.

In total, we have **34** functions!

## MathFox link on:
[**PYPI**](https://pypi.org/project/mathfox)
<br>
[**GitHub**](https://github.com/PipocaFox/MathFox)

---

## Versions

- [**1.0.1**](https://pypi.org/project/mathfox/1.0.1/) **---** 
Correction of the `Chance()` function and creation of more decent documentation.
- [**1.0.0**](https://pypi.org/project/mathfox/1.0.0/) **---** 
Library creation.

---

## Library structure
- mathfox
  
    - math
      - area
        - two_dimensions
        - three_dimensions
    - number
    - numis
  

---

## Math

16 functions + 12 area function

<br>

### - `sumlist(list)`

```python
import mathfox
list = [1, 2, 4, 4]
sum = mathfox.math.sumlist(list)
print(sum)
```
> **11**

<br>

### - `sublist(list)`
```python
import mathfox
list = [7, 4, 2]
sub = mathfox.math.sublist(list)
print(sub)
```
> **1**

<br>

### - `multlist(list)`
```python
import mathfox
list = [2, 4, 2]
mult = mathfox.math.multlist(list)
print(mult)
```
> **16**

<br>

### - `divlist(list)`
```python
import mathfox
list = [1, 2, 2]
div = mathfox.math.divlist(list)
print(div)
```
> **0.25**

<br>

### - `medium(*num)`
```python
import mathfox
list = [10, 8, 4, 5]
medium = mathfox.math.medium(list, 2)
print(medium)
```
> **5.8**

<br>

### - `root(num, ind)`
```python
import mathfox
num = 121
ind = 2
root = mathfox.math.root(num, ind)
print(root)
```
> **11.0**

<br>

### - `factorial(num)`
``` python
import mathfox
num = 5
factorial = mathfox.math.factorial(num)
print(factorial)
```
> **120**

<br>

### - `lcm(*num, result=False)`
```python
import mathfox
list = [8, 9, 2]
lcm1 = mathfox.math.lcm(list, 13)
lcm2 = mathfox.math.lcm(list, result=True)
print(f'{lcm1}\n{lcm2}')
```
> **{2: 3, 3: 2, 13: 1}** <br>
> **{2: 3, 3: 2, 'result': 72}**

<br>

### - `gcm(*num, result=False)`
```python
import mathfox
list = [8, 4]
gcd1 = mathfox.math.gcd(list, 16)
gcd2 = mathfox.math.gcd(list, result=True)
print(f'{gcd1}\n{gcd2}')
```
> **{2: 2}** <br>
> **{2: 2', result': 4}**

<br>

### - `sin(num)`
```python
import mathfox
num = 30
sin = mathfox.math.sin(num)
print(sin)
```
> **-0.9880316240928618**

<br>

### - `cos(num)`
```python
import mathfox
num = 45
cos = mathfox.math.cos(num)
print(cos)
```
> **0.5253219888177297**

<br>

### - `tan(num)`
```python
import mathfox
num = 60
tan = mathfox.math.tan(num)
print(tan)
```
> **0.320040389379563**

<br>

### - `chance(percentage)`
```python
import mathfox
percentage = 50
result = mathfox.math.chance(percentage)
print(result)
```
> **True**

or

> **False**

<br>

### - `log(exp, base)`
```python
import mathfox
exp = 3
base = 2
log = mathfox.math.log(exp, base)
print(log)
```
> **1.5849625007211563**

<br>

### - `rule_of_three(a, b, c)`
```python
import mathfox
a, b, c = 35, 100, 40
result = mathfox.math.rule_of_three(a, b, c)
print(result)
```
> **114.28571428571429**

<br>

### - `bhaskara(a, b, c)`
```python
import mathfox
a, b, c = -1, 2, 3
x1, x2 = mathfox.math.bhaskara(a, b, c)
print(f'''X1 = {x1}
X2 = {x2}''')
```
> **X1 = -1.0**
> 
> **X2 = 3.0**

<br>

## Area

### Two dimensions

<br>

### - `square(side)`
```python
import mathfox
side = 2
area = mathfox.math.area.two_dimensions.square(side)
print(area)
```
> **4**

<br>

### - `rectangle(height, base)`
```python
import mathfox
height = 4
base = 2
area = mathfox.math.area.two_dimensions.rectangle(height, base)
print(area)
```
> **8**

<br>

### - `right_triangle(height, base)`
```python
import mathfox
height = 7
base = 3
area = mathfox.math.area.two_dimensions.right_triangle(height, base)
print(area)
```
> **10.5**

<br>

### - `equilateral_triangle(side)`
```python
import mathfox
side = 6
area = mathfox.math.area.two_dimensions.equilateral_triangle(side)
print(area)
```
> **15.588457268119894**

<br>

### - `pentagon(side)`
```python
import mathfox
side = 5
area = mathfox.math.area.two_dimensions.pentagon(side)
print(area)
```
> **43.01193501472417**

<br>

### - `hexagon(side)`
```python
import mathfox
side = 6
area = mathfox.math.area.two_dimensions.hexagon(side)
print(area)
```
> **93.53074360871938**

<br>


---

## Number
3 functions

---

## Numis
3 functions
