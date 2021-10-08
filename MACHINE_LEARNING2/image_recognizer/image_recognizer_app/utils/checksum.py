import hashlib


class Checksum:


    @staticmethod
    def md5(file):
        size = 1024*1024  # 1MB
        checksum = hashlib.md5()
        if file.multiple_chunks():
            for data in file.chunks(size):
                checksum.update(data)
        else:
            checksum.update(file.read())

        return checksum.hexdigest()
