# 🔐 Python File Integrity Checker

A Python utility that generates SHA-256 hashes for files to help detect whether a file has been modified.

## 🎯 Project Goal

Learn how hashing can be used to create a unique digital fingerprint for a file.

## ✨ Features

- Generate SHA-256 file hashes
- Read files in binary mode
- Detect file changes
- Handle missing files
- Simple command-line interface

## 🛠️ Technologies

- Python
- hashlib
- File Handling
- SHA-256
- Exception Handling
- Object-Oriented Programming

## 📁 Project Structure

```text
python-file-integrity-checker/
├── main.py
├── file_integrity.py
├── sample.txt
├── README.md
└── .gitignore
```

## 🚀 How to Run

```bash
python main.py
```

Enter the file name when asked.

## 🧠 How It Works

The program reads the file as binary data and creates a SHA-256 hash.

```python
sha256 = hashlib.sha256()
sha256.update(data)
sha256.hexdigest()
```

If the file changes, its SHA-256 hash will also change.

## 📚 What I Learned

- SHA-256 hashing
- `hashlib`
- Binary file reading
- `rb` file mode
- File integrity verification
- Exception handling
- Classes and objects

## 🔮 Future Improvements

- Store original hashes
- Compare files automatically
- Check entire folders
- Detect modified files
- Generate integrity reports
- Add a GUI

## 🎓 Project Status

✅ Completed

## 👨‍💻 Author

**Ayushman Tiwari**

GitHub: https://github.com/ayushman-ece