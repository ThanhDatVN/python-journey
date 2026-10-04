"""Tiện ích cho các notebook Django của khóa học.

- setup()      : nạp Django của dự án my_tennis_club để dùng ORM ngay trong notebook
- preview(url) : "mở" một trang web bằng test client của Django (không cần runserver)
- edit_file()  : sửa một đoạn trong file cấu hình (settings.py, urls.py...)
- show_file()  : in nội dung một file
"""
import os
import sys
from pathlib import Path

PROJECT = "my_tennis_club"


def setup():
    """Cấu hình Django để dùng models trong notebook."""
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"  # Jupyter chạy trong một event loop
    path = os.path.abspath(PROJECT)
    if path not in sys.path:
        sys.path.insert(0, path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{PROJECT}.settings")
    import django
    django.setup()


def preview(url, show_html=True, max_chars=2500):
    """Gửi request GET tới url và in mã trạng thái + HTML trả về."""
    setup()
    from django.conf import settings
    from django.test import Client
    if "testserver" not in settings.ALLOWED_HOSTS and "*" not in settings.ALLOWED_HOSTS:
        settings.ALLOWED_HOSTS = [*settings.ALLOWED_HOSTS, "testserver"]
    response = Client().get(url)
    print(f"GET {url}  ->  {response.status_code}")
    if response.status_code in (301, 302):
        print("Chuyển hướng tới:", response["Location"])
    if show_html and response.status_code not in (301, 302):
        if hasattr(response, "streaming_content"):
            text = b"".join(response.streaming_content).decode("utf-8")
        else:
            text = response.content.decode("utf-8")
        print(text[:max_chars] + ("\n..." if len(text) > max_chars else ""))


def edit_file(path, old, new):
    """Thay đoạn `old` bằng `new` trong file (chỉ sửa một lần, chạy lại không sao)."""
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    if new in text:
        print(f"✔ {path}: đã có nội dung mới từ trước")
        return
    if old not in text:
        raise ValueError(f"Không tìm thấy đoạn cần sửa trong {path}:\n{old}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8")
    print(f"✔ Đã sửa {path}")


def replace_view(name, code, path=f"{PROJECT}/members/views.py"):
    """Thay hàm view `name` trong views.py bằng `code` (thêm mới nếu chưa có)."""
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    code = code.strip("\n") + "\n"
    start = text.find(f"\ndef {name}(")
    if start == -1:
        text = text.rstrip("\n") + "\n\n" + code
    else:
        end = text.find("\ndef ", start + 1)
        text = text[:start + 1] + code + ("\n" + text[end + 1:] if end != -1 else "")
    p.write_text(text, encoding="utf-8")
    print(f"✔ Đã cập nhật view {name}() trong {path}")


def show_file(path, start=None, end=None):
    """In nội dung file; có thể chỉ in đoạn giữa hai chuỗi start ... end."""
    text = Path(path).read_text(encoding="utf-8")
    if start:
        i = text.index(start)
        j = text.index(end, i) + len(end) if end else len(text)
        text = text[i:j]
    print(text)
