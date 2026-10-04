# Python Built-in Modules — Thư viện chuẩn

[📖 Reference](README.md) · [📚 Mục lục](../README.md) · W3Schools: [python_modules](https://www.w3schools.com/python/python_modules.asp)

Python đi kèm **thư viện chuẩn (standard library)** rất lớn — dùng ngay bằng `import`, không cần cài thêm. Một số module hay dùng:

| Module | Dùng để | Ví dụ |
|---|---|---|
| `math` | Toán học | `math.sqrt(16)` — xem [Math Module](math_module.md) |
| `cmath` | Toán học số phức | `cmath.sqrt(-1)` — xem [cMath Module](cmath_module.md) |
| `random` | Số ngẫu nhiên | `random.randint(1, 6)` — xem [Random Module](random_module.md) |
| `statistics` | Thống kê | `statistics.mean([1, 2, 3])` — xem [Statistics Module](statistics_module.md) |
| `datetime` | Ngày giờ | `datetime.date.today()` |
| `time` | Thời gian, đo thời gian chạy | `time.perf_counter()` |
| `calendar` | Lịch | `calendar.isleap(2028)` |
| `json` | Đọc/ghi JSON | `json.loads(text)` |
| `csv` | Đọc/ghi CSV | `csv.reader(f)` |
| `re` | Biểu thức chính quy | `re.findall(r"\d+", s)` |
| `os` | Làm việc với hệ điều hành, file | `os.listdir(".")` |
| `os.path` / `pathlib` | Đường dẫn file | `Path("a/b.txt").suffix` |
| `shutil` | Sao chép/di chuyển/xoá thư mục | `shutil.copy(a, b)` |
| `sys` | Thông tin trình thông dịch | `sys.version`, `sys.argv` |
| `platform` | Thông tin hệ thống | `platform.system()` |
| `collections` | Cấu trúc dữ liệu nâng cao | `Counter`, `deque`, `defaultdict`, `namedtuple` |
| `itertools` | Công cụ lặp | `itertools.permutations([1, 2, 3])` |
| `functools` | Công cụ cho hàm | `functools.wraps`, `lru_cache`, `reduce` |
| `copy` | Sao chép nông/sâu | `copy.deepcopy(obj)` |
| `string` | Hằng chuỗi | `string.ascii_letters` |
| `textwrap` | Định dạng đoạn văn | `textwrap.wrap(text, 40)` |
| `unicodedata` | Thông tin ký tự Unicode | `unicodedata.normalize("NFC", s)` |
| `decimal` / `fractions` | Số thập phân chính xác / phân số | `Decimal("0.1") + Decimal("0.2")` |
| `array` | Mảng số cùng kiểu | `array.array("i", [1, 2])` |
| `heapq` | Hàng đợi ưu tiên (heap) | `heapq.heappush(h, x)` |
| `bisect` | Tìm kiếm nhị phân trên list đã sắp xếp | `bisect.insort(a, x)` |
| `sqlite3` | Cơ sở dữ liệu SQLite | `sqlite3.connect("db.sqlite")` |
| `urllib` | Làm việc với URL | `urllib.parse.urlparse(url)` |
| `http.server` | Web server đơn giản | `python -m http.server` |
| `logging` | Ghi log | `logging.info("...")` |
| `unittest` | Kiểm thử | `unittest.TestCase` |
| `venv` | Môi trường ảo | `python -m venv .venv` |
| `zipfile` | Nén/giải nén zip | `zipfile.ZipFile("a.zip")` |
| `hashlib` | Băm (MD5, SHA…) | `hashlib.sha256(b"abc").hexdigest()` |
| `secrets` | Số ngẫu nhiên an toàn (mật khẩu, token) | `secrets.token_hex(16)` |
| `uuid` | Mã định danh duy nhất | `uuid.uuid4()` |
| `tkinter` | Giao diện đồ hoạ (GUI) | `tkinter.Tk()` |

Liệt kê mọi module có sẵn trên máy (chạy trong notebook):

```python
help("modules")
```

Xem nội dung một module:

```python
import platform
print(dir(platform))
```

> 📌 Package **ngoài** thư viện chuẩn (như `requests`, `numpy`, `pandas`) cần cài bằng `pip install`.

**Bài học liên quan:** [Python Modules](../01_python_tutorial/091_python_modules.ipynb) · [Python PIP](../01_python_tutorial/096_python_pip.ipynb)
