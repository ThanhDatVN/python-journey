# Python File Methods — Phương thức file

[📖 Reference](README.md) · [📚 Mục lục](../README.md) · W3Schools: [python_ref_file](https://www.w3schools.com/python/python_ref_file.asp)

`f = open("file.txt", mode, encoding="utf-8")` trả về một **file object** với các phương thức:

| Phương thức | Mô tả |
|---|---|
| `close()` | Đóng file |
| `detach()` | Tách và trả về luồng nhị phân bên dưới |
| `fileno()` | Số mô tả file (file descriptor) |
| `flush()` | Đẩy dữ liệu trong bộ đệm ra file |
| `isatty()` | `True` nếu luồng là terminal tương tác |
| `read(n)` | Đọc toàn bộ (hoặc `n` ký tự) |
| `readable()` | `True` nếu đọc được |
| `readline()` | Đọc một dòng |
| `readlines()` | Đọc mọi dòng thành list |
| `seek(pos)` | Di chuyển vị trí đọc/ghi |
| `seekable()` | `True` nếu đổi được vị trí |
| `tell()` | Vị trí hiện tại |
| `truncate(size)` | Cắt file về kích thước chỉ định |
| `writable()` | `True` nếu ghi được |
| `write(s)` | Ghi chuỗi `s` |
| `writelines(list)` | Ghi một list chuỗi |

### Chế độ mở file

| Mode | Ý nghĩa |
|---|---|
| `"r"` | Đọc (mặc định) — lỗi nếu file không tồn tại |
| `"w"` | Ghi đè — tạo file nếu chưa có |
| `"a"` | Ghi thêm vào cuối — tạo file nếu chưa có |
| `"x"` | Tạo mới — lỗi nếu file đã tồn tại |
| `"t"` / `"b"` | Văn bản (mặc định) / nhị phân |
| `"+"` | Vừa đọc vừa ghi (ví dụ `"r+"`) |

```python
with open("file.txt", encoding="utf-8") as f:   # tự đóng file
    for line in f:
        print(line.strip())
```

> 🇻🇳 Luôn thêm `encoding="utf-8"` khi làm việc với file tiếng Việt.

**Bài học liên quan:** [File Handling](../03_file_handling/001_python_file_handling.ipynb) · [Read Files](../03_file_handling/002_python_read_files.ipynb) · [Write/Create Files](../03_file_handling/003_python_write_create_files.ipynb) · [Delete Files](../03_file_handling/004_python_delete_files.ipynb)
