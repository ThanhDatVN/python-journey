# Python Requests Module — Module requests

[📖 Reference](README.md) · [📚 Mục lục](../README.md) · W3Schools: [module_requests](https://www.w3schools.com/python/module_requests.asp)

Module `requests` dùng để **gửi HTTP request** (lấy dữ liệu từ website, gọi API…). Đây là package ngoài, cần cài:

```bash
pip install requests
```

```python
import requests

x = requests.get('https://www.w3schools.com/python/demopage.htm')
print(x.status_code)
print(x.text[:200])
```

## Các phương thức

| Phương thức | Mô tả |
|---|---|
| `delete(url, args)` | Gửi DELETE request |
| `get(url, params, args)` | Gửi GET request — **lấy** dữ liệu |
| `head(url, args)` | Gửi HEAD request — chỉ lấy header |
| `patch(url, data, args)` | Gửi PATCH request — sửa một phần |
| `post(url, data, json, args)` | Gửi POST request — **gửi** dữ liệu |
| `put(url, data, args)` | Gửi PUT request — thay thế dữ liệu |
| `request(method, url, args)` | Gửi request với phương thức chỉ định |

Tham số `args` hay dùng: `params` (query string), `headers`, `json`, `data`, `timeout`, `auth`, `cookies`.

## Response object — Đối tượng phản hồi

| Thuộc tính / phương thức | Mô tả |
|---|---|
| `status_code` | Mã trạng thái (200 OK, 404 Not Found…) |
| `ok` | `True` nếu `status_code < 400` |
| `text` | Nội dung dạng chuỗi |
| `content` | Nội dung dạng bytes |
| `json()` | Đọc nội dung JSON thành dict/list |
| `headers` | Header phản hồi |
| `encoding` | Bảng mã |
| `url` | URL cuối cùng |
| `raise_for_status()` | Báo lỗi nếu mã trạng thái là lỗi |

```python
import requests

r = requests.get("https://api.github.com/repos/python/cpython", timeout=10)
if r.ok:
    data = r.json()
    print(data["full_name"], "⭐", data["stargazers_count"])
```

> 💡 Luôn đặt `timeout=` để chương trình không bị treo khi server không phản hồi.
