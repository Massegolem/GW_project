



import bilby
import h5py
import pandas as pd
import numpy as np
import corner
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


#data_file1= "outdir/outdir_GW150914_NPE_S/result/GW150914_data0_1126259462-4_sampling.hdf5"
data_file1= "outdir/outdir_GW150914_toy/result/GW150914_data0_1126259462-4_sampling.hdf5"
#data_file2= "/home/tobi/Documents/GW_project/Results/outdir/outdir_GW150914_NPE_S2/result/GW150914_data0_1126259462-4_sampling.hdf5"
data_file3= "outdir/outdir_GW150914_NPE_S3/result/GW150914_data0_1126259462-4_sampling.hdf5"

gwtc1_medians = {
    "chirp_mass": 30.4,
    "mass_ratio": 31.6 / 38.9,   # ≃ 0.86
    "luminosity_distance": 410.0,
    "dec": -1.27,
    "ra": 2.14,
}




with h5py.File(data_file1, "r") as f:
    df1 = pd.DataFrame(f["samples"][:])

#weights1 = df1["weights"] 


#with h5py.File(data_file2, "r") as f:
#    df2 = pd.DataFrame(f["samples"][:])

with h5py.File(data_file3, "r") as f:
    df3 = pd.DataFrame(f["samples"][:])

params = ["chirp_mass", "mass_ratio", "luminosity_distance", "dec", "ra"]

params = ["chirp_mass", "mass_ratio", "luminosity_distance"]

truths = [gwtc1_medians[p] for p in params]

label_map = {
    "chirp_mass": r"$Chirp-Mass \,[M_\odot]$",
    "mass_ratio": r"$Mass-ratio$",
    "luminosity_distance": r"$lum-dist\,[\mathrm{Mpc}]$",
    "dec": r"DEC [rad]",
    "ra": r"RA [rad]",
}


label_map = {
    "chirp_mass": r"$\mathcal{M}\,[M_\odot]$",
    "mass_ratio": r"$q$",
    "luminosity_distance": r"$D_L\,[\mathrm{Mpc}]$",
    "dec": r"DEC [rad]",
    "ra": r"RA [rad]",
}


bins=15
labels = [label_map[p] for p in params]

fig = corner.corner(df1[params], bins=bins,  labels=labels, color="C0",label_kwargs= {"fontsize":15})
corner.corner(df3[params], bins=bins, fig=fig, labels=labels,truths=truths,truth_color="black", color="C1")
#corner.corner(df1[params], bins=bins, fig=fig, labels=labels, weights=weights1, color="C1")
#corner.corner(df2[params], bins=bins, fig=fig, labels=labels, color="C1")

legend_elements = [
    Line2D([0], [0], color="C0", lw=2, label="Dingo Toy Model"),
    #Line2D([0], [0], color="C1", lw=2, label="NPE_S2"),
    Line2D([0], [0], color="C1", lw=2, label="GPU Laptop Trained Dingo NPE Model"),
]


legend_elements.append(
    Line2D(
        [0], [0],
        color="black",
        label="GWTC-1 median (Abbott et al. 2016) "
    )
)

fig.legend(
    handles=legend_elements,
    loc="upper right",
    frameon=False,
    fontsize="15",
    bbox_to_anchor=(1, 0.9)
)

fig.suptitle("Parameter Estimation of GW150914", fontsize=20)
fig.subplots_adjust(top=0.92) # Verringert die Höhe der Plots, um Platz zu schaffen

plt.show()

