



import bilby
import h5py
import pandas as pd
import numpy as np
import corner
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


data_file1= "/home/tobi/Documents/GW_project/Results/outdir_GW150914_NPE_S/result/GW150914_data0_1126259462-4_importance_sampling.hdf5"
data_file2= "/home/tobi/Documents/GW_project/Results/outdir_GW150914_NPE_S/result/GW150914_data0_1126259462-4_sampling.hdf5"
data_file3= "/home/tobi/Documents/GW_project/Results/outdir_GW150914_toy/result/GW150914_data0_1126259462-4_sampling.hdf5"

gwtc1_medians = {
    "chirp_mass": 28.6,
    "mass_ratio": 30.6 / 35.6,   # ≃ 0.86
    "luminosity_distance": 440.0,
}





with h5py.File(data_file1, "r") as f:
    df1 = pd.DataFrame(f["samples"][:])

weights1 = df1["weights"] 


with h5py.File(data_file2, "r") as f:
    df2 = pd.DataFrame(f["samples"][:])

with h5py.File(data_file3, "r") as f:
    df3 = pd.DataFrame(f["samples"][:])

params = ["chirp_mass", "mass_ratio", "luminosity_distance"]

truths = [gwtc1_medians[p] for p in params]

label_map = {
    "chirp_mass": r"$\mathcal{M}\,[M_\odot]$",
    "mass_ratio": r"$q$",
    "luminosity_distance": r"$D_L\,[\mathrm{Mpc}]$",
    "inclination": r"$\iota\,[\mathrm{rad}]$",
}


bins=15
labels = [label_map[p] for p in params]

fig = corner.corner(df3[params], bins=bins,  labels=labels, truths=truths, truth_color="black", color="C0")
corner.corner(df2[params], bins=bins, fig=fig, labels=labels, color="C2")
corner.corner(df1[params], bins=bins, fig=fig, labels=labels, weights=weights1, color="C1")


legend_elements = [
    Line2D([0], [0], color="C0", lw=2, label="NPE Toy model"),
    Line2D([0], [0], color="C1", lw=2, label="NPE small Importance sampling"),
    Line2D([0], [0], color="C2", lw=2, label="NPE small"),
]


legend_elements.append(
    Line2D(
        [0], [0],
        color="black",
        label="GWTC-1 median"
    )
)

fig.legend(
    handles=legend_elements,
    loc="upper right",
    frameon=False,
)



plt.show()

