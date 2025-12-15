import h5py
import numpy as np
import pandas as pd

def load_dingo_hdf5(filename):
    """Load posterior samples from a Dingo HDF5 file into a DataFrame."""
    with h5py.File(filename, "r") as f:
        # Posterior samples
        samples = f["samples"][:]
        # Parameter names (decode bytes)
        param_names = [name.decode('utf-8') for name in f["parameter_names"][:]]
    df = pd.DataFrame(samples, columns=param_names)
    return df

def summarize_posterior(df):
    """Compute median and 90% credible interval for each parameter."""
    summary = {}
    for col in df.columns:
        median = np.median(df[col])
        lower = np.percentile(df[col], 5)
        upper = np.percentile(df[col], 95)
        summary[col] = {"median": median, "5%": lower, "95%": upper}
    return pd.DataFrame(summary).T

def compare_posteriors(file1, file2):
    """Load and summarize two posterior files side by side."""
    df1 = load_dingo_hdf5(file1)
    df2 = load_dingo_hdf5(file2)

    summary1 = summarize_posterior(df1)
    summary2 = summarize_posterior(df2)

    # Merge for easy comparison
    comparison = pd.concat([summary1.add_prefix("run1_"), summary2.add_prefix("run2_")], axis=1)
    return comparison

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Compare Dingo posterior HDF5 files")
    parser.add_argument("file1", help="First HDF5 results file")
    parser.add_argument("file2", help="Second HDF5 results file")
    args = parser.parse_args()

    comparison = compare_posteriors(args.file1, args.file2)
    print("\nPosterior comparison (median and 90% CI):\n")
    print(comparison)