# Python Built-in Exceptions — Các loại lỗi có sẵn

[📖 Reference](README.md) · [📚 Mục lục](../README.md) · W3Schools: [python_ref_exceptions](https://www.w3schools.com/python/python_ref_exceptions.asp)

| Exception | Khi nào xảy ra | Ví dụ gây lỗi |
|---|---|---|
| `ArithmeticError` | Lớp cha của các lỗi tính toán | |
| `AssertionError` | Câu lệnh `assert` sai | `assert 1 > 2` |
| `AttributeError` | Truy cập thuộc tính/phương thức không tồn tại | `"abc".push("d")` |
| `EOFError` | `input()` gặp kết thúc dữ liệu | |
| `Exception` | Lớp cha của hầu hết các lỗi | |
| `FileNotFoundError` | Mở file không tồn tại | `open("khong_co.txt")` |
| `FloatingPointError` | Phép tính số thực thất bại | |
| `GeneratorExit` | Generator bị đóng (`close()`) | |
| `ImportError` | Import thất bại | `from math import abcxyz` |
| `IndentationError` | Thụt lề sai | thiếu thụt lề sau `if` |
| `IndexError` | Chỉ số vượt phạm vi | `[1, 2][5]` |
| `KeyError` | Key không có trong dictionary | `{"a": 1}["b"]` |
| `KeyboardInterrupt` | Người dùng nhấn `Ctrl + C` / Interrupt | |
| `LookupError` | Lớp cha của `IndexError`, `KeyError` | |
| `MemoryError` | Hết bộ nhớ | |
| `ModuleNotFoundError` | Không tìm thấy module | `import khong_ton_tai` |
| `NameError` | Dùng biến chưa định nghĩa | `print(x_chua_co)` |
| `NotImplementedError` | Phương thức "trừu tượng" chưa được cài đặt | |
| `OSError` | Lỗi hệ thống (file, quyền…) | |
| `OverflowError` | Kết quả số thực quá lớn | `2.0 ** 10000` |
| `PermissionError` | Không có quyền truy cập file | |
| `RecursionError` | Đệ quy quá sâu | hàm gọi mãi không dừng |
| `ReferenceError` | Object đã bị giải phóng (weak reference) | |
| `RuntimeError` | Lỗi không thuộc nhóm nào khác | |
| `StopIteration` | `next()` khi iterator hết phần tử | `next(iter([]))` |
| `SyntaxError` | Sai cú pháp | `print("thiếu ngoặc"` |
| `SystemError` | Lỗi nội bộ của trình thông dịch | |
| `SystemExit` | `sys.exit()` được gọi | |
| `TabError` | Trộn tab và khoảng trắng khi thụt lề | |
| `TimeoutError` | Hết thời gian chờ | |
| `TypeError` | Phép toán với kiểu không phù hợp | `"2" + 2` |
| `UnboundLocalError` | Dùng biến cục bộ trước khi gán | đọc `x` rồi mới `x = ...` trong hàm |
| `UnicodeError` / `UnicodeDecodeError` / `UnicodeEncodeError` | Lỗi mã hoá ký tự | đọc file UTF-8 bằng encoding khác |
| `ValueError` | Giá trị đúng kiểu nhưng không hợp lệ | `int("abc")` |
| `ZeroDivisionError` | Chia cho 0 | `1 / 0` |

### Cây kế thừa rút gọn

```text
BaseException
 ├── SystemExit · KeyboardInterrupt · GeneratorExit
 └── Exception
      ├── ArithmeticError → ZeroDivisionError, OverflowError
      ├── LookupError → IndexError, KeyError
      ├── OSError → FileNotFoundError, PermissionError, TimeoutError
      ├── ValueError → UnicodeError
      ├── TypeError · NameError · AttributeError · ImportError → ModuleNotFoundError
      ├── RuntimeError → RecursionError, NotImplementedError
      └── SyntaxError → IndentationError → TabError
```

> 💡 Bắt lỗi **cụ thể** (`except ValueError:`) tốt hơn bắt chung (`except:`). Bắt lớp cha sẽ bắt cả các lớp con: `except LookupError` bắt cả `IndexError` và `KeyError`.

**Bài học liên quan:** [Python Try Except](../01_python_tutorial/097_python_try_except.ipynb)
