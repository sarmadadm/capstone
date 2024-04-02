# Title: Unveiling Urban Road Challenges - NYC Pothole Prediction

## Overview 
A Data-Driven Exploration of Potholes in NYC with Predictive Modeling, Spatial Analysis, and Strategic Recommendations

## Introduction and Problem Statement
In NYC's busy streets, where people spend 40 mins daily commuting, road quality is crucial. Picture this: daily journeys disrupted by potholes and unpredictable hazards, endangering safety and delaying commutes. This project is vital. No prior work in this area exists, and I aim to assist authorities in tackling this issue effectively.

## Solution Proposal
This project aims to predict zip codes of pothole locations across NYC using latitudes and longitudes leveraging machine learning classification problem solutions. 
By analyzing historical data and road maintenance schedules, we'll develop a robust predictive model. Our objective is to provide real-time insights to municipal authorities, helping them proactively address pothole-prone areas. Ultimately, this initiative seeks to enhance NYC's urban transportation system and improve the quality of life for its residents and visitors.

## Impact
Potholes pose a common challenge for drivers and pedestrians, causing vehicle damage and traffic congestion. Efficient pothole management can save millions in repair costs and reduce environmental impact. This project aims to enhance NYC's transportation infrastructure, benefiting businesses, residents, and the environment.
 
 ## The methodology is divided into the following key steps:
This is a high level overview of the methodology used in this project.

 **Data Collection:**
   * Potholes Data and Traffic Data used in this project is collected from "NYC OPEN DATA"
     Weather Data is imported from Kaggle which ranges from 1869 to 2022

   - Street_Pothole_Work_Orders_-_Closed__Dataset_ for Potholes
     Source: https://data.cityofnewyork.us/Transportation/Street-Pothole-Work-Orders-Closed-Dataset-/x9wy-ing4/about_data

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
 


