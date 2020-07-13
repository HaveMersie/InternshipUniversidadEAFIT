"""
@author: mljmersie

Code to visualise the time series of PM2.5 in the Aburra valley in time period 2016-now.

Note that the indices 3, 0 and 2 are used here to retrieve the right columns. If the position of these columns change, then a code should be written to automatically retrieve the right indices belonging to the desired columns
Directories need to be changed if another computer is used
"""


import pandas as pd
from glob import glob
import numpy as np
import seaborn as sns
sns.set(rc={'figure.figsize':(14,7)})
import folium
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
plt.style.use('seaborn-whitegrid')
import datetime
import matplotlib.dates as mdates


# %%

# In the SIATA files up and till 07-2019, they forgot to add 'Fecha_Hora' as the column name of the first column. Because of that the concatenation process goes wrong. The following function can be used to modify the data. Note that you should only use this function ONCE!
def Addtext(file, word):
    with open(file,'r') as modified1:
        a = modified1.readlines()
        a[0] = word + a[0]
        
    with open(file, 'w+') as modified2:
        for line in a:
            modified2.write(line)

## I temporarily removed all the files from folder 2019 that already had Fecha_Hora as the column name, i.e. the last three files/months of every station.
'ONLY RUN/UNCOMMENT THIS SECTION ONCE'

#filestobemodified = glob('/home/mljmersie/Documents/SIATA/2016/estacion*') + glob('/home/mljmersie/Documents/SIATA/2017/estacion*') + glob('/home/mljmersie/Documents/SIATA/2018/estacion*') + glob('/home/mljmersie/Documents/SIATA/2019/estacion*')
#word = 'Fecha_Hora'
#
#for file in filestobemodified:
#    Addtext(file, word)
    
# %% In the following sections, for every year the data per station will be bundled. In other words, we end up with one dataframe per station per year.

# %%
# Year 2016

## Location 3

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2016/estacion_data_calidadaire_3_*.csv')

# Making sure that the files are ordered correctly
filenames = sorted(filenames)

# Concatenating the months and resetting the index
station3_2016 = pd.concat([pd.read_csv(f) for f in filenames])
station3_2016 = station3_2016.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

# Taking the quality column and checking for which indices it contains either a 1 or a -1
station3_2016_calidad = station3_2016.take([3], axis=1)
result = station3_2016_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station3_2016.iloc[rows, 2] = np.nan


# Taking only the 'Fecha_Hora' column and the 'pm25 column'
# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station3_2016 = station3_2016.take([0,2], axis=1)


## Location 12

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2016/estacion_data_calidadaire_12_*.csv')

# Making sure that the files are ordered correctly
filenames = sorted(filenames)

# Concatenating the months and resetting the index
station12_2016 = pd.concat([pd.read_csv(f) for f in filenames])
station12_2016 = station12_2016.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

# Taking the quality column and checking for which indices it contains either a 1 or a -1
station12_2016_calidad = station12_2016.take([3], axis=1)
result = station12_2016_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station12_2016.iloc[rows, 2] = np.nan

# Taking only the 'Fecha_Hora' column and the 'pm25 column'
# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station12_2016 = station12_2016.take([0,2], axis=1)

## Location 28

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2016/estacion_data_calidadaire_28_*.csv')
filenames = sorted(filenames)

station28_2016 = pd.concat([pd.read_csv(f) for f in filenames])
station28_2016 = station28_2016.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station28_2016_calidad = station28_2016.take([3], axis=1)
result = station28_2016_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station28_2016.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station28_2016 = station28_2016.take([0,2], axis=1)


## Location 31

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2016/estacion_data_calidadaire_31_*.csv')
filenames = sorted(filenames)

station31_2016 = pd.concat([pd.read_csv(f) for f in filenames])
station31_2016 = station31_2016.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station31_2016_calidad = station31_2016.take([3], axis=1)
result = station31_2016_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station31_2016.iloc[rows, 2] = np.nan


# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station31_2016 = station31_2016.take([0,2], axis=1)


## Location 38

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2016/estacion_data_calidadaire_38_*.csv')
filenames = sorted(filenames)

station38_2016 = pd.concat([pd.read_csv(f) for f in filenames])
station38_2016 = station38_2016.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station38_2016_calidad = station38_2016.take([3], axis=1)
result = station38_2016_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station38_2016.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station38_2016 = station38_2016.take([0,2], axis=1)


## Location 44

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2016/estacion_data_calidadaire_44_*.csv')
filenames = sorted(filenames)

station44_2016 = pd.concat([pd.read_csv(f) for f in filenames])
station44_2016 = station44_2016.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station44_2016_calidad = station44_2016.take([3], axis=1)
result = station44_2016_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station44_2016.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station44_2016 = station44_2016.take([0,2], axis=1)


## Location 48

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2016/estacion_data_calidadaire_48_*.csv')
filenames = sorted(filenames)

station48_2016 = pd.concat([pd.read_csv(f) for f in filenames])
station48_2016 = station48_2016.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station48_2016_calidad = station48_2016.take([3], axis=1)
result = station48_2016_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station48_2016.iloc[rows, 2] = np.nan


# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station48_2016 = station48_2016.take([0,2], axis=1)



# %%
# Year 2017

# %%

## Location 3

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2017/estacion_data_calidadaire_3_*.csv')
filenames = sorted(filenames)

station3_2017 = pd.concat([pd.read_csv(f) for f in filenames])
station3_2017 = station3_2017.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station3_2017_calidad = station3_2017.take([3], axis=1)
result = station3_2017_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station3_2017.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station3_2017 = station3_2017.take([0,2], axis=1)


## Location 12

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2017/estacion_data_calidadaire_12_*.csv')
filenames = sorted(filenames)

station12_2017 = pd.concat([pd.read_csv(f) for f in filenames])
station12_2017 = station12_2017.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station12_2017_calidad = station12_2017.take([3], axis=1)
result = station12_2017_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station12_2017.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station12_2017 = station12_2017.take([0,2], axis=1)


## Location 28

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2017/estacion_data_calidadaire_28_*.csv')
filenames = sorted(filenames)

station28_2017 = pd.concat([pd.read_csv(f) for f in filenames])
station28_2017 = station28_2017.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station28_2017_calidad = station28_2017.take([3], axis=1)
result = station28_2017_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station28_2017.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station28_2017 = station28_2017.take([0,2], axis=1)


## Location 31

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2017/estacion_data_calidadaire_31_*.csv')
filenames = sorted(filenames)

station31_2017 = pd.concat([pd.read_csv(f) for f in filenames])
station31_2017 = station31_2017.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station31_2017_calidad = station31_2017.take([3], axis=1)
result = station31_2017_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station31_2017.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station31_2017 = station31_2017.take([0,2], axis=1)



## Location 38

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2017/estacion_data_calidadaire_38_*.csv')
filenames = sorted(filenames)

station38_2017 = pd.concat([pd.read_csv(f) for f in filenames])
station38_2017 = station38_2017.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station38_2017_calidad = station38_2017.take([3], axis=1)
result = station38_2017_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station38_2017.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station38_2017 = station38_2017.take([0,2], axis=1)


## Location 44

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2017/estacion_data_calidadaire_44_*.csv')
filenames = sorted(filenames)

station44_2017 = pd.concat([pd.read_csv(f) for f in filenames])
station44_2017 = station44_2017.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station44_2017_calidad = station44_2017.take([3], axis=1)
result = station44_2017_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station44_2017.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station44_2017 = station44_2017.take([0,2], axis=1)


## Location 48

# Loading csv files for location
filenames = glob('/home/mljmersie/Documents/SIATA/2017/estacion_data_calidadaire_48_*.csv')
filenames = sorted(filenames)

station48_2017 = pd.concat([pd.read_csv(f) for f in filenames])
station48_2017 = station48_2017.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station48_2017_calidad = station48_2017.take([3], axis=1)
result = station48_2017_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station48_2017.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station48_2017 = station48_2017.take([0,2], axis=1)



## Location 69

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2017/estacion_data_calidadaire_69_*.csv')
filenames = sorted(filenames)

station69_2017 = pd.concat([pd.read_csv(f) for f in filenames])
station69_2017 = station69_2017.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station69_2017_calidad = station69_2017.take([3], axis=1)
result = station69_2017_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows1 = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Station 69 has measurements that are invalid, but have a -1 or 1
station69_2017_measurements = station69_2017.take([2], axis=1)
result = station69_2017_measurements.isin([-9999])
rows2 = list(result['pm25'][result['pm25'] == True].index)

rows = [y for x in [rows1, rows2] for y in x]

# Replacing invalid values with NaN
station69_2017.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station69_2017 = station69_2017.take([0,2], axis=1)

## Location 78

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2017/estacion_data_calidadaire_78_*.csv')
filenames = sorted(filenames)

station78_2017 = pd.concat([pd.read_csv(f) for f in filenames])
station78_2017 = station78_2017.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station78_2017_calidad = station78_2017.take([3], axis=1)
result = station78_2017_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station78_2017.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station78_2017 = station78_2017.take([0,2], axis=1)

## Location 79

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2017/estacion_data_calidadaire_79_*.csv')
filenames = sorted(filenames)

station79_2017 = pd.concat([pd.read_csv(f) for f in filenames])
station79_2017 = station79_2017.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station79_2017_calidad = station79_2017.take([3], axis=1)
result = station79_2017_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station79_2017.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station79_2017 = station79_2017.take([0,2], axis=1)


## Location 80

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2017/estacion_data_calidadaire_80_*.csv')
filenames = sorted(filenames)

station80_2017 = pd.concat([pd.read_csv(f) for f in filenames])
station80_2017 = station80_2017.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station80_2017_calidad = station80_2017.take([3], axis=1)
result = station80_2017_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station80_2017.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station80_2017 = station80_2017.take([0,2], axis=1)


## Location 81

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2017/estacion_data_calidadaire_81_*.csv')
filenames = sorted(filenames)

station81_2017 = pd.concat([pd.read_csv(f) for f in filenames])
station81_2017 = station81_2017.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station81_2017_calidad = station81_2017.take([3], axis=1)
result = station81_2017_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station81_2017.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station81_2017 = station81_2017.take([0,2], axis=1)


## Location 82

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2017/estacion_data_calidadaire_82_*.csv')
filenames = sorted(filenames)

station82_2017 = pd.concat([pd.read_csv(f) for f in filenames])
station82_2017 = station82_2017.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station82_2017_calidad = station82_2017.take([3], axis=1)
result = station82_2017_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station82_2017.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station82_2017 = station82_2017.take([0,2], axis=1)


## Location 83

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2017/estacion_data_calidadaire_83_*.csv')
filenames = sorted(filenames)

station83_2017 = pd.concat([pd.read_csv(f) for f in filenames])
station83_2017 = station83_2017.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station83_2017_calidad = station83_2017.take([3], axis=1)
result = station83_2017_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station83_2017.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station83_2017 = station83_2017.take([0,2], axis=1)


## Location 84

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2017/estacion_data_calidadaire_84_*.csv')
filenames = sorted(filenames)

station84_2017 = pd.concat([pd.read_csv(f) for f in filenames])
station84_2017 = station84_2017.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station84_2017_calidad = station84_2017.take([3], axis=1)
result = station84_2017_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station84_2017.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station84_2017 = station84_2017.take([0,2], axis=1)


## Location 85

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2017/estacion_data_calidadaire_85_*.csv')
filenames = sorted(filenames)

station85_2017 = pd.concat([pd.read_csv(f) for f in filenames])
station85_2017 = station85_2017.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station85_2017_calidad = station85_2017.take([3], axis=1)
result = station85_2017_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station85_2017.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station85_2017 = station85_2017.take([0,2], axis=1)


## Location 86

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2017/estacion_data_calidadaire_86_*.csv')
filenames = sorted(filenames)

station86_2017 = pd.concat([pd.read_csv(f) for f in filenames])
station86_2017 = station86_2017.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station86_2017_calidad = station86_2017.take([3], axis=1)
result = station86_2017_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station86_2017.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station86_2017 = station86_2017.take([0,2], axis=1)


## Location 87

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2017/estacion_data_calidadaire_87_*.csv')
filenames = sorted(filenames)

station87_2017 = pd.concat([pd.read_csv(f) for f in filenames])
station87_2017 = station87_2017.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station87_2017_calidad = station87_2017.take([3], axis=1)
result = station87_2017_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station87_2017.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station87_2017 = station87_2017.take([0,2], axis=1)



## Location 88

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2017/estacion_data_calidadaire_88_*.csv')
filenames = sorted(filenames)

station88_2017 = pd.concat([pd.read_csv(f) for f in filenames])
station88_2017 = station88_2017.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station88_2017_calidad = station88_2017.take([3], axis=1)
result = station88_2017_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station88_2017.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station88_2017 = station88_2017.take([0,2], axis=1)

# %%
# Year 2018

# %%

## Location 3

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2018/estacion_data_calidadaire_3_*.csv')
filenames = sorted(filenames)

station3_2018 = pd.concat([pd.read_csv(f) for f in filenames])
station3_2018 = station3_2018.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station3_2018_calidad = station3_2018.take([3], axis=1)
result = station3_2018_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station3_2018.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station3_2018 = station3_2018.take([0,2], axis=1)


## Location 12

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2018/estacion_data_calidadaire_12_*.csv')
filenames = sorted(filenames)

station12_2018 = pd.concat([pd.read_csv(f) for f in filenames])
station12_2018 = station12_2018.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station12_2018_calidad = station12_2018.take([3], axis=1)
result = station12_2018_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station12_2018.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station12_2018 = station12_2018.take([0,2], axis=1)


## Location 28

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2018/estacion_data_calidadaire_28_*.csv')
filenames = sorted(filenames)

station28_2018 = pd.concat([pd.read_csv(f) for f in filenames])
station28_2018 = station28_2018.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station28_2018_calidad = station28_2018.take([3], axis=1)
result = station28_2018_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station28_2018.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station28_2018 = station28_2018.take([0,2], axis=1)


## Location 31

# Loading csv files for location 31
filenames = glob('/home/mljmersie/Documents/SIATA/2018/estacion_data_calidadaire_31_*.csv')
filenames = sorted(filenames)

station31_2018 = pd.concat([pd.read_csv(f) for f in filenames])
station31_2018 = station31_2018.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station31_2018_calidad = station31_2018.take([3], axis=1)
result = station31_2018_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station31_2018.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station31_2018 = station31_2018.take([0,2], axis=1)


## Location 38

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2018/estacion_data_calidadaire_38_*.csv')
filenames = sorted(filenames)

station38_2018 = pd.concat([pd.read_csv(f) for f in filenames])
station38_2018 = station38_2018.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station38_2018_calidad = station38_2018.take([3], axis=1)
result = station38_2018_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station38_2018.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station38_2018 = station38_2018.take([0,2], axis=1)


## Location 44

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2018/estacion_data_calidadaire_44_*.csv')
filenames = sorted(filenames)

station44_2018 = pd.concat([pd.read_csv(f) for f in filenames])
station44_2018 = station44_2018.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station44_2018_calidad = station44_2018.take([3], axis=1)
result = station44_2018_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station44_2018.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station44_2018 = station44_2018.take([0,2], axis=1)


## Location 48

# Loading csv files for location 48
filenames = glob('/home/mljmersie/Documents/SIATA/2018/estacion_data_calidadaire_48_*.csv')
filenames = sorted(filenames)

station48_2018 = pd.concat([pd.read_csv(f) for f in filenames])
station48_2018 = station48_2018.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station48_2018_calidad = station48_2018.take([3], axis=1)
result = station48_2018_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station48_2018.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station48_2018 = station48_2018.take([0,2], axis=1)


## Location 69

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2018/estacion_data_calidadaire_69_*.csv')
filenames = sorted(filenames)

station69_2018 = pd.concat([pd.read_csv(f) for f in filenames])
station69_2018 = station69_2018.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station69_2018_calidad = station69_2018.take([3], axis=1)
result = station69_2018_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows1 = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Station 69 has measurements that are invalid, but have a -1 or 1
station69_2018_measurements = station69_2018.take([2], axis=1)
result = station69_2018_measurements.isin([-9999])
rows2 = list(result['pm25'][result['pm25'] == True].index)

rows = [y for x in [rows1, rows2] for y in x]

# Replacing invalid values with NaN
station69_2018.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station69_2018 = station69_2018.take([0,2], axis=1)



## Location 78

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2018/estacion_data_calidadaire_78_*.csv')
filenames = sorted(filenames)

station78_2018 = pd.concat([pd.read_csv(f) for f in filenames])
station78_2018 = station78_2018.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station78_2018_calidad = station78_2018.take([3], axis=1)
result = station78_2018_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station78_2018.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station78_2018 = station78_2018.take([0,2], axis=1)

## Location 79

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2018/estacion_data_calidadaire_79_*.csv')
filenames = sorted(filenames)

station79_2018 = pd.concat([pd.read_csv(f) for f in filenames])
station79_2018 = station79_2018.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station79_2018_calidad = station79_2018.take([3], axis=1)
result = station79_2018_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station79_2018.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station79_2018 = station79_2018.take([0,2], axis=1)


## Location 80

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2018/estacion_data_calidadaire_80_*.csv')
filenames = sorted(filenames)

station80_2018 = pd.concat([pd.read_csv(f) for f in filenames])
station80_2018 = station80_2018.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station80_2018_calidad = station80_2018.take([3], axis=1)
result = station80_2018_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station80_2018.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station80_2018 = station80_2018.take([0,2], axis=1)


## Location 81

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2018/estacion_data_calidadaire_81_*.csv')
filenames = sorted(filenames)

station81_2018 = pd.concat([pd.read_csv(f) for f in filenames])
station81_2018 = station81_2018.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station81_2018_calidad = station81_2018.take([3], axis=1)
result = station81_2018_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station81_2018.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station81_2018 = station81_2018.take([0,2], axis=1)


## Location 82

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2018/estacion_data_calidadaire_82_*.csv')
filenames = sorted(filenames)

station82_2018 = pd.concat([pd.read_csv(f) for f in filenames])
station82_2018 = station82_2018.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station82_2018_calidad = station82_2018.take([3], axis=1)
result = station82_2018_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station82_2018.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station82_2018 = station82_2018.take([0,2], axis=1)


## Location 83

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2018/estacion_data_calidadaire_83_*.csv')
filenames = sorted(filenames)

station83_2018 = pd.concat([pd.read_csv(f) for f in filenames])
station83_2018 = station83_2018.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station83_2018_calidad = station83_2018.take([3], axis=1)
result = station83_2018_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station83_2018.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station83_2018 = station83_2018.take([0,2], axis=1)


## Location 84

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2018/estacion_data_calidadaire_84_*.csv')
filenames = sorted(filenames)

station84_2018 = pd.concat([pd.read_csv(f) for f in filenames])
station84_2018 = station84_2018.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station84_2018_calidad = station84_2018.take([3], axis=1)
result = station84_2018_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station84_2018.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station84_2018 = station84_2018.take([0,2], axis=1)


## Location 85

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2018/estacion_data_calidadaire_85_*.csv')
filenames = sorted(filenames)

station85_2018 = pd.concat([pd.read_csv(f) for f in filenames])
station85_2018 = station85_2018.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station85_2018_calidad = station85_2018.take([3], axis=1)
result = station85_2018_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station85_2018.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station85_2018 = station85_2018.take([0,2], axis=1)


## Location 86

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2018/estacion_data_calidadaire_86_*.csv')
filenames = sorted(filenames)

station86_2018 = pd.concat([pd.read_csv(f) for f in filenames])
station86_2018 = station86_2018.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station86_2018_calidad = station86_2018.take([3], axis=1)
result = station86_2018_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station86_2018.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station86_2018 = station86_2018.take([0,2], axis=1)


## Location 87

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2018/estacion_data_calidadaire_87_*.csv')
filenames = sorted(filenames)

station87_2018 = pd.concat([pd.read_csv(f) for f in filenames])
station87_2018 = station87_2018.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station87_2018_calidad = station87_2018.take([3], axis=1)
result = station87_2018_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station87_2018.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station87_2018 = station87_2018.take([0,2], axis=1)



## Location 88

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2018/estacion_data_calidadaire_88_*.csv')
filenames = sorted(filenames)

station88_2018 = pd.concat([pd.read_csv(f) for f in filenames])
station88_2018 = station88_2018.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station88_2018_calidad = station88_2018.take([3], axis=1)
result = station88_2018_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station88_2018.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station88_2018 = station88_2018.take([0,2], axis=1)


## Location 90

# Loading csv files for location 
filenames = glob('/home/mljmersie/Documents/SIATA/2018/estacion_data_calidadaire_90_*.csv')
filenames = sorted(filenames)

station90_2018 = pd.concat([pd.read_csv(f) for f in filenames])
station90_2018 = station90_2018.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station90_2018_calidad = station90_2018.take([3], axis=1)
result = station90_2018_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station90_2018.iloc[rows, 2] = np.nan

# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station90_2018 = station90_2018.take([0,2], axis=1)

# %%
# Year 2019

# %%

## Location 3

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2019/estacion_data_calidadaire_3_*.csv')
filenames = sorted(filenames)

station3_2019 = pd.concat([pd.read_csv(f) for f in filenames])
last2months = pd.concat([pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_11/estacion_data_calidadaire_3_20191101_20191130.csv'), pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_12/estacion_data_calidadaire_3_20191201_20191231.csv')])
station3_2019 = pd.concat([station3_2019, last2months])
station3_2019 = station3_2019.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station3_2019_calidad = station3_2019.take([3], axis=1)
result = station3_2019_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station3_2019.iloc[rows, 2] = np.nan


# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station3_2019 = station3_2019.take([0,2], axis=1)


## Location 12

# Loading csv files for location 12
filenames = glob('/home/mljmersie/Documents/SIATA/2019/estacion_data_calidadaire_12_*.csv')
filenames = sorted(filenames)

station12_2019 = pd.concat([pd.read_csv(f) for f in filenames])
last2months = pd.concat([pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_11/estacion_data_calidadaire_12_20191101_20191130.csv'), pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_12/estacion_data_calidadaire_12_20191201_20191231.csv')])
station12_2019 = pd.concat([station12_2019, last2months])
station12_2019 = station12_2019.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station12_2019_calidad = station12_2019.take([3], axis=1)
result = station12_2019_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station12_2019.iloc[rows, 2] = np.nan


# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station12_2019 = station12_2019.take([0,2], axis=1)


## Location 28

# Loading csv files for location 28
filenames = glob('/home/mljmersie/Documents/SIATA/2019/estacion_data_calidadaire_28_*.csv')
filenames = sorted(filenames)

station28_2019 = pd.concat([pd.read_csv(f) for f in filenames])
last2months = pd.concat([pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_11/estacion_data_calidadaire_28_20191101_20191130.csv'), pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_12/estacion_data_calidadaire_28_20191201_20191231.csv')])
station28_2019 = pd.concat([station28_2019, last2months])
station28_2019 = station28_2019.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station28_2019_calidad = station28_2019.take([3], axis=1)
result = station28_2019_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station28_2019.iloc[rows, 2] = np.nan


# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station28_2019 = station28_2019.take([0,2], axis=1)


## Location 31

# Loading csv files for location 31
filenames = glob('/home/mljmersie/Documents/SIATA/2019/estacion_data_calidadaire_31_*.csv')
filenames = sorted(filenames)

station31_2019 = pd.concat([pd.read_csv(f) for f in filenames])
last2months = pd.concat([pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_11/estacion_data_calidadaire_31_20191101_20191130.csv'), pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_12/estacion_data_calidadaire_31_20191201_20191231.csv')])
station31_2019 = pd.concat([station31_2019, last2months])
station31_2019 = station31_2019.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station31_2019_calidad = station31_2019.take([3], axis=1)
result = station31_2019_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station31_2019.iloc[rows, 2] = np.nan


# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station31_2019 = station31_2019.take([0,2], axis=1)



## Location 38

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2019/estacion_data_calidadaire_38_*.csv')
filenames = sorted(filenames)

station38_2019 = pd.concat([pd.read_csv(f) for f in filenames])
last2months = pd.concat([pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_11/estacion_data_calidadaire_38_20191101_20191130.csv'), pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_12/estacion_data_calidadaire_38_20191201_20191231.csv')])
station38_2019 = pd.concat([station38_2019, last2months])
station38_2019 = station38_2019.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station38_2019_calidad = station38_2019.take([3], axis=1)
result = station38_2019_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station38_2019.iloc[rows, 2] = np.nan


# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station38_2019 = station38_2019.take([0,2], axis=1)


## Location 44

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2019/estacion_data_calidadaire_44_*.csv')
filenames = sorted(filenames)

station44_2019 = pd.concat([pd.read_csv(f) for f in filenames])
last2months = pd.concat([pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_11/estacion_data_calidadaire_44_20191101_20191130.csv'), pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_12/estacion_data_calidadaire_44_20191201_20191231.csv')])
station44_2019 = pd.concat([station44_2019, last2months])
station44_2019 = station44_2019.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station44_2019_calidad = station44_2019.take([3], axis=1)
result = station44_2019_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station44_2019.iloc[rows, 2] = np.nan


# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station44_2019 = station44_2019.take([0,2], axis=1)


## Location 48

# Loading csv files for location 48
filenames = glob('/home/mljmersie/Documents/SIATA/2019/estacion_data_calidadaire_48_*.csv')
filenames = sorted(filenames)

station48_2019 = pd.concat([pd.read_csv(f) for f in filenames])
last2months = pd.concat([pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_11/estacion_data_calidadaire_48_20191101_20191130.csv'), pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_12/estacion_data_calidadaire_48_20191201_20191231.csv')])
station48_2019 = pd.concat([station48_2019, last2months])
station48_2019 = station48_2019.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station48_2019_calidad = station48_2019.take([3], axis=1)
result = station48_2019_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station48_2019.iloc[rows, 2] = np.nan


# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station48_2019 = station48_2019.take([0,2], axis=1)


## Location 69

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2019/estacion_data_calidadaire_69_*.csv')
filenames = sorted(filenames)

station69_2019 = pd.concat([pd.read_csv(f) for f in filenames])
last2months = pd.concat([pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_11/estacion_data_calidadaire_69_20191101_20191130.csv'), pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_12/estacion_data_calidadaire_69_20191201_20191231.csv')])
station69_2019 = pd.concat([station69_2019, last2months])
station69_2019 = station69_2019.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station69_2019_calidad = station69_2019.take([3], axis=1)
result = station69_2019_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station69_2019.iloc[rows, 2] = np.nan


# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station69_2019 = station69_2019.take([0,2], axis=1)


## Location 78

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2019/estacion_data_calidadaire_78_*.csv')
filenames = sorted(filenames)

station78_2019 = pd.concat([pd.read_csv(f) for f in filenames])
last2months = pd.concat([pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_11/estacion_data_calidadaire_78_20191101_20191130.csv'), pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_12/estacion_data_calidadaire_78_20191201_20191231.csv')])
station78_2019 = pd.concat([station78_2019, last2months])
station78_2019 = station78_2019.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station78_2019_calidad = station78_2019.take([3], axis=1)
result = station78_2019_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station78_2019.iloc[rows, 2] = np.nan


# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station78_2019 = station78_2019.take([0,2], axis=1)


## Location 79

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2019/estacion_data_calidadaire_79_*.csv')
filenames = sorted(filenames)

station79_2019 = pd.concat([pd.read_csv(f) for f in filenames])
last2months = pd.concat([pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_11/estacion_data_calidadaire_79_20191101_20191130.csv'), pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_12/estacion_data_calidadaire_79_20191201_20191231.csv')])
station79_2019 = pd.concat([station79_2019, last2months])
station79_2019 = station79_2019.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station79_2019_calidad = station79_2019.take([3], axis=1)
result = station79_2019_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station79_2019.iloc[rows, 2] = np.nan


# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station79_2019 = station79_2019.take([0,2], axis=1)


## Location 80

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2019/estacion_data_calidadaire_80_*.csv')
filenames = sorted(filenames)

station80_2019 = pd.concat([pd.read_csv(f) for f in filenames])
last2months = pd.concat([pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_11/estacion_data_calidadaire_80_20191101_20191130.csv'), pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_12/estacion_data_calidadaire_80_20191201_20191231.csv')])
station80_2019 = pd.concat([station80_2019, last2months])
station80_2019 = station80_2019.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station80_2019_calidad = station80_2019.take([3], axis=1)
result = station80_2019_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station80_2019.iloc[rows, 2] = np.nan


# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station80_2019 = station80_2019.take([0,2], axis=1)


## Location 81

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2019/estacion_data_calidadaire_81_*.csv')
filenames = sorted(filenames)

station81_2019 = pd.concat([pd.read_csv(f) for f in filenames])
last2months = pd.concat([pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_11/estacion_data_calidadaire_81_20191101_20191130.csv'), pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_12/estacion_data_calidadaire_81_20191201_20191231.csv')])
station81_2019 = pd.concat([station81_2019, last2months])
station81_2019 = station81_2019.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station81_2019_calidad = station81_2019.take([3], axis=1)
result = station81_2019_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station81_2019.iloc[rows, 2] = np.nan


# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station81_2019 = station81_2019.take([0,2], axis=1)


## Location 82

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2019/estacion_data_calidadaire_82_*.csv')
filenames = sorted(filenames)

station82_2019 = pd.concat([pd.read_csv(f) for f in filenames])
last2months = pd.concat([pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_11/estacion_data_calidadaire_82_20191101_20191130.csv'), pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_12/estacion_data_calidadaire_82_20191201_20191231.csv')])
station82_2019 = pd.concat([station82_2019, last2months])
station82_2019 = station82_2019.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station82_2019_calidad = station82_2019.take([3], axis=1)
result = station82_2019_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station82_2019.iloc[rows, 2] = np.nan


# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station82_2019 = station82_2019.take([0,2], axis=1)


## Location 83

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2019/estacion_data_calidadaire_83_*.csv')
filenames = sorted(filenames)

station83_2019 = pd.concat([pd.read_csv(f) for f in filenames])
last2months = pd.concat([pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_11/estacion_data_calidadaire_83_20191101_20191130.csv'), pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_12/estacion_data_calidadaire_83_20191201_20191231.csv')])
station83_2019 = pd.concat([station83_2019, last2months])
station83_2019 = station83_2019.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station83_2019_calidad = station83_2019.take([3], axis=1)
result = station83_2019_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station83_2019.iloc[rows, 2] = np.nan


# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station83_2019 = station83_2019.take([0,2], axis=1)


## Location 84

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2019/estacion_data_calidadaire_84_*.csv')
filenames = sorted(filenames)

station84_2019 = pd.concat([pd.read_csv(f) for f in filenames])
last2months = pd.concat([pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_11/estacion_data_calidadaire_84_20191101_20191130.csv'), pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_12/estacion_data_calidadaire_84_20191201_20191231.csv')])
station84_2019 = pd.concat([station84_2019, last2months])
station84_2019 = station84_2019.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station84_2019_calidad = station84_2019.take([3], axis=1)
result = station84_2019_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station84_2019.iloc[rows, 2] = np.nan


# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station84_2019 = station84_2019.take([0,2], axis=1)


## Location 85

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2019/estacion_data_calidadaire_85_*.csv')
filenames = sorted(filenames)

station85_2019 = pd.concat([pd.read_csv(f) for f in filenames])
last2months = pd.concat([pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_11/estacion_data_calidadaire_85_20191101_20191130.csv'), pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_12/estacion_data_calidadaire_85_20191201_20191231.csv')])
station85_2019 = pd.concat([station85_2019, last2months])
station85_2019 = station85_2019.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station85_2019_calidad = station85_2019.take([3], axis=1)
result = station85_2019_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station85_2019.iloc[rows, 2] = np.nan


# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station85_2019 = station85_2019.take([0,2], axis=1)


## Location 86

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2019/estacion_data_calidadaire_86_*.csv')
filenames = sorted(filenames)

station86_2019 = pd.concat([pd.read_csv(f) for f in filenames])
last2months = pd.concat([pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_11/estacion_data_calidadaire_86_20191101_20191130.csv'), pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_12/estacion_data_calidadaire_86_20191201_20191231.csv')])
station86_2019 = pd.concat([station86_2019, last2months])
station86_2019 = station86_2019.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station86_2019_calidad = station86_2019.take([3], axis=1)
result = station86_2019_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station86_2019.iloc[rows, 2] = np.nan


# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station86_2019 = station86_2019.take([0,2], axis=1)


## Location 87

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2019/estacion_data_calidadaire_87_*.csv')
filenames = sorted(filenames)

station87_2019 = pd.concat([pd.read_csv(f) for f in filenames])
last2months = pd.concat([pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_11/estacion_data_calidadaire_87_20191101_20191130.csv'), pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_12/estacion_data_calidadaire_87_20191201_20191231.csv')])
station87_2019 = pd.concat([station87_2019, last2months])
station87_2019 = station87_2019.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station87_2019_calidad = station87_2019.take([3], axis=1)
result = station87_2019_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station87_2019.iloc[rows, 2] = np.nan


# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station87_2019 = station87_2019.take([0,2], axis=1)


## Location 88

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2019/estacion_data_calidadaire_88_*.csv')
filenames = sorted(filenames)

station88_2019 = pd.concat([pd.read_csv(f) for f in filenames])
last2months = pd.concat([pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_11/estacion_data_calidadaire_88_20191101_20191130.csv'), pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_12/estacion_data_calidadaire_88_20191201_20191231.csv')])
station88_2019 = pd.concat([station88_2019, last2months])
station88_2019 = station88_2019.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station88_2019_calidad = station88_2019.take([3], axis=1)
result = station88_2019_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station88_2019.iloc[rows, 2] = np.nan


# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station88_2019 = station88_2019.take([0,2], axis=1)

## Location 90

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2019/estacion_data_calidadaire_90_*.csv')
filenames = sorted(filenames)

station90_2019 = pd.concat([pd.read_csv(f) for f in filenames])
last2months = pd.concat([pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_11/estacion_data_calidadaire_90_20191101_20191130.csv'), pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_12/estacion_data_calidadaire_90_20191201_20191231.csv')])
station90_2019 = pd.concat([station90_2019, last2months])
station90_2019 = station90_2019.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station90_2019_calidad = station90_2019.take([3], axis=1)
result = station90_2019_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station90_2019.iloc[rows, 2] = np.nan


# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station90_2019 = station90_2019.take([0,2], axis=1)


## Location 94

# Loading csv files for location 3
filenames = glob('/home/mljmersie/Documents/SIATA/2019/estacion_data_calidadaire_94_*.csv')
filenames = sorted(filenames)

station94_2019 = pd.concat([pd.read_csv(f) for f in filenames])
last2months = pd.concat([pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_11/estacion_data_calidadaire_94_20191101_20191130.csv'), pd.read_csv('/home/mljmersie/Documents/SIATA/SIATA_2019_12/estacion_data_calidadaire_94_20191201_20191231.csv')])
station94_2019 = pd.concat([station94_2019, last2months])
station94_2019 = station94_2019.reset_index(drop=True)

# Getting rid of bad measurements
# Note that the index 3 here corresponds to the column calidad_pm25

station94_2019_calidad = station94_2019.take([3], axis=1)
result = station94_2019_calidad.isin([-1,1])

 # Fetch the rows number where there is NOT a -1 or 1 present
rows = list(result['calidad_pm25'][result['calidad_pm25'] == False].index)

# Replacing invalid values with NaN
station94_2019.iloc[rows, 2] = np.nan


# Note that 0 and 2 belong respectively to the date and the pm2.5 value
station94_2019 = station94_2019.take([0,2], axis=1)

# %% Some stations started measuring somewhere in the year. The following section makes sure that the dataframe will be compatible with other stations, by extending the dataframe with NA values.

# Stations starting measurements in 2017
missing6months = pd.date_range('2017-01-01', periods = 4344, freq = 'h')
nomeasfirst6months = pd.DataFrame ({'Fecha_Hora' : missing6months})
nomeasfirst6months['pm25'] = np.nan

missing7months = pd.date_range('2017-01-01', periods = 5088, freq = 'h')
nomeasfirst7months = pd.DataFrame ({'Fecha_Hora' : missing7months})
nomeasfirst7months['pm25'] = np.nan

missing8months = pd.date_range('2017-01-01', periods = 5832, freq = 'h')
nomeasfirst8months = pd.DataFrame ({'Fecha_Hora' : missing8months})
nomeasfirst8months['pm25'] = np.nan

missing9months = pd.date_range('2017-01-01', periods = 6552, freq = 'h')
nomeasfirst9months = pd.DataFrame ({'Fecha_Hora' : missing9months})
nomeasfirst9months['pm25'] = np.nan

station69_2017 = pd.concat([nomeasfirst8months, station69_2017], axis=0)
station69_2017 = station69_2017.reset_index(drop=True)
station78_2017 = pd.concat([nomeasfirst6months, station78_2017], axis=0)
station78_2017 = station78_2017.reset_index(drop=True)
station79_2017 = pd.concat([nomeasfirst7months, station79_2017], axis=0)
station79_2017 = station79_2017.reset_index(drop=True)
station80_2017 = pd.concat([nomeasfirst7months, station80_2017], axis=0)
station80_2017 = station80_2017.reset_index(drop=True)
station81_2017 = pd.concat([nomeasfirst8months, station81_2017], axis=0)
station81_2017 = station81_2017.reset_index(drop=True)
station82_2017 = pd.concat([nomeasfirst8months, station82_2017], axis=0)
station82_2017 = station82_2017.reset_index(drop=True)
station83_2017 = pd.concat([nomeasfirst9months, station83_2017], axis=0)
station83_2017 = station83_2017.reset_index(drop=True)
station84_2017 = pd.concat([nomeasfirst9months, station84_2017], axis=0)
station84_2017 = station84_2017.reset_index(drop=True)
station85_2017 = pd.concat([nomeasfirst9months, station85_2017], axis=0)
station85_2017 = station85_2017.reset_index(drop=True)
station86_2017 = pd.concat([nomeasfirst9months, station86_2017], axis=0)
station86_2017 = station86_2017.reset_index(drop=True)
station87_2017 = pd.concat([nomeasfirst9months, station87_2017], axis=0)
station87_2017 = station87_2017.reset_index(drop=True)
station88_2017 = pd.concat([nomeasfirst9months, station88_2017], axis=0)
station88_2017 = station88_2017.reset_index(drop=True)

# Stations starting measurements in 2018
missing2months = pd.date_range('2018-01-01', periods = 1416, freq = 'h')
nomeasfirst2months = pd.DataFrame ({'Fecha_Hora' : missing2months})
nomeasfirst2months['pm25'] = np.nan

station90_2018 = pd.concat([nomeasfirst2months, station90_2018], axis=0)
station90_2018 = station90_2018.reset_index(drop=True)

# Stations starting measurements in 2019
missing1month = pd.date_range('2019-01-01', periods = 745, freq = 'h')
nomeasfirstmonth = pd.DataFrame ({'Fecha_Hora' : missing1month})
nomeasfirstmonth['pm25'] = np.nan

station94_2019 = pd.concat([nomeasfirstmonth, station94_2019], axis=0)
station94_2019 = station94_2019.reset_index(drop=True)


# %% 
#"The next two sections should be uncommented if it is desired to plot the weekly averages"
## Bundling for every year
#"Note that in this section we only use the stations in the URBAN area, which is the area of interest"
#"i.e. weĺl dismiss stations 3, 31, 69, 81, 82, 94"
#
## 2016
## Concatenating all stations for the year 2016
#stations2016 = pd.concat([station12_2016, station28_2016, station38_2016, station44_2016, station48_2016], axis=1)
#
## Finding averages and variances for every hour
#stations2016['Mean'] = stations2016.mean(axis=1)
#
## Finding weekly averages
#weeklyaverages2016 = []
#for i in range(0,52):
#    average = np.mean(stations2016.iloc[range(i*168,(i+1)*168),-1])
#    weeklyaverages2016 = weeklyaverages2016 + [average]
## Last week should be done differently since it is not a "full week"
#average = np.mean(stations2016.iloc[range((i+1)*168,len(stations2016)), -1])
#weeklyaverages2016 = weeklyaverages2016 + [average]
#
## Creating dataframe and changing indices
#weeklyaverages2016 = pd.DataFrame(data=weeklyaverages2016)
#weeklyaverages2016.index += 1
#weeklyaverages2016.columns = ['pm25']
#
#
## 2017
## Concatenating all stations for the year 2017
#stations2017 = pd.concat([station12_2017, station28_2017, station38_2017, station44_2017, station48_2017, station78_2017, station79_2017, station80_2017, station83_2017, station84_2017, station85_2017, station86_2017, station87_2017, station88_2017], axis=1)
#
## Finding averages and variances for every hour
#stations2017['Mean'] = stations2017.mean(axis=1)
#
## Finding weekly averages
#weeklyaverages2017 = []
#for i in range(0,52):
#    average = np.mean(stations2017.iloc[range(i*168,(i+1)*168),-1])
#    weeklyaverages2017 = weeklyaverages2017 + [average]
## Last week should be done differently since it is not a "full week"
#average = np.mean(stations2017.iloc[range((i+1)*168,len(stations2017)), -1])
#weeklyaverages2017 = weeklyaverages2017 + [average]
#
## Creating dataframe and changing indices
#weeklyaverages2017 = pd.DataFrame(data=weeklyaverages2017)
#weeklyaverages2017.index += 1
#weeklyaverages2017.columns = ['pm25']
#
#
## 2018
## Concatenating all stations for the year 2018
#stations2018 = pd.concat([station12_2018, station28_2018, station38_2018, station44_2018, station48_2018, station78_2018, station79_2018, station80_2018, station83_2018, station84_2018, station85_2018, station86_2018, station87_2018, station88_2018, station90_2018], axis=1)
#
## Finding averages and variances for every hour
#stations2018['Mean'] = stations2018.mean(axis=1)
#
## Finding weekly averages
#weeklyaverages2018 = []
#for i in range(0,52):
#    average = np.mean(stations2018.iloc[range(i*168,(i+1)*168),-1])
#    weeklyaverages2018 = weeklyaverages2018 + [average]
## Last week should be done differently since it is not a "full week"
#average = np.mean(stations2018.iloc[range((i+1)*168,len(stations2018)), -1])
#weeklyaverages2018 = weeklyaverages2018 + [average]
#
## Creating dataframe and changing indices
#weeklyaverages2018 = pd.DataFrame(data=weeklyaverages2018)
#weeklyaverages2018.index += 1
#weeklyaverages2018.columns = ['pm25']
#
#
## 2019
## Concatenating all stations for the year 2019
#stations2019 = pd.concat([station12_2019, station28_2019, station38_2019, station44_2019, station48_2019, station78_2019, station79_2019, station80_2019, station83_2019, station84_2019, station85_2019, station86_2019, station87_2019, station88_2019, station90_2019, station94_2019], axis=1)
#
## Finding averages and variances for every hour
#stations2019['Mean'] = stations2019.mean(axis=1)
#
## Finding weekly averages
#weeklyaverages2019 = []
#for i in range(0,52):
#    average = np.mean(stations2019.iloc[range(i*168,(i+1)*168),-1])
#    weeklyaverages2019 = weeklyaverages2019 + [average]
## Last week should be done differently since it is not a "full week"
#average = np.mean(stations2019.iloc[range((i+1)*168,len(stations2019)), -1])
#weeklyaverages2019 = weeklyaverages2019 + [average]
#
## Creating dataframe and changing indices
#weeklyaverages2019 = pd.DataFrame(data=weeklyaverages2019)
#weeklyaverages2019.index += 1
#weeklyaverages2019.columns = ['pm25']
#
# %% Plotting weekly averages of several years against eachother
#
#AVG = {'2016' : weeklyaverages2016.pm25, '2017' : weeklyaverages2017.pm25, '2018' : weeklyaverages2018.pm25, '2019' : weeklyaverages2019.pm25}
#AVGDF = pd.DataFrame(data = AVG)
#
#sns.set(style = "darkgrid")
#ax = sns.lineplot(data=AVGDF).set_title("Average concentration of PM2.5 in the urban area")
#plt.xlabel('Week number')
#plt.ylabel('PM2.5 (\u03BCg/m3)')
#plt.show(ax)






# %% 
"The next two sections should be uncommented if it is desired to plot overlapping windows"
# Bundling for every year
"Note that in this section we only use the stations in the URBAN area, which is the area of interest"
"i.e. weĺl dismiss stations 3, 31, 69, 81, 82, 94"

# 2016
# Concatenating all stations for the year 2016
stations2016 = pd.concat([station12_2016, station28_2016, station38_2016, station44_2016, station48_2016], axis=1)

# Finding averages and variances for every hour
stations2016['Mean'] = stations2016.mean(axis=1)

# Finding averages of overlapping windows
# The overlapping windows will have a span of 7 days and a stepsize of 3 days, i.e. there will be 120 of these windows every year.

ovwindowaverages2016 = []
for i in range(0,120):
    average = np.mean(stations2016.iloc[range(72*i,72*i+168),-1])
    ovwindowaverages2016 = ovwindowaverages2016 + [average]
    
# Last overlapping windows should be done differently since it is only a full not a "full week"
average = np.mean(stations2016.iloc[range(72*i+168,len(stations2016)), -1])
ovwindowaverages2016 = ovwindowaverages2016 + [average]

# Creating dataframe and changing indices
ovwindowaverages2016 = pd.DataFrame(data=ovwindowaverages2016)
ovwindowaverages2016.index += 1
ovwindowaverages2016.columns = ['pm25']


# 2017
# Concatenating all stations for the year 2017
stations2017 = pd.concat([station12_2017, station28_2017, station38_2017, station44_2017, station48_2017, station78_2017, station79_2017, station80_2017, station83_2017, station84_2017, station85_2017, station86_2017, station87_2017, station88_2017], axis=1)

# Finding averages and variances for every hour
stations2017['Mean'] = stations2017.mean(axis=1)

# Finding averages of overlapping windows
# The overlapping windows will have a span of 7 days and a stepsize of 3 days, i.e. there will be 120 of these windows every year.

ovwindowaverages2017 = []
for i in range(0,119):
    average = np.mean(stations2017.iloc[range(72*i,72*i+168),-1])
    ovwindowaverages2017 = ovwindowaverages2017 + [average]
    
# Last overlapping windows should be done differently since it is only a full not a "full week"
average = np.mean(stations2017.iloc[range(72*i+168,len(stations2017)), -1])
ovwindowaverages2017 = ovwindowaverages2017 + [average]

# Creating dataframe and changing indices
ovwindowaverages2017 = pd.DataFrame(data=ovwindowaverages2017)
ovwindowaverages2017.index += 1
ovwindowaverages2017.columns = ['pm25']


# 2018
# Concatenating all stations for the year 2018
stations2018 = pd.concat([station12_2018, station28_2018, station38_2018, station44_2018, station48_2018, station78_2018, station79_2018, station80_2018, station83_2018, station84_2018, station85_2018, station86_2018, station87_2018, station88_2018, station90_2018], axis=1)

# Finding averages and variances for every hour
stations2018['Mean'] = stations2018.mean(axis=1)

# Finding averages of overlapping windows
# The overlapping windows will have a span of 7 days and a stepsize of 3 days, i.e. there will be 120 of these windows every year.

ovwindowaverages2018 = []
for i in range(0,119):
    average = np.mean(stations2018.iloc[range(72*i,72*i+168),-1])
    ovwindowaverages2018 = ovwindowaverages2018 + [average]
    
# Last overlapping windows should be done differently since it is only a full not a "full week"
average = np.mean(stations2018.iloc[range(72*i+168,len(stations2018)), -1])
ovwindowaverages2018 = ovwindowaverages2018 + [average]

# Creating dataframe and changing indices
ovwindowaverages2018 = pd.DataFrame(data=ovwindowaverages2018)
ovwindowaverages2018.index += 1
ovwindowaverages2018.columns = ['pm25']


# 2019
# Concatenating all stations for the year 2019
stations2019 = pd.concat([station12_2019, station28_2019, station38_2019, station44_2019, station48_2019, station78_2019, station79_2019, station80_2019, station83_2019, station84_2019, station85_2019, station86_2019, station87_2019, station88_2019, station90_2019, station94_2019], axis=1)

# For some reason, the program creates a NaN row for the stations2019 dataframe. Here we get rid of this
stations2019.drop(stations2019.tail(1).index, inplace=True)

# Finding averages and variances for every hour
stations2019['Mean'] = stations2019.mean(axis=1)

# Finding averages of overlapping windows
# The overlapping windows will have a span of 7 days and a stepsize of 3 days, i.e. there will be 120 of these windows every year.

ovwindowaverages2019 = []
for i in range(0,119):
    average = np.mean(stations2019.iloc[range(72*i,72*i+168),-1])
    ovwindowaverages2019 = ovwindowaverages2019 + [average]
    
# Last overlapping windows should be done differently since it is only a full not a "full week"
average = np.mean(stations2019.iloc[range(72*i+168,len(stations2019)), -1])
ovwindowaverages2019 = ovwindowaverages2019 + [average]

# Creating dataframe and changing indices
ovwindowaverages2019 = pd.DataFrame(data=ovwindowaverages2019)
ovwindowaverages2019.index += 1
ovwindowaverages2019.columns = ['pm25']

# %% Plotting overlapping window averages of several years against eachother

OW = {'2016' : ovwindowaverages2016.pm25, '2017' : ovwindowaverages2017.pm25, '2018' : ovwindowaverages2018.pm25, '2019' : ovwindowaverages2019.pm25}
OWDF = pd.DataFrame(data = OW)

sns.set(style = "darkgrid")
ax = sns.lineplot(data=OWDF)
plt.title("Average concentration of PM2.5 in the urban area")
plt.xlabel('Month')
plt.ylabel('PM2.5 (\u03BCg/m3)')
labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

ax.set_xticklabels(labels)
ax.xaxis.set_major_locator(ticker.IndexLocator(base=10, offset=5))

plt.show(ax)

# %% Below this section was still in work a progress. 



# %%

## %% Bundling all data per station
#station3 = pd.concat([station3_2016, station3_2017, station3_2018, station3_2019])
##station3 = station3.reset_index(drop=True)
#
#station12 = pd.concat([station12_2016, station12_2017, station12_2018, station12_2019])
##station12 = station12.reset_index(drop=True)
#
#station28 = pd.concat([station28_2016, station28_2017, station28_2018, station28_2019])
##station28 = station28.reset_index(drop=True)
#
#station31 = pd.concat([station31_2016, station31_2017, station31_2018, station31_2019])
##station31 = station31.reset_index(drop=True)
#
#station38 = pd.concat([station38_2016, station38_2017, station38_2018, station38_2019])
##station38 = station38.reset_index(drop=True)
#
#station44 = pd.concat([station44_2016, station44_2017, station44_2018, station44_2019])
##station44 = station44.reset_index(drop=True)
#
#station48 = pd.concat([station48_2016, station48_2017, station48_2018, station48_2019])
##station48 = station48.reset_index(drop=True)
#
#station69 = pd.concat([#station69_2016, 
#        station69_2017, station69_2018, station69_2019])
##station69 = station69.reset_index(drop=True)
#
#station78 = pd.concat([#station78_2016, 
#        station78_2017, station78_2018, station78_2019])
##station78 = station78.reset_index(drop=True)
#
#station79 = pd.concat([#station79_2016, 
#        station79_2017, station79_2018, station79_2019])
##station79 = station79.reset_index(drop=True)
#
#station80 = pd.concat([#station80_2016, 
#        station80_2017, station80_2018, station80_2019])
##station80 = station80.reset_index(drop=True)
#
#station81 = pd.concat([#station81_2016, 
#        station81_2017, station81_2018, station81_2019])
##station81 = station81.reset_index(drop=True)
#
#station82 = pd.concat([#station82_2016, 
#        station82_2017, station82_2018, station82_2019])
##station82 = station82.reset_index(drop=True)
#
#station83 = pd.concat([#station83_2016, 
#        station83_2017, station83_2018, station83_2019])
##station83 = station83.reset_index(drop=True)
#
#station84 = pd.concat([#station84_2016, 
#        station84_2017, station84_2018, station84_2019])
##station84 = station84.reset_index(drop=True)
#
#station85 = pd.concat([#station85_2016, 
#        station85_2017, station85_2018, station85_2019])
##station85 = station85.reset_index(drop=True)
#
#station86 = pd.concat([#station86_2016, 
#        station86_2017, station86_2018, station86_2019])
##station86 = station86.reset_index(drop=True)
#
#station87 = pd.concat([#station87_2016, 
#        station87_2017, station87_2018, station87_2019])
##station87 = station87.reset_index(drop=True)
#
#station88 = pd.concat([#station88_2016, 
#        station88_2017, station88_2018, station88_2019])
##station88 = station88.reset_index(drop=True)
#
#station90 = pd.concat([#station90_2016, station90_2017, 
#        station90_2018, station90_2019])
##station90 = station90.reset_index(drop=True)
#
#station94 = pd.concat([#station94_2016, station94_2017, station94_2018, 
#        station94_2019])
##station94 = station94.reset_index(drop=True)
#
#   
## %% Time series
#
#"Note that the starting times have to be compatible with the station of interest"
#
#t_start1 = '2016-01-01 00:00:00'
#t_end1 = '2016-01-03 00:00:00'
#
#t_start2 = '2017-01-01 00:00:00'
#t_end2 = '2017-01-03 00:00:00'
#
#t_start3 = '2018-01-01 00:00:00'
#t_end3 = '2018-01-03 00:00:00'
#
#t_start4 = '2019-01-01 00:00:00'
#t_end4 = '2019-01-03 00:00:00'
#
#
#
#a = int(station3[station3['Fecha_Hora'] == t_start1].index.values)
#b = int(station3[station3['Fecha_Hora'] == t_end1].index.values)
#
#c = int(station3[station3['Fecha_Hora'] == t_start2].index.values)
#d = int(station3[station3['Fecha_Hora'] == t_end2].index.values)
#
#e = int(station3[station3['Fecha_Hora'] == t_start3].index.values)
#f= int(station3[station3['Fecha_Hora'] == t_end3].index.values)
#
#g = int(station3[station3['Fecha_Hora'] == t_start4].index.values)
#h = int(station3[station3['Fecha_Hora'] == t_end4].index.values)
#
##Making a dataframe for the stations from t_start1 - t_end1
#station3_1 = station3.iloc [list(range(a,b)),:]
#station3_1 = station3_1.reset_index(drop=True)
##station28_1 = station28.iloc [list(range(a,b)),:]
##station38_1 = station38.iloc [list(range(a,b)),:]
##station44_1 = station44.iloc [list(range(a,b)),:]
##station69_1 = station69.iloc [list(range(a,b)),:]
##station78_1 = station78.iloc [list(range(a,b)),:]
##station79_1 = station79.iloc [list(range(a,b)),:]
##station80_1 = station80.iloc [list(range(a,b)),:]
##station81_1 = station81.iloc [list(range(a,b)),:]
##station82_1 = station82.iloc [list(range(a,b)),:]
##station83_1 = station83.iloc [list(range(a,b)),:]
##station84_1 = station84.iloc [list(range(a,b)),:]
##station85_1 = station85.iloc [list(range(a,b)),:]
##station86_1 = station86.iloc [list(range(a,b)),:]
##station87_1 = station87.iloc [list(range(a,b)),:]
##station88_1 = station88.iloc [list(range(a,b)),:]
##station90_1 = station90.iloc [list(range(a,b)),:]
##station94_1 = station94.iloc [list(range(a,b)),:]
#
##Making a dataframe for the stations from t_start2 - t_end2
#station3_2 = station3.iloc [list(range(c,d)),:]
#station3_2 = station3_2.reset_index(drop=True)
##station28_2 = station28.iloc [list(range(c,d)),:]
##station38_2 = station38.iloc [list(range(c,d)),:]
##station44_2 = station44.iloc [list(range(c,d)),:]
##station69_2 = station69.iloc [list(range(c,d)),:]
##station78_2 = station78.iloc [list(range(c,d)),:]
##station79_2 = station79.iloc [list(range(c,d)),:]
##station80_2 = station80.iloc [list(range(c,d)),:]
##station81_2 = station81.iloc [list(range(c,d)),:]
##station82_2 = station82.iloc [list(range(c,d)),:]
##station83_2 = station83.iloc [list(range(c,d)),:]
##station84_2 = station84.iloc [list(range(c,d)),:]
##station85_2 = station85.iloc [list(range(c,d)),:]
##station86_2 = station86.iloc [list(range(c,d)),:]
##station87_2 = station87.iloc [list(range(c,d)),:]
##station88_2 = station88.iloc [list(range(c,d)),:]
##station90_2 = station90.iloc [list(range(c,d)),:]
##station94_2 = station94.iloc [list(range(c,d)),:]
#
##Making a dataframe for the stations from t_start3 - t_end3
#station3_3 = station3.iloc [list(range(e,f)),:]
#station3_3 = station3_3.reset_index(drop=True)
##station28_3 = station28.iloc [list(range(e,f)),:]
##station38_3 = station38.iloc [list(range(e,f)),:]
##station44_3 = station44.iloc [list(range(e,f)),:]
##station69_3 = station69.iloc [list(range(e,f)),:]
##station78_3 = station78.iloc [list(range(e,f)),:]
##station79_3 = station79.iloc [list(range(e,f)),:]
##station80_3 = station80.iloc [list(range(e,f)),:]
##station81_3 = station81.iloc [list(range(e,f)),:]
##station82_3 = station82.iloc [list(range(e,f)),:]
##station83_3 = station83.iloc [list(range(e,f)),:]
##station84_3 = station84.iloc [list(range(e,f)),:]
##station85_3 = station85.iloc [list(range(e,f)),:]
##station86_3 = station86.iloc [list(range(e,f)),:]
##station87_3 = station87.iloc [list(range(e,f)),:]
##station88_3 = station88.iloc [list(range(e,f)),:]
##station90_3 = station90.iloc [list(range(e,f)),:]
##station94_3 = station94.iloc [list(range(e,f)),:]
#
##Making a dataframe for the stations from t_start4 - t_end4
#station3_4 = station3.iloc [list(range(g,h)),:]
#station3_4 = station3_4.reset_index(drop=True)
##station28_4 = station28.iloc [list(range(g,h)),:]
##station38_4 = station38.iloc [list(range(g,h)),:]
##station44_4 = station44.iloc [list(range(g,h)),:]
##station69_4 = station69.iloc [list(range(g,h)),:]
##station78_4 = station78.iloc [list(range(g,h)),:]
##station79_4 = station79.iloc [list(range(g,h)),:]
##station80_4 = station80.iloc [list(range(g,h)),:]
##station81_4 = station81.iloc [list(range(g,h)),:]
##station82_4 = station82.iloc [list(range(g,h)),:]
##station83_4 = station83.iloc [list(range(g,h)),:]
##station84_4 = station84.iloc [list(range(g,h)),:]
##station85_4 = station85.iloc [list(range(g,h)),:]
##station86_4 = station86.iloc [list(range(g,h)),:]
##station87_4 = station87.iloc [list(range(g,h)),:]
##station88_4 = station88.iloc [list(range(g,h)),:]
##station90_4 = station90.iloc [list(range(g,h)),:]
##station94_4 = station94.iloc [list(range(g,h)),:]
#
##DATA = {'SIATA 3' : station3.pm25, 'SIATA 28' : station28.pm25}
##DATAFRAME = pd.DataFrame(data=DATA)
#
#COMP = {'SIATA 3-2016' : station3_1.pm25, 'SIATA 3-2017' : station3_2.pm25, 'SIATA 3-2018' : station3_3.pm25, 'SIATA 3-2019' : station3_4.pm25}
#COMPDF = pd.DataFrame(data = COMP)
#
##sns.set(style = "darkgrid")
##ax = sns.lineplot(data=DATAFRAME).set_title("Concentration of PM2.5 measured at different stations")
##plt.xlabel('Date')
##plt.ylabel('PM2.5 (\u03BCg/m3)')
##plt.show(ax)
#
#sns.set(style = "darkgrid")
#
#ax = sns.lineplot(data=COMPDF).set_title("Concentration of PM2.5 measured at the same station")
#plt.xlabel('Date')
#plt.ylabel('PM2.5 (\u03BCg/m3)')
#plt.show(ax)
#
## %% Interpolation
##locations = pd.read_csv('/home/mljmersie/Documents/IntroductiontoFolium/SIATA/SIATA LOCATIONS/Estaciones_CalidadAire.csv', encoding = "ISO-8859-1")
##
###Specify the locations from which we interpolate
##locationspm25 = [3, 28, 38, 44, 69, 78, 79]
##
##
##listloc = locations.isin(locationspm25)
##listloc = list(listloc['Codigo'][listloc['Codigo'] == True].index)
##
### Creating matrix for interpolation
##lrmatrix = np.zeros((len(locationspm25),7))
##lrmatrix[:, -1] = 1
##
##j=0
##for i in listloc:
##    lrmatrix[j,0] = locations.iat[i, 2]
##    lrmatrix[j,1] = locations.iat[i, 2]**2
##    lrmatrix[j,2] = locations.iat[i, 2]**3
##    lrmatrix[j,3] = locations.iat[i, 3]# %% Bundling all data per station
station3 = pd.concat([station3_2016, station3_2017, station3_2018, station3_2019])
#station3 = station3.reset_index(drop=True)

station12 = pd.concat([station12_2016, station12_2017, station12_2018, station12_2019])
#station12 = station12.reset_index(drop=True)

station28 = pd.concat([station28_2016, station28_2017, station28_2018, station28_2019])
#station28 = station28.reset_index(drop=True)

station31 = pd.concat([station31_2016, station31_2017, station31_2018, station31_2019])
#station31 = station31.reset_index(drop=True)

station38 = pd.concat([station38_2016, station38_2017, station38_2018, station38_2019])
#station38 = station38.reset_index(drop=True)

station44 = pd.concat([station44_2016, station44_2017, station44_2018, station44_2019])
#station44 = station44.reset_index(drop=True)

station48 = pd.concat([station48_2016, station48_2017, station48_2018, station48_2019])
#station48 = station48.reset_index(drop=True)

station69 = pd.concat([#station69_2016, 
        station69_2017, station69_2018, station69_2019])
#station69 = station69.reset_index(drop=True)

station78 = pd.concat([#station78_2016, 
        station78_2017, station78_2018, station78_2019])
#station78 = station78.reset_index(drop=True)

station79 = pd.concat([#station79_2016, 
        station79_2017, station79_2018, station79_2019])
#station79 = station79.reset_index(drop=True)

station80 = pd.concat([#station80_2016, 
        station80_2017, station80_2018, station80_2019])
#station80 = station80.reset_index(drop=True)

station81 = pd.concat([#station81_2016, 
        station81_2017, station81_2018, station81_2019])
#station81 = station81.reset_index(drop=True)

station82 = pd.concat([#station82_2016, 
        station82_2017, station82_2018, station82_2019])
#station82 = station82.reset_index(drop=True)

station83 = pd.concat([#station83_2016, 
        station83_2017, station83_2018, station83_2019])
#station83 = station83.reset_index(drop=True)

station84 = pd.concat([#station84_2016, 
        station84_2017, station84_2018, station84_2019])
#station84 = station84.reset_index(drop=True)

station85 = pd.concat([#station85_2016, 
        station85_2017, station85_2018, station85_2019])
#station85 = station85.reset_index(drop=True)

station86 = pd.concat([#station86_2016, 
        station86_2017, station86_2018, station86_2019])
#station86 = station86.reset_index(drop=True)

station87 = pd.concat([#station87_2016, 
        station87_2017, station87_2018, station87_2019])
#station87 = station87.reset_index(drop=True)

station88 = pd.concat([#station88_2016, 
        station88_2017, station88_2018, station88_2019])
#station88 = station88.reset_index(drop=True)

station90 = pd.concat([#station90_2016, station90_2017, 
        station90_2018, station90_2019])
#station90 = station90.reset_index(drop=True)

station94 = pd.concat([#station94_2016, station94_2017, station94_2018, 
        station94_2019])
#station94 = station94.reset_index(drop=True)

   
# %% Time series

#"Note that the starting times have to be compatible with the station of interest"
#
#t_start1 = '2016-01-01 00:00:00'
#t_end1 = '2016-01-03 00:00:00'
#
#t_start2 = '2017-01-01 00:00:00'
#t_end2 = '2017-01-03 00:00:00'
#
#t_start3 = '2018-01-01 00:00:00'
#t_end3 = '2018-01-03 00:00:00'
#
#t_start4 = '2019-01-01 00:00:00'
#t_end4 = '2019-01-03 00:00:00'
#
#
#
#a = int(station3[station3['Fecha_Hora'] == t_start1].index.values)
#b = int(station3[station3['Fecha_Hora'] == t_end1].index.values)
#
#c = int(station3[station3['Fecha_Hora'] == t_start2].index.values)
#d = int(station3[station3['Fecha_Hora'] == t_end2].index.values)
#
#e = int(station3[station3['Fecha_Hora'] == t_start3].index.values)
#f= int(station3[station3['Fecha_Hora'] == t_end3].index.values)
#
#g = int(station3[station3['Fecha_Hora'] == t_start4].index.values)
#h = int(station3[station3['Fecha_Hora'] == t_end4].index.values)
#
##Making a dataframe for the stations from t_start1 - t_end1
#station3_1 = station3.iloc [list(range(a,b)),:]
#station3_1 = station3_1.reset_index(drop=True)
#station28_1 = station28.iloc [list(range(a,b)),:]
#station38_1 = station38.iloc [list(range(a,b)),:]
#station44_1 = station44.iloc [list(range(a,b)),:]
#station69_1 = station69.iloc [list(range(a,b)),:]
#station78_1 = station78.iloc [list(range(a,b)),:]
#station79_1 = station79.iloc [list(range(a,b)),:]
#station80_1 = station80.iloc [list(range(a,b)),:]
#station81_1 = station81.iloc [list(range(a,b)),:]
#station82_1 = station82.iloc [list(range(a,b)),:]
#station83_1 = station83.iloc [list(range(a,b)),:]
#station84_1 = station84.iloc [list(range(a,b)),:]
#station85_1 = station85.iloc [list(range(a,b)),:]
#station86_1 = station86.iloc [list(range(a,b)),:]
#station87_1 = station87.iloc [list(range(a,b)),:]
#station88_1 = station88.iloc [list(range(a,b)),:]
#station90_1 = station90.iloc [list(range(a,b)),:]
#station94_1 = station94.iloc [list(range(a,b)),:]

#Making a dataframe for the stations from t_start2 - t_end2
#station3_2 = station3.iloc [list(range(c,d)),:]
#station3_2 = station3_2.reset_index(drop=True)
#station28_2 = station28.iloc [list(range(c,d)),:]
#station38_2 = station38.iloc [list(range(c,d)),:]
#station44_2 = station44.iloc [list(range(c,d)),:]
#station69_2 = station69.iloc [list(range(c,d)),:]
#station78_2 = station78.iloc [list(range(c,d)),:]
#station79_2 = station79.iloc [list(range(c,d)),:]
#station80_2 = station80.iloc [list(range(c,d)),:]
#station81_2 = station81.iloc [list(range(c,d)),:]
#station82_2 = station82.iloc [list(range(c,d)),:]
#station83_2 = station83.iloc [list(range(c,d)),:]
#station84_2 = station84.iloc [list(range(c,d)),:]
#station85_2 = station85.iloc [list(range(c,d)),:]
#station86_2 = station86.iloc [list(range(c,d)),:]
#station87_2 = station87.iloc [list(range(c,d)),:]
#station88_2 = station88.iloc [list(range(c,d)),:]
#station90_2 = station90.iloc [list(range(c,d)),:]
#station94_2 = station94.iloc [list(range(c,d)),:]

#Making a dataframe for the stations from t_start3 - t_end3
#station3_3 = station3.iloc [list(range(e,f)),:]
#station3_3 = station3_3.reset_index(drop=True)
#station28_3 = station28.iloc [list(range(e,f)),:]
#station38_3 = station38.iloc [list(range(e,f)),:]
#station44_3 = station44.iloc [list(range(e,f)),:]
#station69_3 = station69.iloc [list(range(e,f)),:]
#station78_3 = station78.iloc [list(range(e,f)),:]
#station79_3 = station79.iloc [list(range(e,f)),:]
#station80_3 = station80.iloc [list(range(e,f)),:]
#station81_3 = station81.iloc [list(range(e,f)),:]
#station82_3 = station82.iloc [list(range(e,f)),:]
#station83_3 = station83.iloc [list(range(e,f)),:]
#station84_3 = station84.iloc [list(range(e,f)),:]
#station85_3 = station85.iloc [list(range(e,f)),:]
#station86_3 = station86.iloc [list(range(e,f)),:]
#station87_3 = station87.iloc [list(range(e,f)),:]
#station88_3 = station88.iloc [list(range(e,f)),:]
#station90_3 = station90.iloc [list(range(e,f)),:]
#station94_3 = station94.iloc [list(range(e,f)),:]

#Making a dataframe for the stations from t_start4 - t_end4
#station3_4 = station3.iloc [list(range(g,h)),:]
#station3_4 = station3_4.reset_index(drop=True)
#station28_4 = station28.iloc [list(range(g,h)),:]
#station38_4 = station38.iloc [list(range(g,h)),:]
#station44_4 = station44.iloc [list(range(g,h)),:]
#station69_4 = station69.iloc [list(range(g,h)),:]
#station78_4 = station78.iloc [list(range(g,h)),:]
#station79_4 = station79.iloc [list(range(g,h)),:]
#station80_4 = station80.iloc [list(range(g,h)),:]
#station81_4 = station81.iloc [list(range(g,h)),:]
#station82_4 = station82.iloc [list(range(g,h)),:]
#station83_4 = station83.iloc [list(range(g,h)),:]
#station84_4 = station84.iloc [list(range(g,h)),:]
#station85_4 = station85.iloc [list(range(g,h)),:]
#station86_4 = station86.iloc [list(range(g,h)),:]
#station87_4 = station87.iloc [list(range(g,h)),:]
#station88_4 = station88.iloc [list(range(g,h)),:]
#station90_4 = station90.iloc [list(range(g,h)),:]
#station94_4 = station94.iloc [list(range(g,h)),:]

#DATA = {'SIATA 3' : station3.pm25, 'SIATA 28' : station28.pm25}
#DATAFRAME = pd.DataFrame(data=DATA)

#COMP = {'SIATA 3-2016' : station3_1.pm25, 'SIATA 3-2017' : station3_2.pm25, 'SIATA 3-2018' : station3_3.pm25, 'SIATA 3-2019' : station3_4.pm25}
#COMPDF = pd.DataFrame(data = COMP)

#sns.set(style = "darkgrid")
#ax = sns.lineplot(data=DATAFRAME).set_title("Concentration of PM2.5 measured at different stations")
#plt.xlabel('Date')
#plt.ylabel('PM2.5 (\u03BCg/m3)')
#plt.show(ax)

#sns.set(style = "darkgrid")
#
#ax = sns.lineplot(data=COMPDF).set_title("Concentration of PM2.5 measured at the same station")
#plt.xlabel('Date')
#plt.ylabel('PM2.5 (\u03BCg/m3)')
#plt.show(ax)

# %% Interpolation
#locations = pd.read_csv('/home/mljmersie/Documents/IntroductiontoFolium/SIATA/SIATA LOCATIONS/Estaciones_CalidadAire.csv', encoding = "ISO-8859-1")
#
##Specify the locations from which we interpolate
#locationspm25 = [3, 28, 38, 44, 69, 78, 79]
#
#
#listloc = locations.isin(locationspm25)
#listloc = list(listloc['Codigo'][listloc['Codigo'] == True].index)
#
## Creating matrix for interpolation
#lrmatrix = np.zeros((len(locationspm25),7))
#lrmatrix[:, -1] = 1
#
#j=0
#for i in listloc:
#    lrmatrix[j,0] = locations.iat[i, 2]
#    lrmatrix[j,1] = locations.iat[i, 2]**2
#    lrmatrix[j,2] = locations.iat[i, 2]**3
#    lrmatrix[j,3] = locations.iat[i, 3]
#    lrmatrix[j,4] = locations.iat[i, 3]**2
#    lrmatrix[j,5] = locations.iat[i, 3]**3    
#    j=j+1

# %% Time series based on code from Nicolás
#
## Convert to datetime
#station3['Fecha_Hora'] = pd.to_datetime(station3['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
#station28['Fecha_Hora'] = pd.to_datetime(station28['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
#station38['Fecha_Hora'] = pd.to_datetime(station38['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
#station44['Fecha_Hora'] = pd.to_datetime(station44['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
#station69['Fecha_Hora'] = pd.to_datetime(station69['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
#station78['Fecha_Hora'] = pd.to_datetime(station78['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
#station79['Fecha_Hora'] = pd.to_datetime(station79['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
#station80['Fecha_Hora'] = pd.to_datetime(station80['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
#station81['Fecha_Hora'] = pd.to_datetime(station81['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
#station82['Fecha_Hora'] = pd.to_datetime(station82['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
#station83['Fecha_Hora'] = pd.to_datetime(station83['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
#station84['Fecha_Hora'] = pd.to_datetime(station84['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
#station85['Fecha_Hora'] = pd.to_datetime(station85['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
#station86['Fecha_Hora'] = pd.to_datetime(station86['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
#station87['Fecha_Hora'] = pd.to_datetime(station87['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
#station88['Fecha_Hora'] = pd.to_datetime(station88['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
#station90['Fecha_Hora'] = pd.to_datetime(station90['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
#station94['Fecha_Hora'] = pd.to_datetime(station94['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
#
#
## Putting datetime as the index
#station3.set_index('Fecha_Hora', inplace=True)
#station28.set_index('Fecha_Hora', inplace=True)
#station38.set_index('Fecha_Hora', inplace=True)
#station44.set_index('Fecha_Hora', inplace=True)
#station69.set_index('Fecha_Hora', inplace=True)
#station78.set_index('Fecha_Hora', inplace=True)
#station79.set_index('Fecha_Hora', inplace=True)
#station80.set_index('Fecha_Hora', inplace=True)
#station81.set_index('Fecha_Hora', inplace=True)
#station82.set_index('Fecha_Hora', inplace=True)
#station83.set_index('Fecha_Hora', inplace=True)
#station84.set_index('Fecha_Hora', inplace=True)
#station85.set_index('Fecha_Hora', inplace=True)
#station86.set_index('Fecha_Hora', inplace=True)
#station87.set_index('Fecha_Hora', inplace=True)
#station88.set_index('Fecha_Hora', inplace=True)
#station90.set_index('Fecha_Hora', inplace=True)
#station94.set_index('Fecha_Hora', inplace=True)
#
#
#t_start1 = '2016-01-01 00:00:00'
#t_end1 = '2016-05-01 00:00:00'
#
#t_start2 = '2017-01-01 00:00:00'
#t_end2 = '2017-05-01 00:00:00'
#
#t_start3 = '2018-01-01 00:00:00'
#t_end3 = '2018-05-01 00:00:00'
#
#datadic = {'SIATA 3.1' : station3.loc[t_start1:t_end1].pm25, 'SIATA 3.2' : station3.loc[t_start2:t_end2].pm25, 'SIATA 3.3' : station3.loc[t_start3:t_end3].pm25}
##datadic2 = {'SIATA 3' : station3.loc[t_start:t_end].pm25, 'SIATA 28' : station28.loc[t_start:t_end].pm25, 'SIATA 38' : station38.loc[t_start:t_end].pm25}#, 'SIATA 44' : station44.loc[t_start:t_end].pm25, 'SIATA 78' : station78.loc[t_start:t_end].pm25,'SIATA 79' : station79.loc[t_start:t_end].pm25}#, 'SIATA 80' : station80.loc[t_start:t_end].pm25, 'SIATA 81' : station81.loc[t_start:t_end].pm25}#, 'SIATA 82' : station82.loc[t_start:t_end].pm25, 'SIATA 83' : station83.loc[t_start:t_end].pm25, 'SIATA 84' : station84.loc[t_start:t_end].pm25, 'SIATA 85' : station85.loc[t_start:t_end].pm25, 'SIATA 86' : station86.loc[t_start:t_end].pm25, 'SIATA 87' : station87.loc[t_start:t_end].pm25, 'SIATA 88' : station88.loc[t_start:t_end].pm25, 'SIATA 90' : station90.loc[t_start:t_end].pm25, 'SIATA 94' : station94.loc[t_start:t_end].pm25}
#
#
#df = pd.DataFrame(data=datadic)
#
#
#sns.set(style = "darkgrid")
#ax = sns.lineplot(data=df).set_title("Concentration of PM2.5 measured at different stations")
#plt.xlabel('Date')
#plt.ylabel('PM2.5 (\u03BCg/m3)')
#plt.show(ax)
#
#df['Mean'] = df.mean(axis=1)
#df['Min'] = df.min(axis=1)
#df['Max'] = df.max(axis=1)
#
#print("The minimum concentration measured inbetween " + t_start + " and " + t_end + " is " + str(min(df['Min'])))
#print("The average concentration measured inbetween " + t_start + " and " + t_end + " is " + str(df['Mean'].mean()))
#print("The maximum concentration measured inbetween " + t_start + " and " + t_end + " is " + str(max(df['Max'])))


# Scatterplot does not work yet, x-axis is weird
##    lrmatrix[j,4] = locations.iat[i, 3]**2
##    lrmatrix[j,5] = locations.iat[i, 3]**3    
##    j=j+1
#
## %% Time series based on code from Nicolás
##
### Convert to datetime
##station3['Fecha_Hora'] = pd.to_datetime(station3['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
##station28['Fecha_Hora'] = pd.to_datetime(station28['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
##station38['Fecha_Hora'] = pd.to_datetime(station38['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
##station44['Fecha_Hora'] = pd.to_datetime(station44['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
##station69['Fecha_Hora'] = pd.to_datetime(station69['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
##station78['Fecha_Hora'] = pd.to_datetime(station78['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
##station79['Fecha_Hora'] = pd.to_datetime(station79['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
##station80['Fecha_Hora'] = pd.to_datetime(station80['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
##station81['Fecha_Hora'] = pd.to_datetime(station81['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
##station82['Fecha_Hora'] = pd.to_datetime(station82['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
##station83['Fecha_Hora'] = pd.to_datetime(station83['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
##station84['Fecha_Hora'] = pd.to_datetime(station84['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
##station85['Fecha_Hora'] = pd.to_datetime(station85['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
##station86['Fecha_Hora'] = pd.to_datetime(station86['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
##station87['Fecha_Hora'] = pd.to_datetime(station87['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
##station88['Fecha_Hora'] = pd.to_datetime(station88['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
##station90['Fecha_Hora'] = pd.to_datetime(station90['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
##station94['Fecha_Hora'] = pd.to_datetime(station94['Fecha_Hora'], format='%Y-%m-%d %H:%M:%S')
##
##
### Putting datetime as the index
##station3.set_index('Fecha_Hora', inplace=True)
##station28.set_index('Fecha_Hora', inplace=True)
##station38.set_index('Fecha_Hora', inplace=True)
##station44.set_index('Fecha_Hora', inplace=True)
##station69.set_index('Fecha_Hora', inplace=True)
##station78.set_index('Fecha_Hora', inplace=True)
##station79.set_index('Fecha_Hora', inplace=True)
##station80.set_index('Fecha_Hora', inplace=True)
##station81.set_index('Fecha_Hora', inplace=True)
##station82.set_index('Fecha_Hora', inplace=True)
##station83.set_index('Fecha_Hora', inplace=True)
##station84.set_index('Fecha_Hora', inplace=True)
##station85.set_index('Fecha_Hora', inplace=True)
##station86.set_index('Fecha_Hora', inplace=True)
##station87.set_index('Fecha_Hora', inplace=True)
##station88.set_index('Fecha_Hora', inplace=True)
##station90.set_index('Fecha_Hora', inplace=True)
##station94.set_index('Fecha_Hora', inplace=True)
##
##
##t_start1 = '2016-01-01 00:00:00'
##t_end1 = '2016-05-01 00:00:00'
##
##t_start2 = '2017-01-01 00:00:00'
##t_end2 = '2017-05-01 00:00:00'
##
##t_start3 = '2018-01-01 00:00:00'
##t_end3 = '2018-05-01 00:00:00'
##
##datadic = {'SIATA 3.1' : station3.loc[t_start1:t_end1].pm25, 'SIATA 3.2' : station3.loc[t_start2:t_end2].pm25, 'SIATA 3.3' : station3.loc[t_start3:t_end3].pm25}
###datadic2 = {'SIATA 3' : station3.loc[t_start:t_end].pm25, 'SIATA 28' : station28.loc[t_start:t_end].pm25, 'SIATA 38' : station38.loc[t_start:t_end].pm25}#, 'SIATA 44' : station44.loc[t_start:t_end].pm25, 'SIATA 78' : station78.loc[t_start:t_end].pm25,'SIATA 79' : station79.loc[t_start:t_end].pm25}#, 'SIATA 80' : station80.loc[t_start:t_end].pm25, 'SIATA 81' : station81.loc[t_start:t_end].pm25}#, 'SIATA 82' : station82.loc[t_start:t_end].pm25, 'SIATA 83' : station83.loc[t_start:t_end].pm25, 'SIATA 84' : station84.loc[t_start:t_end].pm25, 'SIATA 85' : station85.loc[t_start:t_end].pm25, 'SIATA 86' : station86.loc[t_start:t_end].pm25, 'SIATA 87' : station87.loc[t_start:t_end].pm25, 'SIATA 88' : station88.loc[t_start:t_end].pm25, 'SIATA 90' : station90.loc[t_start:t_end].pm25, 'SIATA 94' : station94.loc[t_start:t_end].pm25}
##
##
##df = pd.DataFrame(data=datadic)
##
##
##sns.set(style = "darkgrid")
##ax = sns.lineplot(data=df).set_title("Concentration of PM2.5 measured at different stations")
##plt.xlabel('Date')
##plt.ylabel('PM2.5 (\u03BCg/m3)')
##plt.show(ax)
##
##df['Mean'] = df.mean(axis=1)
##df['Min'] = df.min(axis=1)
##df['Max'] = df.max(axis=1)
##
##print("The minimum concentration measured inbetween " + t_start + " and " + t_end + " is " + str(min(df['Min'])))
##print("The average concentration measured inbetween " + t_start + " and " + t_end + " is " + str(df['Mean'].mean()))
##print("The maximum concentration measured inbetween " + t_start + " and " + t_end + " is " + str(max(df['Max'])))
#
#
## Scatterplot does not work yet, x-axis is weird