# Python List Methods — Phương thức list

[📖 Reference](README.md) · [📚 Mục lục](../README.md) · W3Schools: [python_ref_list](https://www.w3schools.com/python/python_ref_list.asp)

| Phương thức | Mô tả | Ví dụ (với `a = [3, 1, 2]`) | Trả về |
|---|---|---|---|
| `append(x)` | Thêm `x` vào cuối | `a.append(4)` → `[3, 1, 2, 4]` | `None` |
| `clear()` | Xoá mọi phần tử | `a.clear()` → `[]` | `None` |
| `copy()` | Bản sao nông | `b = a.copy()` | list mới |
| `count(x)` | Số lần `x` xuất hiện | `a.count(1)` → `1` | int |
| `extend(it)` | Thêm mọi phần tử của iterable | `a.extend([5, 6])` → `[3, 1, 2, 5, 6]` | `None` |
| `index(x)` | Chỉ số của `x` đầu tiên (lỗi nếu không có) | `a.index(2)` → `2` | int |
| `insert(i, x)` | Chèn `x` vào vị trí `i` | `a.insert(0, 9)` → `[9, 3, 1, 2]` | `None` |
| `pop(i=-1)` | Xoá và trả về phần tử ở `i` | `a.pop()` → `2` | phần tử |
| `remove(x)` | Xoá `x` đầu tiên (lỗi nếu không có) | `a.remove(1)` → `[3, 2]` | `None` |
| `reverse()` | Đảo ngược tại chỗ | `a.reverse()` → `[2, 1, 3]` | `None` |
| `sort(key, reverse)` | Sắp xếp tại chỗ | `a.sort(reverse=True)` → `[3, 2, 1]` | `None` |

> ⚠️ Các phương thức trả về `None` thay đổi list **tại chỗ** — đừng viết `a = a.sort()`.

### Hàm built-in hay dùng với list

`len(a)` · `min(a)` · `max(a)` · `sum(a)` · `sorted(a)` · `reversed(a)` · `enumerate(a)` · `zip(a, b)` · `list(...)` · `x in a`

### Độ phức tạp

| Thao tác | Big O |
|---|---|
| `a[i]`, `a[i] = x`, `append`, `pop()` | O(1) |
| `insert(0, x)`, `pop(0)`, `remove`, `index`, `x in a` | O(n) |
| `sort()` | O(n log n) |

**Bài học liên quan:** [Python Lists](../01_python_tutorial/035_python_lists.ipynb) → [List Methods](../01_python_tutorial/045_list_methods.ipynb)
