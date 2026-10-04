# Python Math Module — Module math

[📖 Reference](README.md) · [📚 Mục lục](../README.md) · W3Schools: [module_math](https://www.w3schools.com/python/module_math.asp)

```python
import math
```

## Hàm

| Hàm | Mô tả | Ví dụ |
|---|---|---|
| `acos(x)` / `asin(x)` / `atan(x)` | Arc cos / sin / tan (radian) | `math.asin(1)` → `1.5707…` |
| `acosh(x)` / `asinh(x)` / `atanh(x)` | Hàm hyperbolic ngược | |
| `atan2(y, x)` | Arc tan của y/x, đúng góc phần tư | `math.atan2(1, 1)` |
| `ceil(x)` | Làm tròn **lên** | `math.ceil(1.2)` → `2` |
| `comb(n, k)` | Tổ hợp chập k của n | `math.comb(5, 2)` → `10` |
| `copysign(x, y)` | Giá trị của x với dấu của y | `math.copysign(3, -1)` → `-3.0` |
| `cos(x)` / `sin(x)` / `tan(x)` | Lượng giác (radian) | `math.cos(0)` → `1.0` |
| `cosh(x)` / `sinh(x)` / `tanh(x)` | Hyperbolic | |
| `degrees(x)` / `radians(x)` | Radian ↔ độ | `math.degrees(math.pi)` → `180.0` |
| `dist(p, q)` | Khoảng cách Euclid giữa 2 điểm | `math.dist((0, 0), (3, 4))` → `5.0` |
| `erf(x)` / `erfc(x)` | Hàm lỗi / lỗi bù | |
| `exp(x)` / `expm1(x)` | e^x / e^x − 1 | `math.exp(1)` → `2.718…` |
| `fabs(x)` | Giá trị tuyệt đối (float) | `math.fabs(-3)` → `3.0` |
| `factorial(x)` | Giai thừa | `math.factorial(5)` → `120` |
| `floor(x)` | Làm tròn **xuống** | `math.floor(1.8)` → `1` |
| `fmod(x, y)` | Phần dư (float) | `math.fmod(7, 3)` → `1.0` |
| `frexp(x)` | Phân tích thành mantissa và số mũ | |
| `fsum(iter)` | Tổng chính xác cho số thực | `math.fsum([0.1] * 10)` → `1.0` |
| `gamma(x)` / `lgamma(x)` | Hàm Gamma / log Gamma | |
| `gcd(*ints)` / `lcm(*ints)` | ƯCLN / BCNN | `math.gcd(12, 18)` → `6` |
| `hypot(*coords)` | Độ dài vector (cạnh huyền) | `math.hypot(3, 4)` → `5.0` |
| `isclose(a, b)` | Hai số gần bằng nhau? | `math.isclose(0.1 + 0.2, 0.3)` → `True` |
| `isfinite(x)` / `isinf(x)` / `isnan(x)` | Hữu hạn / vô cực / NaN? | |
| `isqrt(n)` | Căn bậc hai nguyên | `math.isqrt(17)` → `4` |
| `ldexp(x, i)` | x * 2**i | |
| `log(x, base)` | Logarit (mặc định cơ số e) | `math.log(8, 2)` → `3.0` |
| `log10(x)` / `log2(x)` / `log1p(x)` | Log cơ số 10 / 2 / log(1+x) | `math.log10(1000)` → `3.0` |
| `modf(x)` | Tách phần thập phân và phần nguyên | `math.modf(3.5)` → `(0.5, 3.0)` |
| `perm(n, k)` | Chỉnh hợp chập k của n | `math.perm(5, 2)` → `20` |
| `pow(x, y)` | x mũ y (float) | `math.pow(2, 3)` → `8.0` |
| `prod(iter)` | Tích các phần tử | `math.prod([1, 2, 3, 4])` → `24` |
| `remainder(x, y)` | Phần dư theo IEEE 754 | |
| `sqrt(x)` | Căn bậc hai | `math.sqrt(64)` → `8.0` |
| `trunc(x)` | Bỏ phần thập phân | `math.trunc(-3.7)` → `-3` |

## Hằng số

| Hằng số | Giá trị |
|---|---|
| `math.e` | 2.718281828459045 |
| `math.inf` | Vô cực dương |
| `math.nan` | NaN (Not a Number) |
| `math.pi` | 3.141592653589793 |
| `math.tau` | 6.283185307179586 (= 2π) |

**Bài học liên quan:** [Python Math](../01_python_tutorial/093_python_math.ipynb)
