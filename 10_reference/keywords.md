# Python Keywords — Từ khoá

[📖 Reference](README.md) · [📚 Mục lục](../README.md) · W3Schools: [python_ref_keywords](https://www.w3schools.com/python/python_ref_keywords.asp)

Từ khoá là các từ **dành riêng** — không dùng làm tên biến, hàm hay class.

| Từ khoá | Ý nghĩa | Bài học |
|---|---|---|
| `and` | Toán tử logic "và" | [Logical Operators](../01_python_tutorial/030_logical_operators.ipynb) |
| `as` | Đặt bí danh (`import x as y`, `with ... as f`, `except E as e`) | [Modules](../01_python_tutorial/091_python_modules.ipynb) |
| `assert` | Kiểm tra điều kiện khi gỡ lỗi (lỗi `AssertionError` nếu sai) | |
| `async` / `await` | Lập trình bất đồng bộ | |
| `break` | Thoát khỏi vòng lặp | [While Loops](../01_python_tutorial/078_python_while_loops.ipynb) |
| `class` | Định nghĩa class | [Classes/Objects](../02_python_classes/002_python_classes_objects.ipynb) |
| `continue` | Bỏ qua phần còn lại của vòng lặp hiện tại | [For Loops](../01_python_tutorial/079_python_for_loops.ipynb) |
| `def` | Định nghĩa hàm | [Functions](../01_python_tutorial/080_python_functions.ipynb) |
| `del` | Xoá object/phần tử | [Remove List Items](../01_python_tutorial/039_remove_list_items.ipynb) |
| `elif` | "else if" | [Python Elif](../01_python_tutorial/071_python_elif.ipynb) |
| `else` | Nhánh còn lại (if, for, while, try) | [Python Else](../01_python_tutorial/072_python_else.ipynb) |
| `except` | Bắt lỗi | [Try Except](../01_python_tutorial/097_python_try_except.ipynb) |
| `False` / `True` | Giá trị boolean | [Booleans](../01_python_tutorial/024_python_booleans.ipynb) |
| `finally` | Khối luôn chạy sau try | [Try Except](../01_python_tutorial/097_python_try_except.ipynb) |
| `for` | Vòng lặp for | [For Loops](../01_python_tutorial/079_python_for_loops.ipynb) |
| `from` | Import một phần của module | [Modules](../01_python_tutorial/091_python_modules.ipynb) |
| `global` | Khai báo biến toàn cục | [Global Variables](../01_python_tutorial/013_global_variables.ipynb) |
| `if` | Câu lệnh điều kiện | [Python If](../01_python_tutorial/070_python_if.ipynb) |
| `import` | Nạp module | [Modules](../01_python_tutorial/091_python_modules.ipynb) |
| `in` | Kiểm tra thành viên / duyệt trong for | [Membership](../01_python_tutorial/032_membership_operators.ipynb) |
| `is` | Kiểm tra cùng object | [Identity](../01_python_tutorial/031_identity_operators.ipynb) |
| `lambda` | Hàm vô danh | [Lambda](../01_python_tutorial/085_python_lambda.ipynb) |
| `None` | Giá trị rỗng | [None](../01_python_tutorial/099_python_none.ipynb) |
| `nonlocal` | Biến của hàm bao ngoài | [Scope](../01_python_tutorial/083_python_scope.ipynb) |
| `not` | Toán tử logic "không" | [Logical Operators](../01_python_tutorial/030_logical_operators.ipynb) |
| `or` | Toán tử logic "hoặc" | [Logical Operators](../01_python_tutorial/030_logical_operators.ipynb) |
| `pass` | Câu lệnh rỗng | [Pass](../01_python_tutorial/076_pass_statement.ipynb) |
| `raise` | Phát sinh lỗi | [Try Except](../01_python_tutorial/097_python_try_except.ipynb) |
| `return` | Trả về giá trị từ hàm | [Functions](../01_python_tutorial/080_python_functions.ipynb) |
| `try` | Khối thử (xử lý lỗi) | [Try Except](../01_python_tutorial/097_python_try_except.ipynb) |
| `while` | Vòng lặp while | [While Loops](../01_python_tutorial/078_python_while_loops.ipynb) |
| `with` | Quản lý ngữ cảnh (tự đóng file…) | [Read Files](../03_file_handling/002_python_read_files.ipynb) |
| `yield` | Trả giá trị từ generator | [Generators](../01_python_tutorial/087_python_generators.ipynb) |

### Soft keywords (Python 3.10+)

Chỉ là từ khoá trong ngữ cảnh đặc biệt — ngoài ngữ cảnh đó vẫn dùng làm tên được: `match`, `case`, `_` ([Python Match](../01_python_tutorial/077_python_match.ipynb)), và `type` (3.12+, khai báo kiểu).

```python
import keyword
print(len(keyword.kwlist), keyword.kwlist)
print(keyword.softkwlist)
```
