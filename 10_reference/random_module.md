# Python Random Module — Module random

[📖 Reference](README.md) · [📚 Mục lục](../README.md) · W3Schools: [module_random](https://www.w3schools.com/python/module_random.asp)

Module `random` có sẵn trong Python, dùng để sinh số **giả ngẫu nhiên**.

```python
import random
```

| Hàm | Mô tả | Ví dụ |
|---|---|---|
| `seed(a)` | Khởi tạo bộ sinh số (kết quả lặp lại được) | `random.seed(42)` |
| `getstate()` | Lấy trạng thái hiện tại của bộ sinh số | `s = random.getstate()` |
| `setstate(s)` | Khôi phục trạng thái | `random.setstate(s)` |
| `getrandbits(k)` | Số nguyên ngẫu nhiên có `k` bit | `random.getrandbits(8)` |
| `randrange(start, stop, step)` | Số nguyên trong `range(...)` | `random.randrange(0, 10, 2)` |
| `randint(a, b)` | Số nguyên trong `[a, b]` (**gồm cả b**) | `random.randint(1, 6)` |
| `choice(seq)` | Một phần tử ngẫu nhiên | `random.choice(["a", "b", "c"])` |
| `choices(seq, weights, k)` | `k` phần tử (có lặp lại), có thể kèm trọng số | `random.choices("ab", weights=[9, 1], k=5)` |
| `shuffle(list)` | Xáo trộn list **tại chỗ** | `random.shuffle(cards)` |
| `sample(seq, k)` | `k` phần tử **không lặp lại** | `random.sample(range(100), 5)` |
| `random()` | Số thực trong `[0, 1)` | `random.random()` |
| `uniform(a, b)` | Số thực trong `[a, b]` | `random.uniform(1.5, 2.5)` |
| `triangular(low, high, mode)` | Phân phối tam giác | `random.triangular(0, 10, 3)` |
| `betavariate(a, b)` | Phân phối Beta | |
| `expovariate(lambd)` | Phân phối mũ | |
| `gammavariate(a, b)` | Phân phối Gamma | |
| `gauss(mu, sigma)` / `normalvariate(mu, sigma)` | Phân phối chuẩn | `random.gauss(170, 10)` |
| `lognormvariate(mu, sigma)` | Phân phối log-chuẩn | |
| `vonmisesvariate(mu, kappa)` | Phân phối von Mises | |
| `paretovariate(alpha)` | Phân phối Pareto | |
| `weibullvariate(alpha, beta)` | Phân phối Weibull | |

```python
import random

random.seed(1)
print(random.randint(1, 6), random.choice("ABC"), random.sample(range(10), 3))
```

> ⚠️ Không dùng `random` cho mật khẩu/token bảo mật — dùng module `secrets`.

**Bài học liên quan:** [Python Numbers](../01_python_tutorial/015_python_numbers.ipynb) · [NumPy Random](../04_python_modules/numpy/017_random_intro.ipynb)
