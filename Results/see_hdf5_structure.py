import h5py

file = "outdir_GW150914_NPE/result/GW150914_data0_1126259462-4_sampling.hdf5"

with h5py.File(file, "r") as f:
    f.visit(print)