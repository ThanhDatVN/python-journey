# 📐 Thiết kế khóa học

[📚 Mục lục](../README.md)

Tài liệu này mô tả **bản thiết kế hoàn chỉnh** của repo — hoàn thiện từ bản phác thảo ban đầu trong [`example.md`](../example.md).

## 1. Mục tiêu

1. Học Python **từ con số 0 tới ứng dụng** (khoa học dữ liệu, học máy, cơ sở dữ liệu, web) bằng **tiếng Việt**.
2. **Bám sát 1:1** cấu trúc [W3Schools Python Tutorial](https://www.w3schools.com/python/) để học **song song**.
3. Dạng **Jupyter Notebook**: "Try it Yourself" ngay trong từng cell.
4. Thiết kế giúp **dễ học, dễ nhớ**: mục tiêu đầu bài, ghi nhớ cuối bài, bài tập tự chấm, ôn tập ngắt quãng.

## 2. Thay đổi so với bản phác thảo (`example.md`)

| Bản phác thảo | Bản hoàn chỉnh | Lý do |
|---|---|---|
| 76 bài Tutorial theo sidebar W3Schools **cũ** | **101** bài theo sidebar **hiện tại** (đã kiểm tra trực tiếp) | W3Schools đã tách nhỏ: Output, Statements, 10 bài Operators, 7 bài If…Else, 8 bài Functions, Match, Range, None, VirtualEnv… |
| Classes nằm trong Tutorial | Chương riêng **02_python_classes** (19 bài, gồm 9 bài Magic Methods) | W3Schools có mục "Python Classes" riêng |
| `extras/` (Phase 2) | Soạn **đầy đủ**: NumPy 44 · Pandas 15 · SciPy 11 · Django 47 · Matplotlib 13 · ML 23 · DSA 20 · MySQL 12 · MongoDB 11 | Theo yêu cầu học trọn bộ module |
| Exercises / Quizzes chưa chi tiết | 21 bộ Exercises + Code Challenge tự chấm · 3 Quiz chấm điểm · ôn tập Leitner · Anki | Tăng thực hành và ghi nhớ |
| Reference: "tra cứu nhanh" | 17 trang Reference + Cheat Sheet | Theo mục Python Reference / Module Reference |

## 3. Cấu trúc thư mục ↔ sidebar W3Schools

| Thư mục | Mục sidebar W3Schools |
|---|---|
| `01_python_tutorial/` | PYTHON TUTORIAL (Python HOME → Python VirtualEnv) |
| `02_python_classes/` | PYTHON CLASSES |
| `03_file_handling/` | FILE HANDLING |
| `04_python_modules/{numpy,pandas,scipy,django}/` | PYTHON MODULES (NumPy, Pandas, SciPy, Django Tutorial) |
| `05_matplotlib/` | PYTHON MATPLOTLIB |
| `06_machine_learning/` | MACHINE LEARNING |
| `07_dsa/` | PYTHON DSA |
| `08_mysql/` · `09_mongodb/` | PYTHON MYSQL · PYTHON MONGODB |
| `10_reference/` | PYTHON REFERENCE · MODULE REFERENCE |
| `11_how_to/` | PYTHON HOW TO |
| `12_exercises/` · `13_quizzes/` | PYTHON EXAMPLES (Exercises, Quiz, Code Challenges) |

Quy ước tên file: `NNN_ten_bai.ipynb` — số thứ tự 3 chữ số theo đúng thứ tự sidebar; mỗi mục con của sidebar là **một notebook riêng** (không gộp).

> Ngoại lệ có chủ đích: nhóm *PostgreSQL* (5 trang) và *Deploy Django* (6 trang) của Django là hướng dẫn thao tác trên AWS Console, được tóm tắt thành 2 notebook (`044`, `045`).

## 4. Giải phẫu một notebook bài học

| # | Thành phần | Nội dung |
|---|---|---|
| 1 | Thanh điều hướng trên | Breadcrumb (chương › nhóm) · *Bài x/y* · « Trước · 📚 Mục lục · Tiếp » |
| 2 | Tiêu đề + 📖 + 🎯 | Tên bài như W3Schools · link trang W3Schools · mục lục mini "Trong bài này" |
| 3 | Các mục `##` | **Heading tiếng Anh giống W3Schools** + bản dịch, giải thích tiếng Việt, cell ví dụ (đã chạy, có output) |
| 4 | 🧪 Try it Yourself | Cell để sửa/thử, có gợi ý cụ thể |
| 5 | `## ➕ Mở rộng: ...` | Kiến thức **ngoài** W3Schools (thực hành tốt, lỗi hay gặp, cách hiện đại) |
| 6 | ⚠️ Lưu ý cập nhật | Chỗ W3Schools dùng API cũ (ví dụ `sns.distplot`, `affinity=`, `math.cos` với mảng NumPy 2) |
| 7 | 🧠 Ghi nhớ nhanh | 3–5 ý cốt lõi + ⚠️ lỗi hay gặp |
| 8 | 📝 Exercise | 1–2 câu trắc nghiệm/điền khuyết, đáp án trong `<details>` |
| 9 | Thanh điều hướng dưới | « Trước · Mục lục · Tiếp » |

Cell có lỗi **cố ý** (minh hoạ lỗi) mang tag `raises-exception`; cell không chạy được trong môi trường chung (cài package, `runserver`, kết nối MySQL thật…) mang tag `skip-execution`.

## 5. Thiết kế giúp dễ học, dễ nhớ

- **Mục tiêu trước — ghi nhớ sau:** 🎯 đầu bài báo trước nội dung, 🧠 cuối bài tóm lại ý chính (hiệu ứng *advance organizer* + *summarization*).
- **Học qua làm:** mọi ví dụ chạy được; Try it Yourself có nhiệm vụ cụ thể.
- **Kiểm tra ngay (retrieval practice):** Exercise cuối mỗi bài, Exercises theo chủ đề, Quiz chấm điểm.
- **Ôn tập ngắt quãng (spaced repetition):** notebook Leitner + bộ thẻ Anki sinh từ ngân hàng câu hỏi.
- **Liên kết kiến thức:** link chéo giữa các bài (ví dụ Matplotlib ↔ NumPy ↔ ML, SciPy Graphs ↔ DSA Graphs), Glossary Anh–Việt.
- **Theo dõi tiến độ:** PROGRESS.md với checklist mọi bài.
- **Bối cảnh Việt Nam:** ví dụ tiếng Việt, cảnh báo `encoding="utf-8"` trên Windows, `slugify()` làm mất chữ "đ"…

## 6. Bài tập & Quiz

- **Exercises** (`12_exercises/`): Phần A trắc nghiệm/điền khuyết (đáp án ẩn) + Phần B Code Challenge: cell ✍️ (stub) → cell ✅ kiểm tra bằng `assert` → 💡 lời giải ẩn.
- **Quiz** (`13_quizzes/`): câu hỏi không hiện đáp án; phiếu trả lời `my_answers` + cell chấm điểm (đáp án được mã hoá base64 để tránh lộ khi làm bài) + đáp án chi tiết ở cuối.
- **Ngân hàng câu hỏi** `question_bank.json`: tự động gom mọi câu 📝 Exercise của bài học (kèm chương, thứ tự bài, link) → dùng cho ôn tập ngẫu nhiên và xuất **Anki** (`flashcards_anki.txt`).

## 7. Dữ liệu

Dữ liệu là **tổng hợp** (sinh bằng code có seed), cùng cấu trúc cột với ví dụ trên W3Schools:

| File | Dùng trong |
|---|---|
| `03_file_handling/demofile.txt` | File Handling (có dòng tiếng Việt để minh hoạ encoding) |
| `04_python_modules/pandas/data.csv`, `data.json` | Pandas (Duration, Pulse, Maxpulse, Calories) |
| `04_python_modules/pandas/dirtydata.csv` | Pandas — Cleaning Data (ô trống, sai định dạng, sai giá trị, trùng lặp) |
| `06_machine_learning/cars.csv` | Multiple Regression, Scale, Categorical Data |
| `06_machine_learning/shows.csv` | Decision Tree |

## 8. Quy trình kiểm thử

Mọi notebook được **chạy thật** khi tạo repo:

- Cell ví dụ chạy tuần tự như một kernel; output (kể cả **ảnh biểu đồ** Matplotlib/Seaborn và **bảng HTML** của Pandas) được lưu vào notebook.
- Cell `raises-exception` phải thực sự báo lỗi; cell `skip-execution` được kiểm tra cú pháp.
- Lời giải Code Challenge được chạy cùng cell kiểm tra.
- 47 notebook Django được chạy **nối tiếp** trên cùng một dự án `my_tennis_club` thật.
- Mọi link nội bộ trong notebook và file Markdown được kiểm tra.

## 9. Thêm/sửa bài học

1. Sửa trực tiếp notebook trong Jupyter/VS Code.
2. Giữ đúng các thành phần ở mục 4 (điều hướng, 📖, 🎯, 🧠, 📝).
3. Bài mới: đặt số thứ tự đúng vị trí sidebar, cập nhật link « Trước/Tiếp » của bài liền kề, thêm vào mục lục `README.md`, README của thư mục và `PROGRESS.md`.
4. Chạy lại toàn bộ notebook (*Kernel → Restart Kernel and Run All Cells*) trước khi commit.
