# Title: Unveiling Urban Road Challenges - NYC Pothole Prediction

Overview: A Data-Driven Exploration of Potholes in NYC with Predictive Modeling, Spatial Analysis, and Strategic Recommendations

Problem: 
In the bustling streets of New York City, where individuals spend an average of 2 hours daily navigating the vibrant urban landscape, the quality of their commuting experience is a critical factor. Imagine a scenario where this daily journey is marred by the presence of potholes, and unpredictable road hazards that not only pose a threat to vehicle safety but also significantly impact commute times. 

This data science project aims to tackle the issue head-on by leveraging advanced predictive modeling techniques to identify and forecast pothole locations across NYC. By analyzing historical data, weather patterns, road maintenance schedules, and other relevant factors, we seek to develop a robust predictive model that can anticipate the likelihood of pothole formation in different areas of the city. "The ultimate objective is to equip municipal authorities with real-time insights, enabling them to proactively address the issue by identifying and prioritizing potential pothole-prone areas in advance. 

through this project, we aim to contribute to the development of a smarter and more resilient urban transportation system in NYC, ultimately improving the quality of life for its residents and visitors.

The Impact: The occurrence of potholes is a common challenge faced by both drivers and pedestrians alike, leading to not only potential vehicle damage but also contributing to traffic congestion and increased travel times. By efficiently managing potholes, the city can potentially save millions of dollars in repair costs and minimize the environmental impact associated with frequent road maintenance. The project's societal value lies in improving the overall quality of transportation infrastructure in NYC, positively impacting businesses, residents, and the environment.

The Data:
NYC Open Data 311 Service Requests Dataset:
This dataset, available on NYC Open Data, contains information about service requests, including those related to potholes. It includes details such as the date of the request, location, and the status of the reported issue.
● Street Pothole Work Orders - Closed (Dataset) | NYC Open Data, https://data.cityofnewyork.us/Transportation/Street-Pothole-Work-Orders-Closed-Dataset-/x9wy-ing4/data

Data Dictionary: 

FID Object ID - Unique Identifier of the Table Shape Geometry - Polyline

DefNum Text 12 Defect Number InitBy Text 8 The unit that initiated the service action

HouseNum Text 12 House or building number on the street (for reports using exact address locations)

OFT Text 32 OFT = On – From – To NYC DOT values to describe a block segment (a six-byte code consisting of borough and five-digit street code)

OnFaceName Text 32 Pothole Location: Main Street

OnPrimName Text 32 Pothole Location: Main Street’s Primary Name

FrmPrimNam Text 32 Pothole Location: From Street

ToPrimName Text 32 Pothole Location: To Street

SpecLoc Text 50 Defect Specific Location

Boro Text 1 Borough Code B – Brooklyn
X – Bronx
M – Manhattan
Q – Queens
S – Staten Island

Source Text 3 Origin of the Report CB – Community Board
CEN – Central, 40 Worth
COR – Correspondence
CTZ – Citizen
DEP – Department of Environmental Protection
HIQ – HIQA
KBO – Boro Office, Brooklyn
MAP – Map
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

RepStatus Text 3 Street Pothole Repair Status XCL = Closed

RptDate Date - Date the street pothole was reported

RptClosed Date - The date the street pothole report was closed

Shape_Leng Double - Length of Polyline in Feet
