# Day 10: Predictive Data Replication & Corruption Analyzer

## Overview
This project simulates a large-scale system where data is replicated across multiple zones for analysis. It demonstrates how improper copying can lead to hidden data corruption and affect system predictions.

## Data Structure
- List of dictionaries
- Each zone contains:
  - `zone` (int)
  - `metrics` → traffic, pollution, energy
  - `history` → list of past values

## Implementation
- Generated random data for 15 zones
- Created:
  - Assignment copy
  - Shallow copy
  - Deep copy
- Applied multi-level modifications:
  - Updated nested metric values
  - Appended values to history
  - Calculated risk using a custom log-based formula

## Data Analysis
- Converted data into a Pandas DataFrame
- Used NumPy for:
  - Mean
  - Variance
- Manually calculated correlation (without using `.corr()`)

## Pattern Detection
- Detected anomaly zones (values beyond mean + standard deviation)
- Identified high-risk zones using custom risk score
- Detected clusters of consecutive risky zones
- Calculated stability index based on variance

## Personalization
- Register number logic:
  - Even → reverse dataset
  - Odd → rotate dataset
- Custom risk score modified using name length
- Output message varies slightly based on name length

## Output
- Displays:
  - DataFrame (sample view)
  - Before vs After comparison
  - Anomaly zones
  - Risk tuple → (max_risk, min_risk, stability_index)
  - Final system decision:
    - System Stable
    - Moderate Risk
    - High Corruption Risk
    - Critical Failure

## Learning Outcome
This project helped in understanding how shallow and deep copy behave differently in nested structures. It also showed how improper copying can cause hidden corruption and affect analysis. Additionally, it improved skills in NumPy, Pandas, and manual statistical computation.