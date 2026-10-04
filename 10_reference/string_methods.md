# Python String Methods — Phương thức chuỗi

[📖 Reference](README.md) · [📚 Mục lục](../README.md) · W3Schools: [python_ref_string](https://www.w3schools.com/python/python_ref_string.asp)

> 📌 Mọi phương thức chuỗi **trả về giá trị mới** — chuỗi gốc không thay đổi (chuỗi là bất biến).

| Phương thức | Mô tả | Ví dụ → kết quả |
|---|---|---|
| `capitalize()` | Viết hoa ký tự đầu | `"hello world".capitalize()` → `'Hello world'` |
| `casefold()` | Chữ thường (mạnh hơn `lower`) | `"Straße".casefold()` → `'strasse'` |
| `center(w, c)` | Căn giữa trong độ rộng `w` | `"hi".center(6, "*")` → `'**hi**'` |
| `count(sub)` | Đếm số lần xuất hiện | `"banana".count("a")` → `3` |
| `encode()` | Mã hoá thành bytes | `"Việt".encode()` → `b'Vi\xe1\xbb\x87t'` |
| `endswith(x)` | Kết thúc bằng `x`? | `"a.py".endswith(".py")` → `True` |
| `expandtabs(n)` | Đặt độ rộng tab | `"a\tb".expandtabs(4)` → `'a   b'` |
| `find(sub)` | Vị trí đầu tiên, `-1` nếu không có | `"hello".find("l")` → `2` |
| `format()` | Định dạng | `"{} + {}".format(1, 2)` → `'1 + 2'` |
| `format_map(d)` | Định dạng từ dict | `"{x}".format_map({"x": 5})` → `'5'` |
| `index(sub)` | Như `find` nhưng **lỗi** nếu không có | `"hello".index("e")` → `1` |
| `isalnum()` | Chỉ chữ và số? | `"abc123".isalnum()` → `True` |
| `isalpha()` | Chỉ chữ cái? | `"abc".isalpha()` → `True` |
| `isascii()` | Chỉ ký tự ASCII? | `"Việt".isascii()` → `False` |
| `isdecimal()` | Chỉ chữ số thập phân? | `"123".isdecimal()` → `True` |
| `isdigit()` | Chỉ chữ số? | `"123".isdigit()` → `True` |
| `isidentifier()` | Là tên định danh hợp lệ? | `"my_var".isidentifier()` → `True` |
| `islower()` | Toàn chữ thường? | `"abc".islower()` → `True` |
| `isnumeric()` | Chỉ ký tự số? | `"½".isnumeric()` → `True` |
| `isprintable()` | In được hết? | `"a\n".isprintable()` → `False` |
| `isspace()` | Chỉ khoảng trắng? | `"   ".isspace()` → `True` |
| `istitle()` | Dạng tiêu đề? | `"Hello World".istitle()` → `True` |
| `isupper()` | Toàn chữ hoa? | `"ABC".isupper()` → `True` |
| `join(iter)` | Nối các phần tử bằng chuỗi này | `"-".join(["a", "b"])` → `'a-b'` |
| `ljust(w, c)` | Căn trái | `"hi".ljust(5, ".")` → `'hi...'` |
| `lower()` | Chữ thường | `"ABC".lower()` → `'abc'` |
| `lstrip()` | Xoá khoảng trắng bên trái | `"  hi".lstrip()` → `'hi'` |
| `maketrans()` | Tạo bảng chuyển đổi | `str.maketrans("ae", "AE")` |
| `partition(sep)` | Tách thành 3 phần | `"a=b".partition("=")` → `('a', '=', 'b')` |
| `removeprefix(p)` | Bỏ tiền tố (3.9+) | `"test_a".removeprefix("test_")` → `'a'` |
| `removesuffix(s)` | Bỏ hậu tố (3.9+) | `"a.txt".removesuffix(".txt")` → `'a'` |
| `replace(a, b)` | Thay thế | `"aaa".replace("a", "b", 2)` → `'bba'` |
| `rfind(sub)` | Vị trí cuối cùng, `-1` nếu không có | `"hello".rfind("l")` → `3` |
| `rindex(sub)` | Như `rfind` nhưng lỗi nếu không có | `"hello".rindex("l")` → `3` |
| `rjust(w, c)` | Căn phải | `"7".rjust(3, "0")` → `'007'` |
| `rpartition(sep)` | Tách 3 phần từ bên phải | `"a.b.c".rpartition(".")` → `('a.b', '.', 'c')` |
| `rsplit(sep, n)` | Tách từ bên phải | `"a,b,c".rsplit(",", 1)` → `['a,b', 'c']` |
| `rstrip()` | Xoá khoảng trắng bên phải | `"hi  ".rstrip()` → `'hi'` |
| `split(sep, n)` | Tách thành list | `"a,b,c".split(",")` → `['a', 'b', 'c']` |
| `splitlines()` | Tách theo dòng | `"a\nb".splitlines()` → `['a', 'b']` |
| `startswith(x)` | Bắt đầu bằng `x`? | `"Hello".startswith("He")` → `True` |
| `strip()` | Xoá khoảng trắng hai đầu | `"  hi  ".strip()` → `'hi'` |
| `swapcase()` | Đảo hoa/thường | `"Hi".swapcase()` → `'hI'` |
| `title()` | Hoa chữ cái đầu mỗi từ | `"hello world".title()` → `'Hello World'` |
| `translate(t)` | Chuyển đổi theo bảng | `"abc".translate(str.maketrans("a", "A"))` → `'Abc'` |
| `upper()` | Chữ hoa | `"abc".upper()` → `'ABC'` |
| `zfill(w)` | Thêm số 0 bên trái | `"42".zfill(5)` → `'00042'` |

**Bài học liên quan:** [Python Strings](../01_python_tutorial/017_python_strings.ipynb) · [Modify Strings](../01_python_tutorial/019_modify_strings.ipynb) · [String Methods](../01_python_tutorial/023_string_methods.ipynb)
