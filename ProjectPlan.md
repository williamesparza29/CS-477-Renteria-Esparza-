# Chicago Traffic Crash Analysis Project Plan
## Overview

Traffic crashes are a common issue in large cities like Chicago, and understanding what causes them can help identify patterns that lead to accidents. The goal of this project is to analyze traffic crash data directly from the City of Chicago to better understand what factors contribute to crashes.

The goal of this project is to analyze how vehicle maneuvers and vehicle types contribute to traffic crashes in Chicago.
To do this, we will use two datasets from the Chicago Open Data Portal: the Traffic Crashes dataset and the Traffic Crashes – Vehicles dataset. The crash dataset contains information about when and where crashes happened, as well as conditions such as weather, road conditions, and crash severity. The vehicles dataset contains information about the vehicles involved in crashes, including vehicle type and the maneuver the vehicle was performing before the crash.

Using Python and the Pandas library, we will clean and integrate the datasets using the shared identifier CRASH_RECORD_ID. After merging the datasets, we will analyze patterns in vehicle maneuvers and crash severity to see which types of driving actions appear most often in crashes and whether some maneuvers are linked to more serious accidents.


## Team

### William

William will take the lead on the technical aspects of the project. His primary responsibilities include developing Python scripts for data extraction and integration, implementing data cleaning procedures, and building the automated workflow. William will also manage the GitHub repository and ensure that code is properly documented and reproducible at all steps of the project. In addition, William will handle submissions to Canvas and GitHub for project deadlines. While his primary focus will be technical and coding tasks, he will also contribute to the written components of the project and participate in analysis discussions whenever necessary/possible. 

### Enrique

Enrique will take the lead on the written and analytical components of the project. His responsibilities include drafting sections of the project documentation such as the project plan, status report, and final report, as well as interpreting results. These responsibilities are not fully on Enrique and will be shared with William as well, with Enrique taking the main lead. Enrique will also focus on documenting the data lifecycle, metadata, ethical considerations, and data quality assessments. Additionally, Enrique will help coordinate the project timeline by ensuring the team stays on track with deadlines. Enrique will also contribute to coding tasks when needed and collaborate on reviewing the technical workflow. 



## Research/Business Question

This project focuses on understanding how driver behavior and vehicle maneuvers relate to traffic crashes in Chicago. The main research question for this project is: 

***What vehicle maneuvers are most commonly associated with traffic crashes in Chicago?***

To support this main question, we will explore several related questions such as: 

-Which vehicle maneuvers appear most frequently in reported crashes?

-Are certain vehicle maneuvers associated with more severe crashes or injuries?

-Do crashes involving multiple vehicles happen more often during specific maneuvers such as turning or lane changes?
-What types of vehicles are most commonly involved in crashes?

By exploring these questions, we hope to better understand how different driving behaviors contribute to traffic crashes.

## DataSets

This project will use two datasets from the Chicago Open Data Portal. These datasets are publicly available and maintained by the City of Chicago.

### Dataset 1: Traffic Crashes – Crashes (https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes)
This dataset contains information about each traffic crash that occurs within the city limits of Chicago. The data is reported by the Chicago Police Department and collected through the electronic crash reporting system. Each record represents a single crash event and includes information such as crash date and time, location, weather conditions, road conditions, and crash severity. Personally identifiable information has been removed from the dataset to protect privacy.

### Dataset 2: Traffic Crashes – Vehicles
https://data.cityofchicago.org/Transportation/Traffic-Crashes-Vehicles
This dataset contains information about the vehicles or units involved in each crash. A unit can include a vehicle, bicycle, pedestrian, or other mode of transportation involved in the incident. The dataset includes information such as vehicle type, vehicle maneuver, and damage location.

These datasets can be connected using the shared field CRASH_RECORD_ID, which uniquely identifies each crash. By merging the two datasets together, we will be able to analyze crash conditions alongside the vehicle maneuvers and vehicle types involved in the incident.

## Timeline
The project will be completed over several stages throughout the semester. Both team members will collaborate on most stages of the project while also contributing to their specific responsibilities.

Week 1 – Project Planning
 Finalize the project topic, identify datasets, and complete the project plan. Submit the project plan through GitHub and Canvas.

Week 2 – Data Acquisition and Exploration
 Download the selected datasets from the Chicago Open Data Portal and explore the data structure. Identify important variables such as vehicle maneuver, crash severity, and vehicle type. Begin reviewing data quality issues.

Week 3 – Data Cleaning
 Clean the datasets by checking for missing values, inconsistent formats, or duplicate records. Standardize date and time formats and ensure that identifiers match between datasets.

Week 4 – Data Integration
 Merge the crash dataset and vehicle dataset using the shared field CRASH_RECORD_ID. Verify that the integration correctly links vehicle information with the crash records.

Week 5 – Data Analysis
 Analyze patterns in vehicle maneuvers and crash characteristics. Identify which maneuvers appear most often in crashes and examine whether certain maneuvers are linked to more severe crashes or injuries.

Week 6 – Visualization and Interpretation
 Create charts and visualizations to help interpret the patterns found in the data. Discuss the findings and evaluate what the results suggest about driving behavior and crash patterns.

Week 7 – Final Report and Documentation
 Prepare the final project report and ensure that all code, data, and documentation are organized and available in the GitHub repository.

## Constraints
We noticed several limitations that we might face with the datasets used in this project.
First, the crash data is based on police reports and self-reported crash incidents. Because of this, some details about crashes such as vehicle maneuvers or crash conditions may depend on the observations of the responding officer or the statements from drivers involved in the crash.
Second, certain identifying fields such as police report numbers and badge numbers have been removed from the dataset for privacy reasons. While this helps protect personal information, it may limit the ability to cross-reference crash records with other data sources.
Another limitation is that not every traffic crash is reported to the police, especially minor incidents. As a result, the dataset may not represent every crash that occurs in the City of Chicago.
Finally, some variables such as weather conditions or road conditions are based on officer observations at the time of the crash and may not always perfectly reflect the actual conditions.

## Gaps
Although the datasets provide detailed information about traffic crashes and the vehicles involved, there are still some gaps that may affect the analysis.
For example, the datasets may not capture all factors that contribute to crashes such as driver distraction, driver fatigue, or road design features. These factors may influence crashes but are not directly included in the available datasets.
Another gap is that vehicle maneuvers are recorded based on reports from officers or drivers, which may sometimes be incomplete or interpreted differently across crash reports.
Additionally, the dataset focuses only on crashes that occur within the City of Chicago and under the jurisdiction of the Chicago Police Department. Crashes occurring on interstate highways or outside the city may not be included.
If necessary, additional datasets such as weather data or traffic congestion data may be explored later in the project to provide more context for the analysis.

