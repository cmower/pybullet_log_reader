import struct
import pandas  # https://pandas.pydata.org/


class PyBulletLogReader:
    def __init__(self, file_name):
        with open(filename, "rb") as f:
            keys = f.readline().decode("utf8").rstrip("\n").split(",")
            fmt = f.readline().decode("utf8").rstrip("\n")

            # The byte number of one record
            sz = struct.calcsize(fmt)
            # The type number of one record
            ncols = len(fmt)

            # Read data
            wholeFile = f.read()
            # split by alignment word
            chunks = wholeFile.split(b"\xaa\xbb")
            log = list()
            for chunk in chunks:
                if len(chunk) == sz:
                    values = struct.unpack(fmt, chunk)
                    record = list()
                    for i in range(ncols):
                        record.append(values[i])
                    log.append(record)

        # Save data as class attributes
        self._log = log
        self._columns = keys
        self._format = fmt
        self._size = size

    @property
    def columns(self):
        return self._columns

    @property
    def format(self):
        return self._format

    @property
    def size(self):
        return self._size

    @property
    def n(self):
        return len(self._log)

    @property
    def shape(self):
        return (len(self._log), len(self._columns))

    def as_pandas(self):
        data = {}
        for column_index, column_name in enumerate(self._columns):
            data[column_name] = [record[column_index] for record in self.log]
        return pandas.DataFrame(data)
