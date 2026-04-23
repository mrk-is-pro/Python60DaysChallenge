# Day 9: Multi-Level Data Replication & Integrity Analyzer

## Overview
This program simulates how user data is replicated across servers in a cloud system. It uses a nested data structure where each user has files and usage information.

## Data Structure
- List of dictionaries
- Each user contains:
  - `id`
  - `data` → files (list) and usage (int)

## Implementation
- Created three versions of data:
  - Assignment
  - Shallow copy
  - Deep copy
- Applied modifications such as:
  - Adding or removing files
  - Updating usage values

## Integrity Analysis
- Checked if original data was affected (data leakage)
- Verified deep copy remains unchanged
- Used sets to detect overlapping files
- Compared before and after data states

## Personalization
- Register number is used to decide:
  - Even → add file
  - Odd → remove file
- Name length is used to slightly vary the output message

## Key Concepts Used
- Lists, Dictionaries, Sets
- Functions
- Shallow Copy vs Deep Copy
- Conditions and Loops

## Learning Outcome
This task helped in understanding how shallow copy and deep copy behave differently in nested structures. It also showed how improper copying can lead to data corruption and inconsistency.