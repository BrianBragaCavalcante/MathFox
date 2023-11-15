# MathFox

A library with math functions to help **Python** developers with their projects.

In total, we have **36** functions and **1** class!

## MathFox link on:
[**PYPI**](https://pypi.org/project/mathfox)
<br>
[**GitHub**](https://github.com/PipocaFox/MathFox)

---

## Versions
- [**1.0.3**](https://pypi.org/project/mathfox/1.0.3/) **LATTER** **---**
Removal of the `sumlist()` function, creation of the `fraction()` class, and creation of a new category in the **math** category, which is **geometry**, within which there will be the **area** category (which was redefined), and the **trigonometry** category, which will have, in addition to the `sin()` functions, `cos()`, and `tan()`, will have the functions `asin()`, `acos()` and `atan()`.
- [**1.0.2**](https://pypi.org/project/mathfox/1.0.2/) **---**
Correction of the `chance()` function, improvement of the `isint()` and `isfloat()` functions, creation of more decent documentation.
- [**1.0.0**](https://pypi.org/project/mathfox/1.0.0/) **---** 
Library creation.

---

## Library structure
- mathfox
    - math
      - geometry
          - area
            - two_dimensions
            - three_dimensions
          - trigonometry
    - number
    - numis
  

---

## Math

15 functions + 19 geometry function

### - `sublist(list)`
```python
import mathfox
list = [7, 4, 2]
sub = mathfox.math.sublist(list)
print(sub)
```
> **1**

### - `multlist(list)`
```python
import mathfox
list = [2, 4, 2]
mult = mathfox.math.multlist(list)
print(mult)
```
> **16**

### - `divlist(list)`
```python
import mathfox
list = [1, 2, 2]
div = mathfox.math.divlist(list)
print(div)
```
> **0.25**

### - `medium(*num)`
```python
import mathfox
list = [10, 8, 4, 5]
medium = mathfox.math.medium(list, 2)
print(medium)
```
> **5.8**

### - `root(num, ind)`
```python
import mathfox
num = 121
ind = 2
root = mathfox.math.root(num, ind)
print(root)
```
> **11.0**

### - `factorial(num)`
``` python
import mathfox
num = 5
factorial = mathfox.math.factorial(num)
print(factorial)
```
> **120**

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

### - `rule_of_three(a, b, c)`
```python
import mathfox
a, b, c = 35, 100, 40

# a -- b
# c -- x

result = mathfox.math.rule_of_three(a, b, c)
print(result)
```
> **114.28571428571429**

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

---

## Geometry
12 area function + 6 trigonometry functions
## Area

### Two dimensions

<br>

### - `square(side)`
```python
import mathfox
side = 2
area = mathfox.math.geometry.area.two_dimensions.square(side)
print(area)
```
> **4**

### - `rectangle(height, base)`
```python
import mathfox
height = 4
base = 2
area = mathfox.math.geometry.area.two_dimensions.rectangle(height, base)
print(area)
```
> **8**

### - `right_triangle(height, base)`
```python
import mathfox
height = 7
base = 3
area = mathfox.math.geometry.area.two_dimensions.right_triangle(height, base)
print(area)
```
> **10.5**

### - `equilateral_triangle(side)`
```python
import mathfox
side = 6
area = mathfox.math.geometry.area.two_dimensions.equilateral_triangle(side)
print(area)
```
> **15.588457268119894**

### - `pentagon(side)`
```python
import mathfox
side = 5
area = mathfox.math.geometry.area.two_dimensions.pentagon(side)
print(area)
```
> **43.01193501472417**

### - `hexagon(side)`
```python
import mathfox
side = 6
area = mathfox.math.geometry.area.two_dimensions.hexagon(side)
print(area)
```
> **93.53074360871938**

### - `polygon(side, sides)`
```python
import mathfox
side = 4
sides = 7
area = mathfox.math.geometry.area.two_dimensions.polygon(side, sides)
print(area)
```
> **58.14259910402543**

### - `circle(radius)`
```python
import mathfox
radius = 2
area = mathfox.math.geometry.area.two_dimensions.circle(radius)
print(area)
```
> **12.5663706143591724639918538741767406463623046875**

### Three dimensions

<br>

### - `cube(edge)`
```python
import mathfox
edge = 5
area = mathfox.math.geometry.area.three_dimensions.cube(edge)
print(area)
```
> **125**

### - `parallelepiped(height, width, depth)`
```python
import mathfox
height = 5
width = 4
depth = 3
area = mathfox.math.geometry.area.three_dimensions.parallelepiped(height, width, depth)
print(area)
```
> **60**

### - `cylinder(height, radius)`
```python
import mathfox
height = 5
radius = 4
area = mathfox.math.geometry.area.three_dimensions.cylinder(height, radius)
print(area)
```
> **251.327412287183449279837077483534812927246093750**

### - `sphere(radius)`
```python
import mathfox
radius = 6
area = mathfox.math.geometry.area.three_dimensions.sphere(radius)
print(area)
```
> **452.389342116930208703706739470362663269042968750**

## Trigonometry

### - `sin(num)`
```python
import mathfox
num = 30
sin = mathfox.math.geometry.trigonometry.sin(num)
print(sin)
```
> **-0.9880316240928618**
<br>

### - `cos(num)`
```python
import mathfox
num = 45
cos = mathfox.math..geometry.trigonometry.cos(num)
print(cos)
```
> **0.5253219888177297**
<br>

### - `tan(num)`
```python
import mathfox
num = 60
tan = mathfox.math.geometry.trigonometry.tan(num)
print(tan)
```
> **0.320040389379563**
<br>

### - `asin(num)`
```python
import mathfox
num = 30
sin = mathfox.math.geometry.trigonometry.asin(num)
print(sin)
```
> **-0.9880316240928618**
<br>

### - `acos(num)`
```python
import mathfox
num = 45
cos = mathfox.math.geometry.trigonometry.acos(num)
print(cos)
```
> **0.5253219888177297**
<br>

### - `atan(num)`
```python
import mathfox
num = 60
tan = mathfox.math.geometry.trigonometry.atan(num)
print(tan)
```
> **0.320040389379563**
<br>
---

## Number
3 functions and 1 class

<br>

### - `prime(count)`
```python
import mathfox
count = 5
primes = mathfox.number.prime(count)
print(primes)
```
> **[2, 3, 5, 7, 11]**

### - `pi(count=48)`
```python
import mathfox
pi1 = mathfox.number.pi()
pi2 = mathfox.number.pi(5)
print(f'PI1: {pi1}\nPI2: {pi2}')
```
> **PI1: 3.141592653589793115997963468544185161590576171875**
> 
> **PI2: 3.14159**

### - `inf()`
```python
import mathfox
from time import sleep
inf = mathfox.number.inf()
sleep(inf) # It will wait infinite seconds, that is, the command will stop there.
```

### - `Fraction()`
```python
import mathfox
fraction1 = mathfox.number.Fraction(numerator=9, denominator=12)
fraction2 = mathfox.number.Fraction(num=0.02)
print(f'''
fraction 1 = {fraction1}; result = {fraction1.result()}
fraction 2 = {fraction2}; result = {fraction2.result()}
''')
fraction1.simplification()
print(f'simplification = {fraction1}')
```
> **fraction 1 = 9 / 12; result = 0.75**
> 
> **fraction 2 = 1 / 50; result = 0.02**
> 
> **simplification = 3 / 4**


---

## Numis
3 functions

<br>

### - `isprime(num)`
```python
import mathfox
num1 = 3
num2 = 10
isprime1 = mathfox.numis.isprime(num1)
isprime2 = mathfox.numis.isprime(num2)
print(f'num1: {isprime1}\nnum2: {isprime2}')
```
> **num1: True**
>
> **num2: False**

### - `isint(num, decimal=True)`
```python
import mathfox
num1 = 5
num2 = 2.5
num3 = 4.2
isint1 = mathfox.numis.isint(num1)
isint2 = mathfox.numis.isint(num2, decimal=False)
isint3 = mathfox.numis.isint(num3)
print(f'num1: {isint1}\nnum2: {isint2}\nnum3: {isint3}')
```
> **num1: True**
>
> **num2: False**
> 
>  **num3: True**


### - `isfloat(num, comma=False, convert=False, integer=True)`
```python
import mathfox
num1 = 5.8
num2 = '2,5'
num3 = 4.2
isfloat1 = mathfox.numis.isfloat(num1)
isfloat2, covert = mathfox.numis.isfloat(num2, convert=True, comma=True)
isfloat3 = mathfox.numis.isfloat(num3, integer=False)
print(f'num1: {isfloat1}\nnum2: {isfloat2}\nconvert: {covert}\nnum3: {isfloat3}')
```
> **num1: True**
>
> **num2: True**
> 
> **convert: 2.5**
> 
>  **num3: False**
