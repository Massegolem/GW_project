from dingo.gw.result import Result

result = Result.load("outdir_GW150914_NPE/result/GW150914_data0_1126259462-4_sampling.hdf5")

parameters = [
    "chirp_mass",
    "mass_ratio",
    "luminosity_distance",
    "theta_jn",
]

fig = result.plot_corner(parameters=parameters)
fig.savefig("corner.png", dpi=300)
