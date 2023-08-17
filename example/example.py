from pybullet_log_reader import PyBulletLogReader

log_reader = PyBulletLogReader("log.dat")

df = log_reader.as_pandas()

print(df)
