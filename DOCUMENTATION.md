# MATHFOX DOCUMENTATION

---

## Calculation

20 functions + 20 geometry function

### • `sublist(list)`
```python
import mathfox
list = [7, 4, 2]
sub = mathfox.cal.sublist(list)
print(sub)
```
> **1**

<br>

### • `multlist(list)`
```python
import mathfox
list = [2, 4, 2]
mult = mathfox.cal.multlist(list)
print(mult)
```
> **16**

<br>

### • `divlist(list)`
```python
import mathfox
list = [1, 2, 2]
div = mathfox.cal.divlist(list)
print(div)
```
> **0.25**

<br>

### • `mean(*num)`
```python
import mathfox
list = [10, 8, 4, 5]
medium = mathfox.cal.mean(list, 2)
print(medium)
```
> **5.8**

<br>

### • `median(*num)`
```python
import mathfox
list1 = [7, 8, 3, 4, 1, 2]
list2 = [6, 7, 3]
median = mathfox.cal.median(list1, list2)
print(median)
```
> **4**

<br>

### • `mode(*num)`
```python
import mathfox
list = [11, 6, 4, 5, 2]
mode = mathfox.cal.mode(list, 2)
print(mode)
```
> **2**

<br>

### • `std(*num)`
```python
import mathfox
list = [1, 4, 7, 2, 6]
std = mathfox.cal.std(list)
print(std)
```
> **2.280350850198276**

<br>

### • `var(*num)`
```python
import mathfox
list = [460, 800, 300, 400]
var = mathfox.cal.var(list)
print(var)
```
> **35300.0**

<br>

### • `root(num, ind)`
```python
import mathfox
num = 121
ind = 2
root = mathfox.cal.root(num, ind)
print(root)
```
> **11.0**

<br>

### • `factorial(num)`
```python
import mathfox
num = 5
factorial = mathfox.cal.factorial(num)
print(factorial)
```
> **120**

<br>

### • `lcm(*num, result=False)`
```python
import mathfox
list = [8, 9, 2]
lcm1 = mathfox.cal.lcm(list, 13)
lcm2 = mathfox.cal.lcm(list, result=True)
print(f'{lcm1}\n{lcm2}')
```
> **{2: 3, 3: 2, 13: 1}** <br>
> **{2: 3, 3: 2, 'result': 72}**

<br>

### • `gcm(*num, result=False)`
```python
import mathfox
list = [8, 4]
gcd1 = mathfox.cal.gcd(list, 16)
gcd2 = mathfox.cal.gcd(list, result=True)  
print(f'{gcd1}\n{gcd2}')
```
> **{2: 2}** <br>
> **{2: 2', result': 4}**

<br>

### • `radians(num)`
```python
import mathfox
num = 30
rad = mathfox.cal.radians(num)
print(rad)
```
> **0.5235987755982988**

<br>

### • `degrees(num)`
```python
import mathfox
num = 3.14159
deg = mathfox.cal.degrees(num)
print(deg)
```
> **179.9998479605043**

<br>

### • `chance(percentage)`
```python
import mathfox
percentage = 50
result = mathfox.cal.chance(percentage) #has a 50% chance of returning True or False
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
log = mathfox.cal.log(exp, base)
print(log)
```
> **1.5849625007211563**

<br>

### • `rule_of_three(a, b, c, invert=False)`
```python
import mathfox
a, b, c = 100, 30, 50

# a -- c
# b -- x

result_normal = mathfox.cal.rule_of_three(a, b, c)
result_invert = mathfox.cal.rule_of_three(a, b, c, invert=True)

print(f'normal = {result_normal}')
print(f'invert = {result_invert}')
```
> **normal = 15.0** <br>
> **invert = 60.0**

<br>

### • `bhaskara(a, b, c)`
```python
import mathfox
a, b, c = -1, 2, 3
x1, x2 = mathfox.cal.bhaskara(a, b, c)
print(f'''X1 = {x1}
X2 = {x2}''')
```
> **X1 = -1.0** <br>
> **X2 = 3.0**

---

## Geometry
13 area function + 6 trigonometry functions

### • `hypotenuse(leg1, leg2):`
```python
import mathfox
leg1 = 3
leg2 = 4
hyp = mathfox.cal.geo.hypotenuse(leg1, leg2)
print(hyp)
```
> **5.0** <br>


---

## Area

### Two dimensions

### • `square(side)`
```python
import mathfox
side = 2
area = mathfox.cal.geo.area.two_dimensions.square(side)
print(area)
```
> **4**

<br>

### • `rectangle(height, base)`
```python
import mathfox
height = 4
base = 2
area = mathfox.cal.geo.area.two_dimensions.rectangle(height, base)
print(area)
```
> **8**

<br>

### • `right_triangle(height, base)`
```python
import mathfox
height = 7
base = 3
area = mathfox.cal.geo.area.two_dimensions.right_triangle(height, base)
print(area)
```
> **10.5**

<br>

### • `equilateral_triangle(side)`
```python
import mathfox
side = 6
area = mathfox.cal.geo.area.two_dimensions.equilateral_triangle(side)
print(area)
```
> **15.588457268119894**

<br>

### • `pentagon(side)`
```python
import mathfox
side = 5
area = mathfox.cal.geo.area.two_dimensions.pentagon(side)
print(area)
```
> **43.01193501472417**

<br>

### • `hexagon(side)`
```python
import mathfox
side = 6
area = mathfox.cal.geo.area.two_dimensions.hexagon(side)
print(area)
```
> **93.53074360871938**

<br>

### • `polygon(side, sides)`
```python
import mathfox
side = 4
sides = 7
area = mathfox.cal.geo.area.two_dimensions.polygon(side, sides)
print(area)
```
> **58.14259910402543**

<br>

### • `circle(radius)`
```python
import mathfox
radius = 2
area = mathfox.cal.geo.area.two_dimensions.circle(radius)
print(area)
```
> **12.5663706143591724639918538741767406463623046875**

<br>

### Three dimensions

### • `cube(edge)`
```python
import mathfox
edge = 5
area = mathfox.cal.geo.area.three_dimensions.cube(edge)
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
area = mathfox.cal.geo.area.three_dimensions.parallelepiped(height, width, depth)
print(area)
```
> **60**

<br>

### • `cylinder(height, radius)`
```python
import mathfox
height = 5
radius = 4
area = mathfox.cal.geo.area.three_dimensions.cylinder(height, radius)
print(area)
```
> **251.327412287183449279837077483534812927246093750**

<br>

### • `sphere(radius)`
```python
import mathfox
radius = 6
area = mathfox.cal.geo.area.three_dimensions.sphere(radius)
print(area)
```
> **452.389342116930208703706739470362663269042968750**

<br>

## Trigonometry

### • `sin(num, type='degrees')`
```python
import mathfox
num = 30
sin1 = mathfox.cal.geo.trigo.sin(num)
sin2 = mathfox.cal.geo.trigo.sin(num, type='radians')
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
cos1 = mathfox.cal.geo.trigo.cos(num)
cos2 = mathfox.cal.geo.trigo.cos(num, type='radians')
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
tan1 = mathfox.cal.geo.trigo.tan(num)
tan2 = mathfox.cal.geo.trigo.tan(num, type='radians')
print(tan1)
print(tan2)
```
> **1.7320508075688767** <br>
> **0.320040389379563**

<br>

### • `arcsin(num, type='degrees')`
```python
import mathfox
num = 1
arcsin1 = mathfox.cal.geo.trigo.arcsin(num)
arcsin2 = mathfox.cal.geo.trigo.arcsin(num, type='radians')
print(arcsin1)
print(arcsin2)
```
> **90.0** <br>
> **1.5707963267948966**

<br>

### • `arccos(num, type='degrees')`
```python
import mathfox
num = -1
arccos1 = mathfox.cal.geo.trigo.arccos(num)
arccos2 = mathfox.cal.geo.trigo.arccos(num, type='radians')
print(arccos1)
print(arccos2)
```
> **180.0** <br>
> **3.141592653589793**

<br>

### • `arctan(num)`
```python
import mathfox
num = 1
arctan1 = mathfox.cal.geo.trigo.arctan(num)
arctan2 = mathfox.cal.geo.trigo.arctan(num, type= 'radians')
print(arctan1)
print(arctan2)
```
> **45.0** <br>
> **0.7853981633974483**

<br>

### • `csc(num, type='degrees')`
```python
import mathfox
num = 30
csc1 = mathfox.cal.geo.trigo.csc(num)
csc2 = mathfox.cal.geo.trigo.csc(num, type='radians')
print(csc1)
print(csc2)
```
> **2.0000000000000004** <br>
> **-1.012113353070178**

<br>

### • `sec(num, type='degrees')`
```python
import mathfox
num = 45
sec1 = mathfox.cal.geo.trigo.sec(num)
sec2 = mathfox.cal.geo.trigo.sec(num, type='radians')
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
cot1 = mathfox.cal.geo.trigo.cot(num)
cot2 = mathfox.cal.geo.trigo.cot(num, type='radians')
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
inf = mathfox.number.inf
print(1 < inf)
```
> **True**

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

### • `pi(precision=48)`
```python
import mathfox
pi1 = mathfox.number.pi()
pi2 = mathfox.number.pi(5)
print(f'PI1: {pi1}\nPI2: {pi2}')
```
> **PI1: 3.141592653589793115997963468544185161590576171875** <br>
> **PI2: 3.14159**

<br>

### • `e(precision=48)`
```python
import mathfox
e1 = mathfox.number.e()
e2 = mathfox.number.e(5)
print(f'e1: {e1}\ne: {e2}')
```
> **e1: 2.718281828459045235360287471352662497757247093699** <br>
> **e2: 2.71828**

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
isdecimal1, decimal_places = mathfox.numis.isdecimal(num1, decimal_places=True)
isdecimal2, covert = mathfox.numis.isdecimal(num2, convert=True, comma=True)
isdecimal3 = mathfox.numis.isdecimal(num3, integer=False)
print(f'Num1: {isdecimal1}; decimal places: {decimal_places}\nNum2: {isdecimal2}; convert: {covert}\nNum3: {isdecimal3}')
```
> **Num1: True; decimal places: 2** <br>
> **Num2: True; convert: 2.5** <br>
> **Num3: False**

---