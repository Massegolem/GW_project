data_file= "/home/tobi/Documents/GW_project/Results/outdir_GW150914_NPE/result/GW150914_data0_1126259462-4_importance_sampling.hdf5"
import pandas
import h5py

data = h5py.File(data_file, 'r')
print(data["samples"])#
df = pandas.DataFrame(data["samples"][:])
print(df.head())