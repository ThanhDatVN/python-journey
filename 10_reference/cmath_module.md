# Python cMath Module — Module cmath

[📖 Reference](README.md) · [📚 Mục lục](../README.md) · W3Schools: [module_cmath](https://www.w3schools.com/python/module_cmath.asp)

Module `cmath` cung cấp các hàm toán học cho **số phức** (`complex`). Nhiều hàm giống module `math`, nhưng nhận và trả về số phức.

```python
import cmath

print(cmath.sqrt(-1))        # 1j  (math.sqrt(-1) sẽ báo lỗi!)
print(cmath.phase(-1 + 0j))  # góc: π
print(cmath.polar(1 + 1j))   # (độ lớn, góc)
```

## Hàm

| Hàm | Mô tả |
|---|---|
| `acos(x)` / `asin(x)` / `atan(x)` | Lượng giác ngược |
| `acosh(x)` / `asinh(x)` / `atanh(x)` | Hyperbolic ngược |
| `cos(x)` / `sin(x)` / `tan(x)` | Lượng giác |
| `cosh(x)` / `sinh(x)` / `tanh(x)` | Hyperbolic |
| `exp(x)` | e mũ x |
| `isclose(a, b)` | Hai giá trị gần bằng nhau? |
| `isfinite(x)` / `isinf(x)` / `isnan(x)` | Hữu hạn / vô cực / NaN? |
| `log(x, base)` / `log10(x)` | Logarit |
| `phase(x)` | Góc (pha) của số phức |
| `polar(x)` | Chuyển sang toạ độ cực `(r, phi)` |
| `rect(r, phi)` | Chuyển từ toạ độ cực sang số phức |
| `sqrt(x)` | Căn bậc hai (kể cả số âm) |

## Hằng số

| Hằng số | Ý nghĩa |
|---|---|
| `cmath.e` / `cmath.pi` / `cmath.tau` | e, π, 2π |
| `cmath.inf` / `cmath.infj` | Vô cực thực / ảo |
| `cmath.nan` / `cmath.nanj` | NaN thực / ảo |

**Bài học liên quan:** [Python Numbers — Complex](../01_python_tutorial/015_python_numbers.ipynb)
