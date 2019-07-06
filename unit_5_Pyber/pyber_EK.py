#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# File to Load (Remember to change these)
city_data_file = "city_data.csv"
ride_data_file = "ride_data.csv"

# Read the City and Ride Data
city_df = pd.read_csv(city_data_to_load)
ride_df = pd.read_csv(ride_data_to_load)

city_df.head()


# In[4]:


ride_df.head()


# In[6]:


# Combine the data into a single dataset
city_ride_df = pd.merge(ride_df, city_df, how='left', on='city')

# Display the data table for preview
city_ride_df.head()


# In[14]:


# Obtain the x and y coordinates for each of the three city types
city_urban = city_ride_df.loc[city_ride_df['type'] == "Urban"]
city_rural = city_ride_df.loc[city_ride_df['type'] == "Rural"]
city_suburban = city_ride_df.loc[city_ride_df['type'] == "Suburban"]

ride_urban = city_urban.groupby("city")["ride_id"].count()
ride_rural = city_rural.groupby("city")["ride_id"].count()
ride_suburban = city_suburban.groupby("city")["ride_id"].count()

avg_fare_urban = city_urban.groupby("city")["fare"].mean()
avg_fare_rural = city_rural.groupby("city")["fare"].mean()
avg_fare_suburban = city_suburban.groupby("city")["fare"].mean()

drivers_urban = city_urban.groupby("city")["driver_count"].mean()
drivers_rural = city_rural.groupby("city")["driver_count"].mean()
drivers_suburban = city_suburban.groupby("city")["driver_count"].mean()

# Build the scatter plots for each city types
plt.scatter(ride_urban, avg_fare_urban, s = drivers_urban * 10, color = 'gold', edgecolor = 'black', label = 'Urban', alpha = .8)
plt.scatter(ride_rural, avg_fare_rural, s = drivers_rural * 10, color = 'coral', edgecolor = 'black', label = 'Rural', alpha = .8)
plt.scatter(ride_suburban, avg_fare_suburban, s = drivers_suburban * 10, color = 'skyblue', edgecolor = 'black', label = 'Suburban', alpha = .8)

# Incorporate the other graph properties
plt.xlabel("Total Number of Rides Per City")
plt.ylabel("Average Fare in Dollars)")
plt.title("2016 Pyber Ride Sharing Data")

plt.grid()

# Format legend
legend = plt.legend(title= "City Types", loc="best")
frame = legend.get_frame()
frame.set_facecolor('#eeeeee')

# Incorporate a text label regarding circle size
plt.text(42,35,"Circle size correlates with\nnumber of drivers per city", fontsize = 10)

# Save Figure
plt.savefig('pyber_2016_data_ek.png')


# In[16]:


# Calculate Type Percents
sum_urban = city_urban["fare"].sum()
sum_rural = city_rural["fare"].sum()
sum_suburban = city_suburban["fare"].sum()


# In[29]:


# Build Pie Chart
labels = ["Urban", "Suburban", "Rural"]
plt.title("Percent of Total Fares by City Type", fontsize=14,y=1.5)
colors = ["gold", "skyblue", "coral"]
explode = (0.2, .05, .02)

sizes = [sum_urban, sum_suburban, sum_rural]

# Creates the pie chart based upon the values above
plt.pie(sizes, explode=explode,radius=2, labels=labels, colors=colors, autopct="%1.1f%%", startangle=300,  textprops={'fontsize': 14}, wedgeprops = {'linewidth': 1, 'edgecolor':'black'})


# In[30]:


# Save Figure
plt.savefig('percent_total_fares.png', bbox_inches="tight")


# In[31]:


# Calculate Ride Percents
ride_count_urban = city_urban["ride_id"].count()
ride_count_rural = city_rural["ride_id"].count()
ride_count_suburban = city_suburban["ride_id"].count()


# In[32]:


# Build Pie Chart
labels = ["Urban", "Suburban", "Rural"]
plt.title("Percent of Total Rides by City Type", fontsize=14,y=1.5)
colors = ["gold", "skyblue", "coral"]
explode = (0.2, .05, .03)

sizes = [ride_count_urban, ride_count_suburban, ride_count_rural]

plt.pie(sizes, explode=explode,radius=2, labels=labels, colors=colors, autopct="%1.1f%%", startangle=270,  textprops={'fontsize': 14}, wedgeprops = {'linewidth': 1, 'edgecolor':'black'})


# In[33]:


# Save Figure
plt.savefig('percent_total_rides.png', bbox_inches="tight")


# In[34]:


# Calculate Driver Percents
driver_count_urban = city_urban.groupby("city")["driver_count"].mean().sum()
driver_count_rural = city_rural.groupby("city")["driver_count"].mean().sum()
driver_count_suburban = city_suburban.groupby("city")["driver_count"].mean().sum()


# In[35]:


# Build Pie Charts
labels = ["Urban", "Suburban", "Rural"]
plt.title("Percent of Total Drivers by City Type", fontsize=14,y=1.5)
colors = ["gold", "skyblue", "coral"]
explode = (0.2, .04, .03)

sizes = [driver_count_urban, driver_count_suburban, driver_count_rural]

plt.pie(sizes, explode=explode,radius=2, labels=labels, colors=colors, autopct="%1.1f%%", startangle=270,  textprops={'fontsize': 14}, wedgeprops = {'linewidth': 1, 'edgecolor':'black'})


# In[36]:


# Save Figure
plt.savefig('percent_drivers.png', bbox_inches="tight")


# Trends
# It is more expensive to use Pyber in rural areas than in urban areas, likely because there are fewer rides being ordered.
# Lower costs in urban areas could be due to a higher number of drivers and/or higher number of rides ordered (ultimately, a question of supply and demand)
# There are some seeming extreme values in terms of cost and number of drivers for the rural rides.  They are likely having to travel further distances than urban or suburban counterparts.
