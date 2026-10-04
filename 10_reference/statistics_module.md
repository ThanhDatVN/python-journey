# Python Statistics Module — Module statistics

[📖 Reference](README.md) · [📚 Mục lục](../README.md) · W3Schools: [module_statistics](https://www.w3schools.com/python/module_statistics.asp)

Module `statistics` (có sẵn) chứa các hàm thống kê cho dữ liệu số.

| Hàm | Mô tả | Ví dụ với `[1, 3, 5, 7, 9, 11]` |
|---|---|---|
| `mean()` | Trung bình cộng | `6` |
| `fmean()` | Trung bình cộng (float, nhanh hơn) | `6.0` |
| `geometric_mean()` | Trung bình nhân | `≈ 4.67` |
| `harmonic_mean()` | Trung bình điều hoà | `≈ 3.19` |
| `median()` | Trung vị | `6.0` |
| `median_low()` / `median_high()` | Trung vị thấp / cao | `5` / `7` |
| `median_grouped()` | Trung vị dữ liệu nhóm | |
| `mode()` | Yếu vị (giá trị xuất hiện nhiều nhất) | |
| `multimode()` | Mọi yếu vị | |
| `pstdev()` / `stdev()` | Độ lệch chuẩn tổng thể / mẫu | |
| `pvariance()` / `variance()` | Phương sai tổng thể / mẫu | |
| `quantiles()` | Chia dữ liệu thành các phân vị | |
| `correlation()` | Hệ số tương quan (3.10+) | |
| `covariance()` | Hiệp phương sai (3.10+) | |
| `linear_regression()` | Hồi quy tuyến tính đơn (3.10+) | |

```python
import statistics

data = [1, 3, 5, 7, 9, 11]
print(statistics.mean(data), statistics.median(data), statistics.stdev(data))
print(statistics.mode([1, 2, 2, 3]))
print(statistics.quantiles(data, n=4))
```

> 💡 `pstdev` chia cho `n` (cả tổng thể), `stdev` chia cho `n - 1` (mẫu). `numpy.std()` mặc định giống `pstdev`.

**Bài học liên quan:** [ML Mean Median Mode](../06_machine_learning/002_ml_mean_median_mode.ipynb) · [ML Standard Deviation](../06_machine_learning/003_ml_standard_deviation.ipynb)
