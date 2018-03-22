# Data Analysis done on H1b Kaggle dataset for the year 2011-2016

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd # Pandas is a python package for easy manipulation of data strcutures and structured data , here in this case a CSV file
with open('h1b_kaggle.csv') as csvfile: # Opening the CSV file
 h1b = pd.read_csv ('h1b_kaggle.csv') # Reading the CSV file as pandas dataframe
 print(h1b.nunique()) #Prints the number of unique values in each column
 print("The number of unique Case Statuses are", h1b['CASE_STATUS'].unique()) #Displaying the number of unque case statuses(nan is not counted as a uniques case status type)
 print(h1b['CASE_STATUS'].dtype) #Printing the datatype of the CASE_STATUS column
 h1b = h1b.dropna (axis=0, how='any')#Dropping all nan values from the pandas data frame
 print(h1b.nunique())#Printing the number of uniques values after removing nan
print ("The number of unique Case Statuses are", h1b['CASE_STATUS'].unique ())#Displaying the number of unique case statuses after removing nan


# Petitions files per year
def petitionsYearly(a):
 return (h1b.loc[h1b.YEAR==a,['CASE_STATUS','EMPLOYER_NAME','SOC_NAME', 'JOB_TITLE','FULL_TIME_POSITION','PREVAILING_WAGE','WORKSITE']])

CS_2011=petitionsYearly(2011).shape[0]
CS_2012=petitionsYearly(2012).shape[0]
CS_2013=petitionsYearly(2013).shape[0]
CS_2014=petitionsYearly(2014).shape[0]
CS_2015=petitionsYearly(2015).shape[0]
CS_2016=petitionsYearly(2016).shape[0]
print(type(CS_2011))

height = [CS_2011,CS_2012,CS_2013,CS_2014,CS_2015,CS_2016]
bars = ('2011', '2012', '2013', '2014', '2015','2016')
y_pos = np.arange(len(bars))
#Create bars
plt.bar(bars, height)
# # Create names on the x-axis
plt.xlabel('Year')
plt.ylabel('No. of Petitions')
plt.title('Petitions filed over the years')
plt.xticks (y_pos, bars)
# # Show graphic
plt.show ()

# Petition case statuses over the 6 years
def caseStatuses(a):
 return (h1b.loc[
  h1b.CASE_STATUS == a, ['YEAR', 'EMPLOYER_NAME', 'SOC_NAME', 'JOB_TITLE', 'FULL_TIME_POSITION', 'PREVAILING_WAGE',
                    'WORKSITE']])

certWithdrawn=caseStatuses('CERTIFIED-WITHDRAWN').shape[0]
certified=caseStatuses('CERTIFIED').shape[0]
withdrawn=caseStatuses('WITHDRAWN').shape[0]
denied=caseStatuses('DENIED').shape[0]
rejected=caseStatuses('REJECTED').shape[0]
invalidated=caseStatuses('INVALIDATED').shape[0]
unassigned=caseStatuses('PENDING QUALITY AND COMPLIANCE REVIEW - UNASSIGNED').shape[0]


height = [certWithdrawn,certified,withdrawn,denied,rejected,invalidated,unassigned]
bars = ('CERTIFIED-WITHDRAWN', 'CERTIFIED', 'WITHDRAWN', 'DENIED', 'REJECTED','INVALIDATED','UNASSIGNED')
y_pos = np.arange(len(bars))
#Create bars
plt.bar(bars, height)
# # Create names on the x-axis
plt.xlabel('Case Status')
plt.ylabel('No. of Petitions')
plt.title('Petitions Statuses over the years')
plt.xticks (y_pos, bars)
# # Show graphic
plt.show ()

# Certified petitions yearly
def certifiedYearly(a):
 return (h1b.loc[
h1b.CASE_STATUS == 'CERTIFIED', ['YEAR', 'EMPLOYER_NAME', 'SOC_NAME', 'JOB_TITLE', 'FULL_TIME_POSITION', 'PREVAILING_WAGE',
                   'WORKSITE']])

certified2011=certifiedYearly(2011).shape[0]
certified2012=certifiedYearly(2012).shape[0]
certified2013=certifiedYearly(2013).shape[0]
certified2014=certifiedYearly(2014).shape[0]
certified2015=certifiedYearly(2015).shape[0]
certified2016=certifiedYearly(2016).shape[0]

height = [certified2011,certified2012,certified2013,certified2014,certified2015,certified2016]
bars = ('2011', '2012', '2013', '2014', '2015','2016')
y_pos = np.arange(len(bars))
#Create bars
plt.bar(bars, height)
# # Create names on the x-axis
plt.xlabel('Year')
plt.ylabel('No. of Petitions')
plt.title('Certified petitions over the years')
plt.xticks (y_pos, bars)
# # Show graphic
plt.show ()


#
# Yearly denied Petitions
def deniedYearly(a):
 return (CS_2011.loc[
CS_2011.CASE_STATUS == 'DENIED', ['YEAR', 'EMPLOYER_NAME', 'SOC_NAME', 'JOB_TITLE', 'FULL_TIME_POSITION', 'PREVAILING_WAGE',
                   'WORKSITE']])

denied2011=deniedYearly(2011)
denied2012=deniedYearly(2012)
denied2013=deniedYearly(2013)
denied2014=deniedYearly(2014)
denied2015=deniedYearly(2015)
denied2016=deniedYearly(2016)

print("Number of petitions certified in the year 2011 is ",(denied2011.shape[0]))
print("Number of petitions certified in the year 2011 is ",(denied2012.shape[0]))
print("Number of petitions certified in the year 2011 is ",(denied2013.shape[0]))
print("Number of petitions certified in the year 2011 is ",(denied2014.shape[0]))
print("Number of petitions certified in the year 2011 is ",(denied2015.shape[0]))
print("Number of petitions certified in the year 2011 is ",(denied2016.shape[0]))


# Yearly reject petitions
def rejectedYearly(a):
 return (CS_2011.loc[
CS_2011.CASE_STATUS == 'REJECTED', ['YEAR', 'EMPLOYER_NAME', 'SOC_NAME', 'JOB_TITLE', 'FULL_TIME_POSITION', 'PREVAILING_WAGE',
                   'WORKSITE']])

rejected2011=rejectedYearly(2011)
rejected2012=rejectedYearly(2012)
rejected2013=rejectedYearly(2013)
rejected2014=rejectedYearly(2014)
rejected2015=rejectedYearly(2015)
rejected2016=rejectedYearly(2016)

print("Number of petitions certified in the year 2011 is ",(rejected2011.shape[0]))
print("Number of petitions certified in the year 2011 is ",(rejected2012.shape[0]))
print("Number of petitions certified in the year 2011 is ",(rejected2013.shape[0]))
print("Number of petitions certified in the year 2011 is ",(rejected2014.shape[0]))
print("Number of petitions certified in the year 2011 is ",(rejected2015.shape[0]))
print("Number of petitions certified in the year 2011 is ",(rejected2016.shape[0]))


# Yearly withdrwan petitions
def withdrawnYearly(a):
 return (CS_2011.loc[
CS_2011.CASE_STATUS == 'WITHDRAWN', ['YEAR', 'EMPLOYER_NAME', 'SOC_NAME', 'JOB_TITLE', 'FULL_TIME_POSITION', 'PREVAILING_WAGE',
                   'WORKSITE']])

withdrawn2011=withdrawnYearly(2011)
withdrawn2012=withdrawnYearly(2012)
withdrawn2013=withdrawnYearly(2013)
withdrawn2014=withdrawnYearly(2014)
withdrawn2015=withdrawnYearly(2015)
withdrawn2016=withdrawnYearly(2016)

print("Number of petitions certified in the year 2011 is ",(withdrawn2011.shape[0]))
print("Number of petitions certified in the year 2011 is ",(withdrawn2012.shape[0]))
print("Number of petitions certified in the year 2011 is ",(withdrawn2013.shape[0]))
print("Number of petitions certified in the year 2011 is ",(withdrawn2014.shape[0]))
print("Number of petitions certified in the year 2011 is ",(withdrawn2015.shape[0]))
print("Number of petitions certified in the year 2011 is ",(withdrawn2015.shape[0]))
print(pd.Series(h1b['JOB_TITLE'].sort_values().unique()))

#Number of petitions filed by an employer
print(h1b.groupby('EMPLOYER_NAME').size().sort_values(ascending=False).reset_index(name='Petitions by employers'))
#Number of petitions filed by an job title
print(h1b.groupby('JOB_TITLE').size().sort_values(ascending=False).reset_index(name='Petitions for job title'))
#Number of petitions filed by an full time positions
print(h1b.groupby('FULL_TIME_POSITION').size().sort_values(ascending=False).reset_index(name='Petitions for FP'))
#Number of petitions filed by an worksites
print(h1b.groupby('WORKSITE').size().sort_values(ascending=False).reset_index(name='Petitions for sites'))
#
# Trend Data Science and Data Engineer Petitons over the years
def petitionsJobs(a,b):
 return (h1b.loc[h1b.YEAR==a],h1b.loc[h1b.JOB_TITLE==b])
petitionsDataEnigineer11=petitionsJobs(2011,'DATA ENGINEER')
petitionsDataScientist11=petitionsJobs(2011,'DATA SCIENTIST')
print("Number of Data Engineer petitions in year 2011 is ",pd.DataFrame(petitionsDataEnigineer11).shape[0])
print ("Number of Data Scientist petitions in year 2011 is", petitionsDataScientist11.count(2011))
def petitionsJobs(b):
 return (CS_2012.loc[h1b.JOB_TITLE==b])
petitionsDataEnigineer12=petitionsJobs('DATA ENGINEER')
petitionsDataScientist12=petitionsJobs('DATA SCIENTIST')
print("Number of Data Engineer petitions in year 2012 is ",petitionsDataEnigineer12.shape[0])
print ("Number of Data Scientist petitions in year 2012 is", petitionsDataScientist12.shape[0])
def petitionsJobs(b):
 return (CS_2013.loc[h1b.JOB_TITLE==b])
petitionsDataEnigineer13=petitionsJobs('DATA ENGINEER')
petitionsDataScientist13=petitionsJobs('DATA SCIENTIST')
print("Number of Data Engineer petitions in year 2013 is ",petitionsDataEnigineer13.shape[0])
print ("Number of Data Scientist petitions in year 2013 is", petitionsDataScientist13.shape[0])
def petitionsJobs(b):
 return (CS_2014.loc[h1b.JOB_TITLE==b])
petitionsDataEnigineer14=petitionsJobs('DATA ENGINEER')
petitionsDataScientist14=petitionsJobs('DATA SCIENTIST')
print("Number of Data Engineer petitions in year 2014 is ",petitionsDataEnigineer14.shape[0])
print ("Number of Data Scientist petitions in year 2014 is", petitionsDataScientist14.shape[0])
def petitionsJobs(b):
 return (CS_2015.loc[h1b.JOB_TITLE==b])
petitionsDataEnigineer15=petitionsJobs('DATA ENGINEER')
petitionsDataScientist15=petitionsJobs('DATA SCIENTIST')
print("Number of Data Engineer petitions in year 2015 is ",petitionsDataEnigineer15.shape[0])
print ("Number of Data Scientist petitions in year 2015 is", petitionsDataScientist15.shape[0])
def petitionsJobs(b):
 return (CS_2016.loc[h1b.JOB_TITLE==b])

petitionsDataEnigineer16=petitionsJobs('DATA ENGINEER')
petitionsDataScientist16=petitionsJobs('DATA SCIENTIST')
print("Number of Data Engineer petitions in year 2016 is ",petitionsDataEnigineer16.shape[0])
print ("Number of Data Scientist petitions in year 2016 is", petitionsDataScientist16.shape[0])













