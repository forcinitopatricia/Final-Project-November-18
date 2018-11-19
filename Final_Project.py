# import the pandas library.
import pandas as pd

# import a .csv file to a DataFrame
##df starts with 2010 but will contain all FYs
#To avoid problems with cells without UTF-8 format, we use enconding = 'ISO-8859-1

del df_all_years

df_all_years = pd.read_csv('RePORTER_PRJ_C_FY2010.csv', encoding='ISO-8859-1')
df_FY2011 = pd.read_csv('RePORTER_PRJ_C_FY2011.csv',encoding='ISO-8859-1')
df_FY2012 = pd.read_csv('RePORTER_PRJ_C_FY2012.csv',encoding='ISO-8859-1')
df_FY2013 = pd.read_csv('RePORTER_PRJ_C_FY2013.csv',encoding='ISO-8859-1')
df_FY2014 = pd.read_csv('RePORTER_PRJ_C_FY2014.csv',encoding='ISO-8859-1')
df_FY2015 = pd.read_csv('RePORTER_PRJ_C_FY2015.csv',encoding='ISO-8859-1')
df_FY2016 = pd.read_csv('RePORTER_PRJ_C_FY2016.csv',encoding='ISO-8859-1')
df_FY2017 = pd.read_csv('RePORTER_PRJ_C_FY2017.csv',encoding='ISO-8859-1')

#check column headers for df_all_header
df_all_years.columns
df_all_years.shape

#set appl ID as index
df_all_years.set_index('APPLICATION_ID', inplace=True)
df_FY2011.set_index('APPLICATION_ID', inplace=True)
df_FY2012.set_index('APPLICATION_ID', inplace=True)
df_FY2013.set_index('APPLICATION_ID', inplace=True)
df_FY2014.set_index('APPLICATION_ID', inplace=True)
df_FY2015.set_index('APPLICATION_ID', inplace=True)
df_FY2016.set_index('APPLICATION_ID', inplace=True)
df_FY2017.set_index('APPLICATION_ID', inplace=True)

#clean headers
df_all_years.columns = df_all_years.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-','_')
df_FY2011.columns = df_FY2011.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-','_')
df_FY2012.columns = df_FY2012.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-','_')
df_FY2013.columns = df_FY2013.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-','_')
df_FY2014.columns = df_FY2014.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-','_')
df_FY2015.columns = df_FY2015.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-','_')
df_FY2016.columns = df_FY2016.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-','_')
df_FY2017.columns = df_FY2017.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-','_')

#Creating a list with column headers

col_names_10 = list(df_all_years.columns)
col_names_10
col_names_11 = list(df_FY2011.columns)
col_names_11
col_names_12 = list(df_FY2012.columns)
col_names_12
col_names_13 = list(df_FY2013.columns)
col_names_13
col_names_14 = list(df_FY2014.columns)
col_names_14
col_names_15 = list(df_FY2015.columns)
col_names_15
col_names_16 = list(df_FY2016.columns)
col_names_16
col_names_17 = list(df_FY2017.columns)
col_names_17

# looking for the intersection
intersection= set(col_names_10) & set(col_names_11) & set(col_names_12) & set(col_names_14) & set(col_names_15) & set(col_names_16) & set(col_names_17)
intersection

#change set intersection for a list named columns_in_common
columns_in_common = list(intersection)
columns_in_common

#get info about columns_in_common
df_all_years[columns_in_common].info()



#looking for which are the extra columns
difference= set(col_names_12) - set(col_names_17)
difference


#drop 'direct cost' columns
df_12_43 = df_FY2012.drop(columns='indirect_cost_amt')
df_12_42 = df_12_43.drop(columns='direct_cost_amt')
df_12_42.shape

df_13_43 = df_FY2013.drop(columns='indirect_cost_amt')
df_13_42 = df_13_43.drop(columns='direct_cost_amt')
df_13_42.shape

df_14_44 = df_FY2014.drop(columns='indirect_cost_amt')
df_14_43 = df_14_44.drop(columns='direct_cost_amt')
df_14_42 = df_14_43.drop(columns='org_ipf_code')
df_14_42.shape

df_15_44 = df_FY2015.drop(columns='indirect_cost_amt')
df_15_43 = df_15_44.drop(columns='direct_cost_amt')
df_15_42 = df_15_43.drop(columns='org_ipf_code')
df_15_42.shape

df_16_44 = df_FY2016.drop(columns='indirect_cost_amt')
df_16_43 = df_16_44.drop(columns='direct_cost_amt')
df_16_42 = df_16_43.drop(columns='org_ipf_code')
df_16_42.shape

df_17_44 = df_FY2017.drop(columns='indirect_cost_amt')
df_17_43 = df_17_44.drop(columns='direct_cost_amt')
df_17_42 = df_17_43.drop(columns='org_ipf_code')
df_17_42.shape



#check column headers for df_all_header
df_all_years.shape

#Creating a list with column headers to check if all data frames have the same columns

col_names_12_42 = list(df_12_42.columns)
col_names_12_42

col_names_13_42 = list(df_13_42.columns)
col_names_13_42

col_names_14_42 = list(df_14_42.columns)
col_names_14_42

#looking for which are the extra columns
difference= set(col_names_12_42) - set(col_names_10)
difference

difference= set(col_names_12_42) - set(col_names_11)
difference

difference= set(col_names_13_42) - set(col_names_10)
difference

difference= set(col_names_13_42) - set(col_names_11)
difference

difference= set(col_names_14_42) - set(col_names_10)
difference

difference= set(col_names_14_42) - set(col_names_11)
difference

#now these are the dataframes that need to be combined
#df_12_42
#df_13_42
#df_14_42
#df_15_42
#df_16_42
#df_17_42
#df_all_years
#df_FY2011

#add FY10 to 17
df_10and11 = df_all_years.append(df_FY2011)
df_10and11.shape

df_10and11and12 = df_10and11.append(df_12_42)
df_10and11and12.shape

df_10and11and12and13 = df_10and11and12.append(df_13_42)
df_10and11and12and13

df_10and11and12and13and14=df_10and11and12and13.append(df_14_42)
df_10and11and12and13and14

df_10and11and12and13and14and15 = df_10and11and12and13and14.append(df_15_42)
df_10and11and12and13and14and15

df_10and11and12and13and14and15and16 = df_10and11and12and13and14and15.append(df_16_42)
df_10and11and12and13and14and15and16

df_10to17 = df_10and11and12and13and14and15and16.append(df_17_42)
df_10to17.info()

#sort data by admin ic
df_10to17_sorted = df_10to17.sort_values('administering_ic', axis=0, ascending=True)

#check for column admin ic to see if it is sorted alphabetically
df_10to17_sorted.iloc[:,1]

#How many cells are empty or NA in each column?
df_10to17_sorted.isnull().sum()
##Gives the same results ##df_10to17_sorted.isna().sum()

#List number of unique PI IDs
df_10to17_sorted_PIsNumber = df_10to17_sorted.pi_ids.unique()
len(df_10to17_sorted_PIsNumber)

# Count the groupby() function:
df_number_of_PIs_per_Year = df_10to17_sorted.groupby('fy')['pi_ids'].nunique()
type(df_number_of_PIs_per_Year)


# create a bar chart for number of PIs per year
import matplotlib.pyplot as plt
df_number_of_PIs_per_Year.plot(kind='bar')
plt.show()

# Count the number of applications per core grant
df_number_of_appls_per_core = df_10to17_sorted.groupby('fy')['core_project_num'].nunique()
len(df_number_of_appls_per_core)

df_number_of_appls_per_core.plot(kind='bar')
plt.show()
