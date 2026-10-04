# Python Set Methods — Phương thức set

[📖 Reference](README.md) · [📚 Mục lục](../README.md) · W3Schools: [python_ref_set](https://www.w3schools.com/python/python_ref_set.asp)

| Phương thức | Toán tử | Mô tả |
|---|---|---|
| `add(x)` | | Thêm một phần tử |
| `clear()` | | Xoá mọi phần tử |
| `copy()` | | Bản sao |
| `difference(*others)` | `-` | Phần tử có ở set này mà không có ở set khác |
| `difference_update(*others)` | `-=` | Xoá khỏi set này các phần tử có ở set khác |
| `discard(x)` | | Xoá `x` (không lỗi nếu không có) |
| `intersection(*others)` | `&` | Phần tử chung |
| `intersection_update(*others)` | `&=` | Chỉ giữ phần tử chung |
| `isdisjoint(other)` | | `True` nếu không có phần tử chung |
| `issubset(other)` | `<=` | `True` nếu là tập con (`<`: tập con thực sự) |
| `issuperset(other)` | `>=` | `True` nếu là tập cha (`>`: tập cha thực sự) |
| `pop()` | | Xoá và trả về một phần tử **bất kỳ** |
| `remove(x)` | | Xoá `x` (**lỗi** nếu không có) |
| `symmetric_difference(other)` | `^` | Phần tử chỉ có ở một trong hai set |
| `symmetric_difference_update(other)` | `^=` | Cập nhật bằng hiệu đối xứng |
| `union(*others)` | `\|` | Hợp các set |
| `update(*others)` | `\|=` | Thêm phần tử từ set/iterable khác |

```python
a = {1, 2, 3}
b = {3, 4}
a | b   # {1, 2, 3, 4}
a & b   # {3}
a - b   # {1, 2}
a ^ b   # {1, 2, 4}
```

> 📌 `{}` là **dict rỗng**; set rỗng phải viết `set()`. Phiên bản bất biến: `frozenset()`.

**Bài học liên quan:** [Python Sets](../01_python_tutorial/053_python_sets.ipynb) → [Join Sets](../01_python_tutorial/058_join_sets.ipynb) → [Set Methods](../01_python_tutorial/060_set_methods.ipynb)
