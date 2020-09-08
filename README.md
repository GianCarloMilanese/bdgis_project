# Big Data in Geographic Information Systems - Project

Part 1 (notebook 1.ipynb):

- Perform hypothesis tests on the linear trends of gridded precipitation
  observational data implementing the False Discovery Rate (FDR) approach
  described in Wilks (2016), using the same data in order to validate the
  correctness of the implementation.

Part 2 (notebook 2.ipynb):

- Apply the FDR approach to temperature data from CMIP6 climate models to test
  the significance of temperature trends.


## Requirements

Main requirements: numpy, xarray, pandas, cartopy, tqdm, matplotlib,
statsmodels, ipywidgets

(Ipywidgets is only required for the final interactive visualization in both
notebooks.)

## References

1. Wilks, D. S., 2016: "The Stippling Shows Statistically Significant Grid
   Points": How Research Results are Routinely Overstated and Overinterpreted,
   and What to Do about It. Bull. Amer. Meteor. Soc., 97, 2263–2273,
   https://doi.org/10.1175/BAMS-D-15-00267.1.
   2. Hartmann, D.L., A.M.G. Klein Tank, M. Rusticucci, L. Alexander, S.
      Brönnimann, Y. Charabi, F. Dentener, E. Dlugo-kencky, D. Easterling, A.
      Kaplan, B. Soden, P. Thorne, M. Wild and P.M. Zhai, 2013: Observations:
      Atmosphere and Surface Supplementary Material. In: Climate Change 2013:
      The Physical Science Basis. Contribution of Working Group I to the Fifth
      Assessment Report of the Intergovernmental Panel on Climate Change
      [Stocker, T.F., D. Qin, G.-K. Plattner, M. Tignor, S.K. Allen, J.
      Boschung, A. Nauels, Y. Xia, V. Bex and P.M. Midgley (eds.)]. Available
      from www.climatechange2013.org and www.ipcc.ch.

