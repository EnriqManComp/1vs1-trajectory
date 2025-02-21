import h5py

f = h5py.File("database/1/0/first_plane.h5", "r")

data = f["first_plane"][:]  # Read all data

print(data)