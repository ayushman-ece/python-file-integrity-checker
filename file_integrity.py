import hashlib


class FileIntegrityChecker:
    def calculate_hash(self, filename):
        sha256 = hashlib.sha256()

        with open(filename, "rb") as file:
            data = file.read()

        sha256.update(data)

        return sha256.hexdigest()