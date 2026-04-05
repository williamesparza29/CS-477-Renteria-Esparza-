## Satus Report

## Project Progress Overview  

Since completing our initial project plan, we have made strong progress in data acquisition, cleaning, and integration. The main goal of this phase was to build a clean and structured dataset that we can use to perform meaningful and creative analysis of traffic crashes in Chicago.

We successfully retrieved two large datasets from the City of Chicago: a crash dataset and a vehicle dataset. Due to the size of these datasets, we implemented a chunk-based data retrieval method to download the data in segments instead of all at once. This approach allowed us to handle over 100,000 rows efficiently without running into memory or performance issues.

The data acquisition and preprocessing pipeline is implemented in our script:
- `ProjectScript.py` :contentReference[oaicite:0]{index=0}  

We also created a structured data storage system by separating raw data and processed data into different folders. This ensures reproducibility, allows us to track how the data evolves, and provides a fallback in case errors occur during processing.

After acquiring the data, we performed attribute selection to focus only on relevant variables. The datasets initially contained a large number of features, but many of them were not useful for our analysis or would have made the process unnecessarily complex. We retained variables related to crash type, causes, environmental conditions, and vehicle maneuvers, while removing unnecessary columns.

Next, we merged the crash and vehicle datasets using the shared identifier `crash_record_id`. This merge created a one-to-many relationship, since a single crash can involve multiple vehicles. As a result, we structured the dataset at the vehicle level, allowing us to better analyze driver behavior and actions such as maneuver type.

We then continued cleaning and standardizing the data. This included standardizing text values (uppercase and whitespace removal), handling missing values by replacing them with “UNKNOWN,” grouping similar categories such as distraction and impairment, and converting numeric columns into appropriate data types.

Additionally, we created a secondary dataset (`analysis_df`) that excludes rows with unknown maneuver values. This allows for more precise and focused analysis when needed.

---

## Task Updates  

Below is an update on each task outlined in our original project plan:

### 1. Data Acquisition — **Completed**  
We successfully retrieved crash and vehicle datasets using API endpoints. Because of the dataset size, we implemented chunking to download the data in batches. This significantly improved efficiency and allowed us to work with the data locally.

Artifacts:
- `ProjectScript.py`
- Raw datasets in `/Data/raw/`

---

### 2. Data Cleaning — **Completed (Initial Phase)**  
We performed initial data cleaning by selecting relevant variables, standardizing categorical values, handling missing data, and converting data types. We also fixed inconsistencies such as mixed casing and formatting issues across columns.

Artifacts:
- Processed datasets in `/Data/processed/`
- Cleaning logic in `ProjectScript.py`

---

### 3. Data Integration — **Completed**  
We merged the crash and vehicle datasets using `crash_record_id`. This allowed us to combine environmental context from crashes with behavioral information from vehicles into a single dataset.

Artifacts:
- `merged_2024.csv` in `/Data/processed/`

---

### 4. Feature Engineering — **Completed (Initial Phase)**  
We created new grouped variables for contributory causes, such as DISTRACTION, TRAFFIC_VIOLATION, and IMPAIRMENT. This reduced complexity and made the data easier to analyze.

We also created a filtered dataset (`analysis_df`) that removes unknown maneuver values to improve analysis quality.

Artifacts:
- `analysis_df.csv` in `/Data/processed/`

---

### 5. Exploratory Data Analysis — **In Progress**  
We have started exploring distributions of key variables, including maneuver types and crash causes. This initial exploration is helping us understand patterns in the data and guide our next steps.

---

### 6. Visualization — **Not Started**  
We plan to create visualizations such as bar charts of crash causes, comparisons between maneuvers and crash types, and breakdowns of environmental conditions.

---

### 7. Final Report — **Not Started**  
The final report will summarize insights and conclusions drawn from our analysis.

---

## Updated Timeline  

| Task | Status | Updated Completion |
|------|--------|-------------------|
| Data Acquisition | Completed | Done |
| Data Cleaning | Completed (Initial) | Done |
| Data Integration | Completed | Done |
| Feature Engineering | Completed (Initial) | Done |
| Exploratory Analysis | In Progress | Next phase |
| Visualization | Not Started | Upcoming |
| Final Report | Not Started | Final phase |

---

## Changes to Project Plan  

Based on our progress so far, we made several adjustments to our original project plan.

First, we decided to focus only on 2024 data to ensure completeness and consistency, since more recent data may still be updated. This allows us to work with a stable dataset.

Second, we shifted our analysis to the vehicle level instead of the crash level. This change allows us to better capture driver behavior, particularly maneuvers and actions taken during crashes.

Third, we created multiple versions of the dataset, including a full dataset and a filtered dataset that excludes unknown maneuvers. This gives us flexibility depending on the type of analysis we want to perform.

Finally, we introduced category grouping for contributory causes to simplify the dataset and improve interpretability.

---

## Challenges and Solutions  

During this phase, we encountered several challenges.

One major challenge was the size of the dataset. Loading the full dataset at once caused performance issues, so we implemented a chunk-based retrieval method to download the data in manageable portions.

Another challenge was the presence of missing and “UNKNOWN” values, especially in key variables like maneuver and contributory causes. We addressed this by standardizing missing values and also creating a filtered dataset that excludes unknown maneuvers.

We also encountered inconsistencies in categorical variables, such as differences in casing and formatting. This was resolved by standardizing all text fields to uppercase and removing whitespace.

Additionally, the contributory cause variable contained too many categories, making analysis difficult. To address this, we grouped similar causes into broader categories such as distraction, impairment, and traffic violations.

Finally, some variables, such as speed limit and speeding indicators, appeared unreliable or incomplete. We plan to further evaluate whether these variables should be excluded or handled differently in future analysis.

---

## Team Member Contributions  

### William
- Developed the data acquisition pipeline  
- Implemented chunking for large datasets  
- Performed dataset merging and cleaning  
- Documented preprocessing steps in code  

### Enrique
- Wrote and structured the status report  
- Translated technical work into clear documentation  
- Updated the project plan based on progress  
- Ensured alignment with assignment requirements  


---

## Summary  

At this stage, we have successfully completed data acquisition, cleaning, and integration. We now have a structured and analysis-ready dataset that combines both crash-level and vehicle-level information.

Moving forward, we will focus on exploratory data analysis, visualization, and generating insights to answer our research questions. Despite challenges, we were able to resolve key issues and maintain strong progress throughout this milestone.

Overall, the project is on track and well-prepared for the next phase.
