# Python Built-in Functions — Hàm có sẵn

[📖 Reference](README.md) · [📚 Mục lục](../README.md) · W3Schools: [python_ref_functions](https://www.w3schools.com/python/python_ref_functions.asp)

Python có sẵn các hàm sau — dùng được **không cần import**:

| Hàm | Mô tả | Ví dụ |
|---|---|---|
| `abs()` | Giá trị tuyệt đối | `abs(-7.25)` → `7.25` |
| `all()` | `True` nếu **mọi** phần tử của iterable là True | `all([1, 1, 0])` → `False` |
| `any()` | `True` nếu **có ít nhất một** phần tử True | `any([0, 0, 1])` → `True` |
| `ascii()` | Biểu diễn dễ đọc, thay ký tự non-ASCII bằng mã thoát | `print(ascii("Việt"))` in ra `'Vi\u1ec7t'` |
| `bin()` | Dạng nhị phân của số | `bin(6)` → `'0b110'` |
| `bool()` | Chuyển thành boolean | `bool("")` → `False` |
| `bytearray()` | Mảng byte (thay đổi được) | `bytearray(3)` |
| `bytes()` | Đối tượng bytes (bất biến) | `bytes("hi", "utf-8")` |
| `callable()` | `True` nếu object gọi được | `callable(print)` → `True` |
| `chr()` | Ký tự từ mã Unicode | `chr(97)` → `'a'` |
| `classmethod()` | Biến phương thức thành class method | dùng dạng `@classmethod` |
| `compile()` | Biên dịch mã nguồn thành code object | `compile("1+1", "", "eval")` |
| `complex()` | Tạo số phức | `complex(3, 5)` → `(3+5j)` |
| `delattr()` | Xoá thuộc tính của object | `delattr(obj, "age")` |
| `dict()` | Tạo dictionary | `dict(name="An", age=20)` |
| `dir()` | Danh sách thuộc tính/phương thức của object | `dir(str)` |
| `divmod()` | Thương và dư | `divmod(17, 5)` → `(3, 2)` |
| `enumerate()` | Duyệt kèm chỉ số | `list(enumerate("ab"))` → `[(0,'a'),(1,'b')]` |
| `eval()` | Đánh giá biểu thức dạng chuỗi ⚠️ | `eval("2 * 3")` → `6` |
| `exec()` | Thực thi code dạng chuỗi ⚠️ | `exec("x = 5")` |
| `filter()` | Lọc phần tử theo hàm | `list(filter(lambda x: x > 1, [1, 2, 3]))` → `[2, 3]` |
| `float()` | Chuyển thành số thực | `float("3.5")` → `3.5` |
| `format()` | Định dạng giá trị | `format(0.5, "%")` → `'50.000000%'` |
| `frozenset()` | Tạo frozenset | `frozenset([1, 2])` |
| `getattr()` | Lấy giá trị thuộc tính theo tên | `getattr(obj, "name", None)` |
| `globals()` | Dictionary các biến toàn cục | `globals()["x"]` |
| `hasattr()` | Object có thuộc tính không | `hasattr(obj, "name")` |
| `hash()` | Giá trị băm | `hash("abc")` |
| `help()` | Hiện tài liệu trợ giúp | `help(len)` |
| `hex()` | Dạng thập lục phân | `hex(255)` → `'0xff'` |
| `id()` | Định danh (địa chỉ) của object | `id(x)` |
| `input()` | Nhận dữ liệu người dùng (str) | `input("Tên: ")` |
| `int()` | Chuyển thành số nguyên | `int("42")` → `42` · `int("ff", 16)` → `255` |
| `isinstance()` | Object có thuộc kiểu không | `isinstance(5, int)` → `True` |
| `issubclass()` | Class có là lớp con không | `issubclass(bool, int)` → `True` |
| `iter()` | Tạo iterator | `it = iter([1, 2])` |
| `len()` | Độ dài | `len("abc")` → `3` |
| `list()` | Tạo list | `list("ab")` → `['a', 'b']` |
| `locals()` | Dictionary các biến cục bộ | `locals()` |
| `map()` | Áp dụng hàm cho từng phần tử | `list(map(str.upper, ["a", "b"]))` → `['A', 'B']` |
| `max()` | Giá trị lớn nhất | `max(3, 8, 1)` → `8` |
| `memoryview()` | Memory view của object bytes | `memoryview(b"abc")` |
| `min()` | Giá trị nhỏ nhất | `min([3, 8, 1])` → `1` |
| `next()` | Phần tử tiếp theo của iterator | `next(it)` |
| `object()` | Object cơ sở | `object()` |
| `oct()` | Dạng bát phân | `oct(8)` → `'0o10'` |
| `open()` | Mở file | `open("f.txt", encoding="utf-8")` |
| `ord()` | Mã Unicode của ký tự | `ord("a")` → `97` |
| `pow()` | Luỹ thừa (có thể kèm modulo) | `pow(2, 10)` → `1024` · `pow(2, 10, 7)` → `2` |
| `print()` | In ra màn hình | `print("a", "b", sep="-")` |
| `property()` | Tạo thuộc tính có getter/setter | dùng dạng `@property` |
| `range()` | Dãy số | `list(range(3))` → `[0, 1, 2]` |
| `repr()` | Biểu diễn "chính thức" | `repr("hi")` → `"'hi'"` |
| `reversed()` | Iterator đảo ngược | `list(reversed([1, 2]))` → `[2, 1]` |
| `round()` | Làm tròn | `round(3.14159, 2)` → `3.14` |
| `set()` | Tạo set | `set([1, 1, 2])` → `{1, 2}` |
| `setattr()` | Gán thuộc tính theo tên | `setattr(obj, "age", 20)` |
| `slice()` | Đối tượng cắt | `"python"[slice(0, 2)]` → `'py'` |
| `sorted()` | List mới đã sắp xếp | `sorted([3, 1, 2])` → `[1, 2, 3]` |
| `staticmethod()` | Biến phương thức thành static | dùng dạng `@staticmethod` |
| `str()` | Chuyển thành chuỗi | `str(3.0)` → `'3.0'` |
| `sum()` | Tổng | `sum([1, 2, 3])` → `6` |
| `super()` | Truy cập class cha | `super().__init__(...)` |
| `tuple()` | Tạo tuple | `tuple([1, 2])` → `(1, 2)` |
| `type()` | Kiểu của object | `type(5)` → `<class 'int'>` |
| `vars()` | `__dict__` của object | `vars(obj)` |
| `zip()` | Ghép nhiều iterable theo cặp | `list(zip("ab", [1, 2]))` → `[('a',1),('b',2)]` |

> ⚠️ `eval()` và `exec()` chạy **bất kỳ** code nào trong chuỗi — **không bao giờ** dùng với dữ liệu người dùng nhập.
>
> 📌 Python 3.10+ còn có `aiter()`, `anext()` (lập trình bất đồng bộ) và `breakpoint()` (gỡ lỗi).

**Bài học liên quan:** [Python Functions](../01_python_tutorial/080_python_functions.ipynb) · [Python Lambda](../01_python_tutorial/085_python_lambda.ipynb) · [Python Iterators](../01_python_tutorial/090_python_iterators.ipynb)
