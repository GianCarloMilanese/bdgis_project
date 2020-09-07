These data sets contain gridded temperature anomalies for three parameters (mean, minimum, and maximum temperatures) from the GHCN V2 monthly temperature data sets. 
GHCN homogeneity adjusted data was the primary source for developing the gridded fields.  In grid boxes without homogeneity adjusted data, GHCN raw data was used to provide
additional coverage when possible.  

Each month of data consists of 2592 gridded data points
produced on a 5 X 5 degree basis for the entire globe (72 longitude X 36 latitude grid boxes).
   
Gridded data for every month from January 1880 (tempeature) or January 1900 (precipitation) to the most recent month are available. For temperature, the data are temperature anomalies in hundredths of a degree Celcius.  For precipitation, the data are provided as anomalies in hundredths of a millimeter or as precipitation totals in hundredths of a millimeter. (Each gridded value was multiplied by 100 and written to file as an integer.)  Missing values are represented by the value -32768.

There are 3 files:
1. grid-mntp-1880-current-v2.dat.gz contains mean temperature anomalies on a 5X5 degree grid from January 1880 through the most recently available month.
2. grid_prcp_1900-current.dat.gz contains monthly precipitation anomalies on a 5X5 degree grid from January 1900 through the most recently available month.
3. grid.prcp.DMean* contains monthly precipitation totals on a 5X5 degree grid from January 1900 through the most recently available month.

The data are formatted by year, month, latitude and longitude.  There are twelve longitude grid values per line, so there are 6 lines (72/12 = 6) for each of the 36 latitude bands.  Longitude
values are written from 180 W to 180 E, and latitude values from 90 N to 90 S.  Data for each month is preceded by a label containing the month and year of the gridded data.

grid-mntp-1880-current-v2.dat
     for year = begyr to endyr
      for month = 1 to 12
        format(2i5) month,year
        for ylat = 1 to 36 (85-90N,80-85N,...,80-85S,85-90S)
          format(12i5) 180-175W,175-170W,...,130-125W,125-120W
          format(12i5) 120-115W,175-170W,...,70-65W,65-60W
          format(12i5) 60-55W,55-50W,...,10-5W,5-0W
          format(12i5) 0-5E,5-10E,...,50-55E,55-60E
          format(12i5) 60-65E,65-70E,...,110-115E,115-120E
          format(12i5) 120-125E,125-130E,...,170-175E,175-180E
   
grid_prcp_1900-current.dat  and grid.prcp.DMean
     for year = begyr to endyr
      for month = 1 to 12
        format(2i7) month,year
        for ylat = 1 to 36 (85-90N,80-85N,...,80-85S,85-90S)
          format(12i5) 180-175W,175-170W,...,130-125W,125-120W
          format(12i5) 120-115W,175-170W,...,70-65W,65-60W
          format(12i5) 60-55W,55-50W,...,10-5W,5-0W
          format(12i5) 0-5E,5-10E,...,50-55E,55-60E
          format(12i5) 60-65E,65-70E,...,110-115E,115-120E
          format(12i5) 120-125E,125-130E,...,170-175E,175-180E


Each file has been compressed using 'gzip'.  They can be uncompressed with 'WinZip' for those
using Windows 95 or with 'gzip' from most UNIX platforms.  The FORTRAN utility program
'read_gridded.f' can be downloaded to assist in extracting data of interest.  This program allows
the user to extract non-missing values for selected months and write the data to an ascii output
file.  The latitude and longitude of the center of each corresponding grid box accompanies each
gridded value in the output file.
   
Temperature and precipitation anomalies are calculated with respect to the period 1961 - 1990 using the Climate Anomaly Method). The gridded data sets are produced to provide the most accurate time series possible. However, this required that we treat months and grid boxes independently through time.  The use
of these data is most appropriate for analyzing the change in temperature within a particular grid box, or set of grid boxes, over a span of years.  If one is more interested in analyzing temperature changes within individual years, e.g., the change in temperature between February and March, 1908, or between two regions in 1908, we recommend that the GHCN station data be used
directly.

*Negative values can occur in grid.prcp.DMean when there are stations with different periods of record and different climatologies in the same grid box. If for example there are 2 stations in a grid box having data from 1950 through present, the 1961-1990 climatological average for the grid box will be the average of the two.  If one of these stations also has data from 1900-1950 but the other doesn't then monthly values during that period could be negative. This could occur if the station with data from 1900-1950 is a climatologically wetter station than climatological average of the two; and the month in question was extremely dry. The anomaly for the single station would be a large negative anomaly in that month; and when applied to the climatological average for the grid box, the grid box value could be negative.

To access anonymous FTP at NCDC use the following information: 

Machine Address : ftp.ncdc.noaa.gov
Login Name      : anonymous 
Password        : your email address
Directory       : /pub/data/ghcn/v2/
Enter           : bin
Enter           : get 'filename'
