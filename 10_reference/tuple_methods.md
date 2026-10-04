# Python Tuple Methods — Phương thức tuple

[📖 Reference](README.md) · [📚 Mục lục](../README.md) · W3Schools: [python_ref_tuple](https://www.w3schools.com/python/python_ref_tuple.asp)

Tuple **bất biến** nên chỉ có hai phương thức:

| Phương thức | Mô tả | Ví dụ (với `t = (1, 3, 7, 8, 7, 5)`) |
|---|---|---|
| `count(x)` | Số lần `x` xuất hiện | `t.count(7)` → `2` |
| `index(x)` | Vị trí đầu tiên của `x` (lỗi nếu không có) | `t.index(8)` → `3` |

### Thao tác khác với tuple

```python
t = ("apple",)                 # tuple 1 phần tử cần dấu phẩy
a, b, *rest = (1, 2, 3, 4)     # unpacking
t1 + t2                        # nối
t * 2                          # lặp
list(t) → sửa → tuple(...)     # "sửa" tuple
len(t) · min(t) · max(t) · sum(t) · sorted(t) · x in t
```

**Bài học liên quan:** [Python Tuples](../01_python_tutorial/046_python_tuples.ipynb) → [Tuple Methods](../01_python_tutorial/052_tuple_methods.ipynb)
