#!/usr/bin/env python
# coding: utf-8

# Heroes Of Pymoli Data Analysis
# Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
# 
# Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).

# 
# Note
# Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()


# Player Count
# Display the total number of players

# In[2]:


count_unique_players = pd.DataFrame({"Total Players":[purchase_data["SN"].nunique()]})
count_unique_players


# Purchasing Analysis (Total)
# Run basic calculations to obtain number of unique items, average price, etc.
# Create a summary data frame to hold the results
# Optional: give the displayed data cleaner formatting
# Display the summary data frame

# In[3]:


count_unique_items = purchase_data["Item ID"].nunique()
average_price = purchase_data["Price"].mean()
total_purchases_of_item = purchase_data["Item ID"].count()
total_spent_on_item = purchase_data["Price"].sum()

purchase_analysis = pd.DataFrame(
    {"Number of Unique Items":[count_unique_items],
     "Average Price":[average_price],
     "Number of Purchases":[total_purchases_of_item],
     "Total Revenue":[total_spent_on_item]
    }
)

purchase_analysis = purchase_analysis.style.format({'Average Price':"\${:,.2f}", 'Total Revenue': "\${:,.2f}"}) 
purchase_analysis


# In[4]:


# Gender Demographics
purchase_data_gender = purchase_data.groupby(['Gender'])
total_players_gender = purchase_data_gender["SN"].nunique()
total_players_percent = total_players_gender / purchase_data["SN"].nunique() * 100

gender_breakdown_df = pd.concat([total_players_gender.rename("Count"), total_players_percent.rename("Percent")], axis=1)
gender_breakdown_df
# Percentage and Count of Male Players
# Percentage and Count of Female Players
# Percentage and Count of Other / Non-Disclosed


# Purchasing Analysis (Gender)
# Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# Create a summary data frame to hold the results
# Optional: give the displayed data cleaner formatting
# Display the summary data frame

# In[9]:


purchase_count_by_gender = purchase_data_gender["Item ID"].count()
average_purchase_by_gender = purchase_data_gender["Price"].mean()
total_purchase_by_gender = purchase_data_gender["Price"].sum()
average_price_by_gender = total_purchase_by_gender/total_players_gender

summary_df = pd.concat([purchase_count_by_gender.rename("Count"), average_purchase_by_gender.rename("Average Purchase"), total_purchase_by_gender.rename("Total"), average_price_by_gender.rename("Average Price")], axis=1)
summary_df
summary_df.style.format({'Average Purchase':"\${:,.2f}", 'Total': "\${:,.2f}", 'Average Price': "\${:,.2f}"})


# 
# Age Demographics
# Establish bins for ages
# Categorize the existing players using the age bins. Hint: use pd.cut()
# Calculate the numbers and percentages by age group
# Create a summary data frame to hold the results
# Optional: round the percentage column to two decimal points
# Display Age Demographics Table

# In[7]:


bins = [0, 10, 20, 30, 40, 100]
labels = ["10 and under", "11 - 20", "21 - 30", "31 - 40", "over 40"]
purchase_data["Group"] = pd.cut(purchase_data['Age'], bins, labels = labels)
grouped_purchase_data_df = purchase_data.groupby("Group")
count_ages_df = grouped_purchase_data_df["SN"].nunique()
percent_ages_df = count_ages_df/purchase_data["SN"].nunique() * 100

merged_df = pd.concat([count_ages_df.rename('Total Count'),percent_ages_df.rename('Percentage')],axis=1)
merged_df

merged_df.style.format({"Percentage": "{:.2f}%"})


# 
# Purchasing Analysis (Age)
# Bin the purchase_data data frame by age
# Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# Create a summary data frame to hold the results
# Optional: give the displayed data cleaner formatting
# Display the summary data frame

# In[13]:


total_purchase_age_count_df = grouped_purchase_data_df["Item ID"].count()
total_purchase_average_age_df = grouped_purchase_data_df["Price"].mean()
total_purchase_price_age_df = grouped_purchase_data_df["Price"].sum()
average_purchase_price_by_age_df = total_purchase_price_age_df/total_purchase_age_count_df

merged_summary_df = pd.concat([total_purchase_age_count_df.rename("Count"), total_purchase_average_age_df.rename("Value"), average_purchase_price_by_age_df.rename("Average")], axis=1)
merged_summary_df
merged_summary_df.style.format({"Value": "\${:,.2f}", "Average": "\${:,.2f}"})


# Top Spenders
# Run basic calculations to obtain the results in the table below
# Create a summary data frame to hold the results
# Sort the total purchase value column in descending order
# Optional: give the displayed data cleaner formatting
# Display a preview of the summary data frame

# In[20]:


top_spender_group = purchase_data.groupby("SN")
total_count_name = top_spender_group["Item ID"].count()
total_price_name = top_spender_group["Price"].sum()
average_purchase_by_name = total_price_name/total_count_name

top_spender_df = pd.concat([total_count_name.rename("Total Count"), total_price_name.rename("Total Price"), average_purchase_by_name.rename("Average")], axis=1)
top_spender_df

top_spender_df.style.format({"Total Price":"\${:,.2f}", "Average":"\${:,.2f}"})


# 
# Most Popular Items
# Retrieve the Item ID, Item Name, and Item Price columns
# Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# Create a summary data frame to hold the results
# Sort the purchase count column in descending order
# Optional: give the displayed data cleaner formatting
# Display a preview of the summary data frame

# In[28]:


popular_df = purchase_data[["Item ID", "Item Name", "Price"]]
popular_df = popular_df.groupby(["Item ID", "Item Name"])

items_counted_df = popular_df["Item ID"].count()
items_value_df = popular_df["Price"].sum()
item_price_average = items_value_df/items_counted_df

summarize_popularity_df = pd.concat([items_counted_df.rename("Count"), items_value_df.rename("Value"), item_price_average.rename("Average")], axis=1)
summarize_popularity_df

summarize_popularity_df.style.format({"Average":"\${:,.2f}", "Value":"\${:,.2f}"})


Most Profitable Items
Sort the above table by total purchase value in descending order
Optional: give the displayed data cleaner formatting
Display a preview of the data frame
# In[30]:


summarize_popularity_df.sort_values(["Value"], ascending=False).style.format({"Average":"\${:,.2f}", "Value":"\${:,.2f}"})

