# MATHFOX DOCUMENTATION

---

## Calculation

15 functions + 19 geometry function

### • `sublist(list)`
```python
import mathfox
list = [7, 4, 2]
sub = mathfox.calculation.sublist(list)
print(sub)
```
> **1**

<br>

### • `multlist(list)`
```python
import mathfox
list = [2, 4, 2]
mult = mathfox.calculation.multlist(list)
print(mult)
```
> **16**

<br>

### • `divlist(list)`
```python
import mathfox
list = [1, 2, 2]
div = mathfox.calculation.divlist(list)
print(div)
```
> **0.25**

<br>

### • `medium(*num)`
```python
import mathfox
list = [10, 8, 4, 5]
medium = mathfox.calculation.medium(list, 2)
print(medium)
```
> **5.8**

<br>

### • `root(num, ind)`
```python
import mathfox
num = 121
ind = 2
root = mathfox.calculation.root(num, ind)
print(root)
```
> **11.0**

<br>

### • `factorial(num)`
```python
import mathfox
num = 5
factorial = mathfox.calculation.factorial(num)
print(factorial)
```
> **120**

<br>

### • `lcm(*num, result=False)`
```python
import mathfox
list = [8, 9, 2]
lcm1 = mathfox.calculation.lcm(list, 13)
lcm2 = mathfox.calculation.lcm(list, result=True)
print(f'{lcm1}\n{lcm2}')
```
> **{2: 3, 3: 2, 13: 1}** <br>
> **{2: 3, 3: 2, 'result': 72}**

<br>

### • `gcm(*num, result=False)`
```python
import mathfox
list = [8, 4]
gcd1 = mathfox.calculation.gcd(list, 16)
gcd2 = mathfox.calculation.gcd(list, result=True)  
print(f'{gcd1}\n{gcd2}')
```
> **{2: 2}** <br>
> **{2: 2', result': 4}**

<br>

### • `radians(num)`
```python
import mathfox
num = 30
rad = mathfox.calculation.radians(num)
print(rad)
```
> **0.5235987755982988**

<br>

### • `chance(percentage)`
```python
import mathfox
percentage = 50
result = mathfox.calculation.chance(percentage) #has a 50% chance of returning True or False
print(result)
```
> **True**

or

> **False**

<br>

### • `log(exp, base)`
```python
import mathfox
exp = 3
base = 2
log = mathfox.calculation.log(exp, base)
print(log)
```
> **1.5849625007211563**

<br>

### • `rule_of_three(a, b, c, invert=False)`
```python
import mathfox
a, b, c = 100, 30, 50

# a -- b
# c -- x

result_normal = mathfox.calculation.rule_of_three(a, b, c)
result_invert = mathfox.calculation.rule_of_three(a, b, c, invert=True)

print(f'normal = {result_normal}')
print(f'invert = {result_invert}')
```
> **normal = 30.0** <br>
> **invert = 60.0**

<br>

### • `bhaskara(a, b, c)`
```python
import mathfox
a, b, c = -1, 2, 3
x1, x2 = mathfox.calculation.bhaskara(a, b, c)
print(f'''X1 = {x1}
X2 = {x2}''')
```
> **X1 = -1.0** <br>
> **X2 = 3.0**

---

## Geometry
12 area function + 6 trigonometry functions
## Area

### Two dimensions

### • `square(side)`
```python
import mathfox
side = 2
area = mathfox.calculation.geometry.area.two_dimensions.square(side)
print(area)
```
> **4**

<br>

### • `rectangle(height, base)`
```python
import mathfox
height = 4
base = 2
area = mathfox.calculation.geometry.area.two_dimensions.rectangle(height, base)
print(area)
```
> **8**

<br>

### • `right_triangle(height, base)`
```python
import mathfox
height = 7
base = 3
area = mathfox.calculation.geometry.area.two_dimensions.right_triangle(height, base)
print(area)
```
> **10.5**

<br>

### • `equilateral_triangle(side)`
```python
import mathfox
side = 6
area = mathfox.calculation.geometry.area.two_dimensions.equilateral_triangle(side)
print(area)
```
> **15.588457268119894**

<br>

### • `pentagon(side)`
```python
import mathfox
side = 5
area = mathfox.calculation.geometry.area.two_dimensions.pentagon(side)
print(area)
```
> **43.01193501472417**

<br>

### • `hexagon(side)`
```python
import mathfox
side = 6
area = mathfox.calculation.geometry.area.two_dimensions.hexagon(side)
print(area)
```
> **93.53074360871938**

<br>

### • `polygon(side, sides)`
```python
import mathfox
side = 4
sides = 7
area = mathfox.calculation.geometry.area.two_dimensions.polygon(side, sides)
print(area)
```
> **58.14259910402543**

<br>

### • `circle(radius)`
```python
import mathfox
radius = 2
area = mathfox.calculation.geometry.area.two_dimensions.circle(radius)
print(area)
```
> **12.5663706143591724639918538741767406463623046875**

<br>

### Three dimensions

### • `cube(edge)`
```python
import mathfox
edge = 5
area = mathfox.calculation.geometry.area.three_dimensions.cube(edge)
print(area)
```
> **125**

<br>

### • `parallelepiped(height, width, depth)`
```python
import mathfox
height = 5
width = 4
depth = 3
area = mathfox.calculation.geometry.area.three_dimensions.parallelepiped(height, width, depth)
print(area)
```
> **60**

<br>

### • `cylinder(height, radius)`
```python
import mathfox
height = 5
radius = 4
area = mathfox.calculation.geometry.area.three_dimensions.cylinder(height, radius)
print(area)
```
> **251.327412287183449279837077483534812927246093750**

<br>

### • `sphere(radius)`
```python
import mathfox
radius = 6
area = mathfox.calculation.geometry.area.three_dimensions.sphere(radius)
print(area)
```
> **452.389342116930208703706739470362663269042968750**

<br>

## Trigonometry

### • `sin(num, type='degrees')`
```python
import mathfox
num = 30
sin1 = mathfox.calculation.geometry.trigonometry.sin(num)
sin2 = mathfox.calculation.geometry.trigonometry.sin(num, type='radian')
print(sin1)
print(sin2)
```
> **0.49999999999999994** <br>
> **-0.9880316240928618**

<br>

### • `cos(num, type='degrees')`
```python
import mathfox
num = 45
cos1 = mathfox.calculation.geometry.trigonometry.cos(num)
cos2 = mathfox.calculation.geometry.trigonometry.cos(num, type='radian')
print(cos1)
print(cos2)
```
> **0.7071067811865476** <br>
> **0.5253219888177297**

<br>

### • `tan(num, type='degrees')`
```python
import mathfox
num = 60
tan1 = mathfox.calculation.geometry.trigonometry.tan(num)
tan2 = mathfox.calculation.geometry.trigonometry.tan(num, type='radian')
print(tan1)
print(tan2)
```
> **1.7320508075688767** <br>
> **0.320040389379563**

<br>

### • `asin(num, type='degrees')`
```python
import mathfox
num = 1
asin1 = mathfox.calculation.geometry.trigonometry.asin(num)
asin2 = mathfox.calculation.geometry.trigonometry.asin(num, type='radian')
print(asin1)
print(asin2)
```
> **0.01745417873758517** <br>
> **1.5707963267948966**

<br>

### • `acos(num, type='degrees')`
```python
import mathfox
num = -1
acos1 = mathfox.calculation.geometry.trigonometry.acos(num)
acos2 = mathfox.calculation.geometry.trigonometry.acos(num, type='radian')
print(acos1)
print(acos2)
```
> **0.5253219888177297**

<br>

### • `atan(num)`
```python
import mathfox
num = 90
atan = mathfox.calculation.geometry.trigonometry.atan(num)
print(atan)
```
> **1.5596856728972892**

<br>

### • `csc(num, type='degrees')`
```python
import mathfox
num = 30
csc1 = mathfox.calculation.geometry.trigonometry.csc(num)
csc2 = mathfox.calculation.geometry.trigonometry.csc(num, type='radian')
print(csc1)
print(csc2)
```
> **1.060370348985591** <br>
> **-0.9880316240928618**

<br>

### • `sec(num, type='degrees')`
```python
import mathfox
num = 45
sec1 = mathfox.calculation.geometry.trigonometry.sec(num)
sec2 = mathfox.calculation.geometry.trigonometry.sec(num, type='radian')
print(sec1)
print(sec2)
```
> **1.414213562373095** <br>
> **1.9035944074044246**

<br>

### • `cot(num, type='degrees')`
```python
import mathfox
num = 60
cot1 = mathfox.calculation.geometry.trigonometry.cot(num)
cot2 = mathfox.calculation.geometry.trigonometry.cot(num, type='radian')
print(cot1)
print(cot2)
```
> **0.577350269189626** <br>
> **3.124605622242308**

---

## Number
3 functions and 1 class

### • `inf`
```python
import mathfox
from time import sleep
inf = mathfox.number.inf
sleep(inf) # It will wait infinite seconds, that is, the command will stop there.
```

<br>

### • `prime(count)`
```python
import mathfox
count = 5
primes = mathfox.number.prime(count)
print(primes)
```
> **[2, 3, 5, 7, 11]**

<br>

### • `pi(count=48)`
```python
import mathfox
pi1 = mathfox.number.pi()
pi2 = mathfox.number.pi(5)
print(f'PI1: {pi1}\nPI2: {pi2}')
```
> **PI1: 3.141592653589793115997963468544185161590576171875** <br>
> **PI2: 3.14159**

<br>

### • `Fraction()`
```python
import mathfox
fraction1 = mathfox.number.Fraction(numerator=9, denominator=12)
fraction2 = mathfox.number.Fraction(0.02)
print(f'''
fraction 1 = {fraction1}; result = {fraction1.result}
fraction 2 = {fraction2}; result = {fraction2.result}
''')
fraction1.simplification()
print(f'simplification = {fraction1}')
print(f'sum = {fraction1 + fraction2}')
print(fraction1 > fraction2)
```
> **fraction 1 = 9 / 12; result = 0.75** <br>
> **fraction 2 = 1 / 50; result = 0.02** <br>
> **simplification = 3 / 4** <br>
> **sum = 77 / 100** <br>
> **True**


---

## Numis
3 functions

### • `isprime(num)`
```python
import mathfox
num1 = 3
num2 = 10
isprime1 = mathfox.numis.isprime(num1)
isprime2 = mathfox.numis.isprime(num2)
print(f'num1: {isprime1}\nnum2: {isprime2}')
```
> **num1: True** <br>
> **num2: False**

<br>

### • `isint(num, decimal=True)`
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
> **num1: True** <br>
> **num2: False** <br>
> **num3: True**

<br>

### • `isdecimal(num, comma=False, convert=False, integer=True decimal_places=False)`
```python
import mathfox
num1 = 5.84
num2 = '2,5'
num3 = 4
isfloat1, decimal_places = mathfox.numis.isdecimal(num1, decimal_places=True)
isfloat2, covert = mathfox.numis.isdecimal(num2, convert=True, comma=True)
isfloat3 = mathfox.numis.isdecimal(num3, integer=False)
print(f'Num1: {isfloat1}; decimal places: {decimal_places}\nNum2: {isfloat2}; convert: {covert}\nNum3: {isfloat3}')
```
> **Num1: True; decimal places: 2** <br>
> **Num2: True; convert: 2.5** <br>
> **Num3: False**

---
