# Python Dictionary Methods — Phương thức dictionary

[📖 Reference](README.md) · [📚 Mục lục](../README.md) · W3Schools: [python_ref_dictionary](https://www.w3schools.com/python/python_ref_dictionary.asp)

| Phương thức | Mô tả | Ví dụ (với `d = {"a": 1, "b": 2}`) |
|---|---|---|
| `clear()` | Xoá mọi phần tử | `d.clear()` → `{}` |
| `copy()` | Bản sao nông | `d2 = d.copy()` |
| `fromkeys(keys, v)` | Tạo dict từ danh sách key | `dict.fromkeys(["x", "y"], 0)` → `{'x': 0, 'y': 0}` |
| `get(k, default)` | Lấy value, không lỗi nếu thiếu key | `d.get("z", 0)` → `0` |
| `items()` | View các cặp `(key, value)` | `list(d.items())` → `[('a', 1), ('b', 2)]` |
| `keys()` | View các key | `list(d.keys())` → `['a', 'b']` |
| `pop(k, default)` | Xoá key, trả về value | `d.pop("a")` → `1` |
| `popitem()` | Xoá và trả về cặp **thêm vào cuối cùng** | `d.popitem()` → `('b', 2)` |
| `setdefault(k, v)` | Trả về value; thêm `k: v` nếu chưa có | `d.setdefault("c", 3)` → `3` |
| `update(other)` | Cập nhật/thêm từ dict hoặc cặp key-value | `d.update({"a": 10})` |
| `values()` | View các value | `list(d.values())` → `[1, 2]` |

### Cú pháp hay dùng

```python
d["key"]                 # lỗi KeyError nếu thiếu key
d["key"] = value         # thêm hoặc sửa
del d["key"]             # xoá
"key" in d               # kiểm tra key
d1 | d2                  # gộp (3.9+)
{k: v for k, v in d.items() if v > 1}   # dict comprehension
counts[x] = counts.get(x, 0) + 1        # đếm tần suất
```

**Bài học liên quan:** [Python Dictionaries](../01_python_tutorial/061_python_dictionaries.ipynb) → [Dictionary Methods](../01_python_tutorial/069_dictionary_methods.ipynb)
