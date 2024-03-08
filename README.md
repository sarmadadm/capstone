# Title: Unveiling Urban Road Challenges - NYC Pothole Prediction

## Overview 
A Data-Driven Exploration of Potholes in NYC with Predictive Modeling, Spatial Analysis, and Strategic Recommendations

## Introduction
In the bustling streets of New York City, where individuals spend an average of 2 hours daily navigating the vibrant urban landscape, the quality of their commuting experience is a critical factor. Imagine a scenario where this daily journey is marred by the presence of potholes, and unpredictable road hazards that not only pose a threat to vehicle safety but also significantly impact commute times. 

This data science project aims to tackle the issue head-on by leveraging advanced predictive modeling techniques to identify and forecast pothole locations across NYC. By analyzing historical data, weather patterns, road maintenance schedules, and other relevant factors, we seek to develop a robust predictive model that can anticipate the likelihood of pothole formation in different areas of the city. "The ultimate objective is to equip municipal authorities with real-time insights, enabling them to proactively address the issue by identifying and prioritizing potential pothole-prone areas in advance. 

through this project, we aim to contribute to the development of a smarter and more resilient urban transportation system in NYC, ultimately improving the quality of life for its residents and visitors.

## Impact
The occurrence of potholes is a common challenge faced by both drivers and pedestrians alike, leading to not only potential vehicle damage but also contributing to traffic congestion and increased travel times. By efficiently managing potholes, the city can potentially save millions of dollars in repair costs and minimize the environmental impact associated with frequent road maintenance. The project's societal value lies in improving the overall quality of transportation infrastructure in NYC, positively impacting businesses, residents, and the environment.


 
 ## The methodology is divided into the following key steps:
This is a high level overview of the methodology used in this project.

 **Data Collection:**
   * Potholes Data and Traffic Data used in this project is collected from "NYC OPEN DATA"
     Weather Data is imported from Kaggle which ranges from 1869 to 2022

   - Street_Pothole_Work_Orders_-_Closed__Dataset_ for Potholes
     Source: https://data.cityofnewyork.us/Transportation/Street-Pothole-Work-Orders-Closed-Dataset-/x9wy-ing4/about_data
   - NYC_Central_Park_weather_1869-2022 for weather
     Source: https://www.kaggle.com/datasets/danbraswell/new-york-city-weather-18692022
   - Automated_Traffic_Volume_Counts_20240306 for Traffic Volumes
     Source: https://data.cityofnewyork.us/Transportation/Automated-Traffic-Volume-Counts/7ym2-wayt/about_data


 **Data Processing, Cleaning and EDA:**
   - Clean and explore NYC_Potholes Data.
   - Look at Distributions of features.
   - Look at relationships between features.
   - Plot the Data for visual insights

## Jupyter Notebooks 

The Jupyter Notebooks will cover every Data Analysis, Cleaning and further steps.

 - EDA_CAPSTONE.ipnb

## Data Dictionary
This is a general data dictionary for Potholes Data. 
<details>
  <summary>Data Dictionary</summary>

- **FID:** Object, Unique Identifier of the Table.
- **Shape** Geometry, Polyline
- **DefNum:** Text, Defect Number.
- **InitBy:** Text, The unit that initiated the service action
- **HouseNum:** Text, House or building number on the street (for reports using exact address      locations)
- **OFT:** Text, OFT = On – From – To
NYC DOT values to describe a block segment (a six-byte code consisting of borough and five digit street code)
- **OnFaceName:** Text, Pothole Location: Main Street
- **OnPrimName:** Text, Pothole Location: Main Street’s Primary Name
- **FrmPrimNam:** Text, Pothole Location: From Street
- **ToPrimName:** Text, Pothole Location: To Street
- **SpecLoc:** Text, Defect Specific Location
- **Boro:** Text, Borough Code
   B – Brooklyn
   X – Bronx
   M – Manhattan Q – Queens
   S – Staten Island
- **Source:** Text, Origin of the Report
   CB – Community Board 
   CEN – Central, 40 Worth 
   COR – Correspondence 
   CTZ – Citizen
   DEP – Department of Environmental Protection 
   HIQ – HIQA
   KBO – Boro Office, Brooklyn MAP – Map
   MBO – Boro Office, Manhattan 
   OFF – Official
   OSE – Office of Special Events 
   OTH – Other
   PCT – Police PCT
   POL – Political Office HOL
   QBO – Boro Office, Queens 
   RAD – Radio Room
   RFU – Referral Unit
   SBO – Boro Office, Staten Island 
   TRF – Traffic Communications 
   XBO – Boro Office, Bronx
   YRD – Yard
- **RepStatus:** Text, Street Pothole Repair Status
   XCL = Closed
- **RptDate:** Date, Date the street pothole was reported
- **RptClosed:** Date, Date the street pothole report was closed
- **Shape_Leng:** Double, Length of Polyline in Feet

</details>
 


