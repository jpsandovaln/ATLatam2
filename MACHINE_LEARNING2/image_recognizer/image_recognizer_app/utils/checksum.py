import hashlib


class Checksum:

    @staticmethod
    def md5(file):
        checksum = hashlib.md5()
        if file.multiple_chunks():
            print("it will be chunked")
            for data in file.chunks():
                checksum.update(data)

        else:
            checksum.update(file.read())

        return checksum.hexdigest()

