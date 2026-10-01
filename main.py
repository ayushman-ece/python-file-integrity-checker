from file_integrity import FileIntegrityChecker


checker = FileIntegrityChecker()

filename = input("Enter file name: ").strip()

try:
    file_hash = checker.calculate_hash(filename)

    print("\n===== FILE INTEGRITY =====")
    print(f"File : {filename}")
    print(f"SHA-256: {file_hash}")

except FileNotFoundError:
    print("File not found. ❌")