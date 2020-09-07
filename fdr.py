import numpy as np
import statsmodels.api as sm


def find_p_FDR(pvs, alpha_FDR):
    """
    Given an array/list of p values and alpha_FDR, apply the algorithm described
    in Wilks (2016) to find the value of p_FDR.

    Reference:

    Wilks, D. S., 2016: “The Stippling Shows Statistically Significant Grid
    Points”: How Research Results are Routinely Overstated and Overinterpreted,
    and What to Do about It. Bull. Amer. Meteor. Soc., 97, 2263–2273,
    https://doi.org/10.1175/BAMS-D-15-00267.1.
    
    :pvs: array/list of p_values
    :alpha_FDR: Control level alpha_FDR

    :returns: p_FDR
    """
    pvs_flat = np.array(pvs).flatten()
    nas = np.isnan(pvs_flat)
    N = len(pvs_flat[~nas])
    pvs_ranked = np.sort(pvs_flat)
    pvs_FDR = []

    for i in range(len(pvs_ranked)):
        current_p = pvs_ranked[i]
        if np.isnan(current_p):
            continue
        if current_p <= ((i+1)/N)*alpha_FDR:
            pvs_FDR.append(current_p)

    p_FDR = np.max(pvs_FDR)
    return p_FDR


def t_tests(grid):
    """
    Given a numpy array with shape (time, latitudes, longitues), performs an OLS
    linear regression on each cell [:, i, j] and a t test on the slope
    coefficient (H0: slope = 0).

    :grid: A numpy array with shape (time, latitudes, longitudes)

    :returns: three arrays containing the p values, intercepts and slopes of
    each cell
    """

    nlat = grid.shape[1]
    nlon = grid.shape[2]

    pvs = np.empty([nlat, nlon], dtype=float)  # p values
    pvs[:, :] = np.nan

    trends = np.empty([nlat, nlon], dtype=float)  # slopes
    trends[:, :] = np.nan

    ints = np.empty([nlat, nlon], dtype=float)  # intercepts
    ints[:, :] = np.nan

    for j in range(nlon):
        for i in range(nlat):

            Y = grid[:, i, j]

            # if np.all(np.isnan(Y)):
            #     continue

            X = np.arange(1, Y.shape[0]+1)
            X = sm.add_constant(X)

            # OLS
            # Discard missing values
            nas = np.isnan(Y)
            model = sm.OLS(Y[~nas], X[~nas])
            results = model.fit()

            # Store result in array
            pvs[i, j] = results.pvalues[1]
            ints[i, j] = results.params[0]
            trends[i, j] = results.params[1]

    return pvs, ints, trends
