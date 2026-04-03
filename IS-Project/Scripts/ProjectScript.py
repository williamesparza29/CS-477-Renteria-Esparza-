#Data Aquisition

import pandas as pd
from urllib.parse import quote
import os

# Create folders
os.makedirs("../Data/raw", exist_ok=True)
os.makedirs("../Data/processed", exist_ok=True)


def fetch_all_rows(base_url, start_date, end_date, batch_size=50000):
    all_parts = []
    offset = 0

    where = (
        f"crash_date between '{start_date}T00:00:00' "
        f"and '{end_date}T23:59:59'"
    )
    encoded_where = quote(where)

    while True:
        url = (
            f"{base_url}"
            f"?$where={encoded_where}"
            f"&$limit={batch_size}"
            f"&$offset={offset}"
        )

        print(f"Downloading rows starting at offset {offset}...")
        chunk = pd.read_csv(url)

        if chunk.empty:
            break

        all_parts.append(chunk)

        if len(chunk) < batch_size:
            break

        offset += batch_size

    return pd.concat(all_parts, ignore_index=True)


# Fetch data
crashes = fetch_all_rows(
    "https://data.cityofchicago.org/resource/85ca-t3if.csv",
    "2024-01-01",
    "2024-12-31"
)

vehicles = fetch_all_rows(
    "https://data.cityofchicago.org/resource/68nd-jvt3.csv",
    "2024-01-01",
    "2024-12-31"
)

print("Crashes shape:", crashes.shape)
print("Vehicles shape:", vehicles.shape)


#raw data
crashes.to_csv("../Data/raw/crashes_2024_raw.csv", index=False)
vehicles.to_csv("../Data/raw/vehicles_2024_raw.csv", index=False)


# working copies for data cleaning
crashes_clean = crashes.copy()
vehicles_clean = vehicles.copy()


crashes_clean.to_csv("../Data/processed/crashes_2024_processed.csv", index=False)
vehicles_clean.to_csv("../Data/processed/vehicles_2024_processed.csv", index=False)

#Attribute Removal
vehicles_keep = [
    'crash_record_id',
    'unit_type',
    'vehicle_type',
    'maneuver',
    'exceed_speed_limit_i'
]

vehicles_clean = vehicles[vehicles_keep].copy()

crashes_keep = [
    'crash_record_id',
    'first_crash_type',
    'crash_type',
    'prim_contributory_cause',
    'sec_contributory_cause',
    'posted_speed_limit',
    'weather_condition',
    'lighting_condition',
    'roadway_surface_cond',
    'traffic_control_device',
    'trafficway_type',
    'num_units',
    
]
crashes_clean = crashes[crashes_keep].copy()

#Combine and Integrate Data
merged = pd.merge(
    crashes_clean,
    vehicles_clean,
    on="crash_record_id",
    how="inner"
)
#The datasets were linked using CRASH_RECORD_ID, which represents a one-to-many relationship where a single crash may involve multiple vehicles.
#Due to the one-to-many relationship between crashes and vehicles, the primary dataset is structured at the vehicle level to capture maneuver-specific behavior
merged.to_csv("../data/processed/merged_2024.csv", index=False)
#Raw Merged is converted to CSV for storage

# strip and standardize all string columns
for col in merged.select_dtypes(include="object").columns:
    merged[col] = merged[col].astype(str).str.strip().str.upper()

#Get rid of N/A / missing in Manuever, most important variable.
merged["maneuver"] = merged["maneuver"].replace("NAN", pd.NA)
merged["maneuver"] = merged["maneuver"].fillna("UNKNOWN")
merged["maneuver"] = merged["maneuver"].replace("UNKNOWN/NA", "UNKNOWN")

#reducing unable to determine and N/A to unknown, easier for analysis. 
merged["prim_contributory_cause"] = merged["prim_contributory_cause"].replace({
    "UNABLE TO DETERMINE": "UNKNOWN",
    "NOT APPLICABLE": "UNKNOWN"
}) 
merged["sec_contributory_cause"] = merged["sec_contributory_cause"].replace({
    "UNABLE TO DETERMINE": "UNKNOWN",
    "NOT APPLICABLE": "UNKNOWN"
}) 

#Grouping some similiar causes helps aid with better and cleaner analysis
def clean_cause(x):
    if pd.isna(x):
        return "UNKNOWN"
    
    if "DISTRACTION" in x or "TEXTING" in x or "CELL PHONE" in x:
        return "DISTRACTION"
    
    if "DISREGARDING" in x:
        return "TRAFFIC_VIOLATION"
    
    if "DRINK" in x or "ALCOHOL" in x or "DRUG" in x:
        return "IMPAIRMENT"
    
    return x
merged["prim_cause_cl"] = merged["prim_contributory_cause"].apply(clean_cause)
merged["secnd_cause_cl"] = merged["sec_contributory_cause"].apply(clean_cause)

#reducing unable to determine and N/A to unknown, easier for analysis. 
merged["prim_contributory_cause"] = merged["prim_contributory_cause"].replace({
    "UNABLE TO DETERMINE": "UNKNOWN",
    "NOT APPLICABLE": "UNKNOWN"
}) 
merged["sec_contributory_cause"] = merged["sec_contributory_cause"].replace({
    "UNABLE TO DETERMINE": "UNKNOWN",
    "NOT APPLICABLE": "UNKNOWN"
}) 

#cleaning for other columns, they will all get basic cleaning like as before, in case items were not cleaned correctly.

#crash types
for col in ["first_crash_type", "crash_type"]:
    merged[col] = merged[col].astype(str).str.strip().str.upper()

#speed limit - issues with this maybe fix later. Add to issues part of report. 
# many posted limits are not real/ prolyl placeholders, what should we do with this, or remove column, or leave as is. note in analysis. 
merged["posted_speed_limit"] = pd.to_numeric(
    merged["posted_speed_limit"], errors="coerce"
)

#Environmental conditions
env_cols = [
    "weather_condition",
    "lighting_condition",
    "roadway_surface_cond"
]

for col in env_cols:
    merged[col] = merged[col].astype(str).str.strip().str.upper()

#Roadways
road_cols = ["traffic_control_device", "trafficway_type"]

for col in road_cols:
    merged[col] = merged[col].astype(str).str.strip().str.upper()
#Num units
merged["num_units"] = pd.to_numeric(merged["num_units"], errors="coerce")

#vehicle info
veh_cols = ["unit_type", "vehicle_type"]

for col in veh_cols:
    merged[col] = merged[col].astype(str).str.strip().str.upper()


#speed limit - issues with this maybe fix later. Add to issues part of report. 
# many posted limits are not real/ prolyl placeholders, what should we do with this, or remove column, or leave as is. note in analysis. 
#another issue to include in phase 1. The exceed speed limit indicator has 200000+ N/A values. Should we drop both columns, as they wont be useful. 
#INCLUDE BOTH FOR ISSUES RAN INTO/ discuss how we plan to address later on. 
merged["posted_speed_limit"] = pd.to_numeric(
    merged["posted_speed_limit"], errors="coerce"
)
#replace clean cause with original
merged = merged.drop(columns=[
    "prim_contributory_cause",
    "sec_contributory_cause"
])

merged = merged.rename(columns={
    "prim_cause_cl": "primary_cause",
    "secnd_cause_cl": "secondary_cause"
})

#creating a seconadry analysis dataframe that only includes instances where manuever is not UNKNOWN.
#Another good issue to include is that exaclty, what to do when manuever is unknown, We solved by making 2 seperate tables. 
analysis_df = merged[
    (merged["maneuver"] != "UNKNOWN")
]

#curent Final Df for analysis and converted into CSV for storage purposes. 
analysis_df.to_csv("../Data/processed/analysis_df.csv", index=False)
analysis_df