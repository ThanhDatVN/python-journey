# ⭐ Python Cheat Sheet — Một trang ghi nhớ

[📖 Reference](README.md) · [📚 Mục lục](../README.md)

## 1. Cơ bản

```python
print("Hello", 42, sep=" | ", end="\n")   # in ra màn hình
# comment một dòng
x = 5                  # tạo biến (không cần khai báo kiểu)
a, b, c = 1, 2, 3      # gán nhiều biến
a, b = b, a            # hoán đổi
type(x)                # xem kiểu
int("3") float("2.5") str(10) bool(0)   # ép kiểu
name = input("Tên: ")  # nhập — luôn trả về str
```

## 2. Kiểu dữ liệu

| Kiểu | Ví dụ | Đặc điểm |
|---|---|---|
| `int` / `float` / `complex` | `5`, `2.5`, `1j` | Số |
| `str` | `"hi"`, `'hi'`, `"""..."""` | Chuỗi, **bất biến** |
| `bool` | `True`, `False` | Falsy: `0 "" [] () {} None False` |
| `list` | `[1, 2, 3]` | Có thứ tự · thay đổi được · trùng lặp |
| `tuple` | `(1, 2)`, `(1,)` | Có thứ tự · **bất biến** · trùng lặp |
| `set` | `{1, 2}`, `set()` | **Không** thứ tự · **không** trùng |
| `dict` | `{"k": "v"}` | Key–value · có thứ tự (3.7+) · không trùng key |
| `None` | `None` | Không có giá trị — so sánh bằng `is None` |

## 3. Chuỗi

```python
s = "Hello, World!"
s[0]  s[-1]  s[2:5]  s[::-1]          # chỉ số & cắt
len(s)   "World" in s                  # độ dài, kiểm tra
s.upper() s.lower() s.strip() s.replace("H", "J") s.split(",")
" ".join(["a", "b"])                   # nối list chuỗi
f"{name} có {price:,.2f} đ"            # f-string
"\n" "\t" "\\" "\""                    # ký tự thoát · r"C:\path" raw string
```

## 4. Toán tử

```text
Số học:   +  -  *  /  //  %  **         (/ luôn ra float; // chia lấy nguyên)
Gán:      =  +=  -=  *=  /=  :=          (walrus)
So sánh:  ==  !=  >  <  >=  <=   (nối tiếp: 0 < x < 10)
Logic:    and  or  not
Định danh: is  is not             Thành viên: in  not in
Bitwise:  &  |  ^  ~  <<  >>
Ưu tiên:  ()  >  **  >  * / // %  >  + -  >  so sánh  >  not  >  and  >  or
Ternary:  a if điều_kiện else b
```

## 5. List · Tuple · Set · Dict

```python
L = [3, 1, 2]
L.append(4) L.insert(0, 9) L.extend([5, 6])     # thêm
L.remove(9) L.pop() L.pop(0) del L[0] L.clear()  # xoá
L.sort() L.sort(reverse=True, key=len) sorted(L) L.reverse()
L.index(x) L.count(x) L.copy()  L2 = L[:]        # ⚠️ L2 = L không sao chép!
[x * 2 for x in L if x > 1]                      # list comprehension

t = (1, 2, 3);  a, *rest = t                     # unpacking
s = {1, 2}; s.add(3); s.discard(9); s | t2  s & t2  s - t2  s ^ t2

d = {"name": "An", "age": 20}
d["name"]  d.get("x", "mặc định")  d["city"] = "Huế"  d.update({...})
d.pop("age")  d.keys() d.values() d.items()
for k, v in d.items(): ...
{k: v for k, v in d.items() if v}               # dict comprehension
```

## 6. Điều kiện & vòng lặp

```python
if x > 0:
    ...
elif x == 0:
    ...
else:
    ...

match command:              # Python 3.10+
    case "start" | "go": ...
    case _: ...             # mặc định

while i < 5:
    i += 1                  # ⚠️ nhớ cập nhật biến điều khiển
for i in range(2, 10, 2):   # range(start, stop, step) — không gồm stop
    if i == 6: break        # dừng vòng lặp
    if i == 4: continue     # bỏ qua vòng hiện tại
else:
    ...                     # chạy khi không break
for i, item in enumerate(L): ...
for a, b in zip(list1, list2): ...
```

## 7. Hàm

```python
def greet(name, greeting="Hello", *args, **kwargs):
    """Docstring mô tả hàm."""
    return f"{greeting}, {name}"

greet("An")                  greet(greeting="Hi", name="An")
square = lambda x: x ** 2    # hàm vô danh
sorted(people, key=lambda p: p[1])

def outer():
    count = 0
    def inner():
        nonlocal count       # global x: biến toàn cục
        count += 1
    ...

def gen():                   # generator
    yield 1
    yield 2

@decorator                   # ⇔ f = decorator(f)
def f(): ...
```

## 8. Class (OOP)

```python
class Person:
    species = "Human"                     # thuộc tính class (dùng chung)

    def __init__(self, name, age):        # hàm khởi tạo
        self.name = name                  # thuộc tính object
        self.__age = age                  # private (name mangling)

    def greet(self):                      # phương thức
        return f"Hi, I'm {self.name}"

    def __str__(self):                    # print(obj)
        return f"{self.name} ({self.__age})"

class Student(Person):                    # kế thừa
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.year = year

    def greet(self):                      # ghi đè (đa hình)
        return super().greet() + f", class of {self.year}"
```

Magic methods: `__init__ __str__ __repr__ __eq__ __lt__ __add__ __len__ __contains__ __call__ __iter__ __next__`

## 9. Lỗi & file

```python
try:
    x = 10 / int(value)
except ZeroDivisionError:
    ...
except (ValueError, TypeError) as e:
    print("Lỗi:", e)
else:
    ...          # khi không lỗi
finally:
    ...          # luôn chạy
raise ValueError("thông báo")

with open("file.txt", "r", encoding="utf-8") as f:   # r · w · a · x  (+ b)
    content = f.read()        # f.readline() · for line in f · f.readlines()
with open("out.txt", "w", encoding="utf-8") as f:
    f.write("Dòng mới\n")

import os
os.path.exists("file.txt");  os.remove("file.txt")
```

## 10. Module hay dùng

```python
import math;      math.sqrt(16) math.ceil(1.2) math.floor(1.8) math.pi
import random;    random.randint(1, 6) random.choice(L) random.shuffle(L)
import datetime;  datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
import json;      json.loads(text)  json.dumps(obj, indent=4, ensure_ascii=False)
import re;        re.findall(r"\d+", s)  re.sub(r"\s", "-", s)
from collections import Counter, deque, defaultdict
```

```bash
pip install tên_package        python -m venv .venv        pip install -r requirements.txt
```
