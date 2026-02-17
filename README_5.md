# Package Weight Classification Program

## Description
This program helps classify package weights into categories: Very Light, Normal Load, Heavy Load, Overload, and Invalid Entries.
Each weight is checked using loops and conditions to ensure it falls in the correct category.  

A personalization rule based on the length of the user's name (PLI) is applied. For this program, Rule B (PLI = 1) is used, which removes all Very Light items from the final plan.
Removed items are displayed separately, along with counts of affected and valid weights, giving a clear summary of the loading plan.

## Features
- Classifies weights into appropriate categories  
- Applies personalization rule to remove Very Light items  
- Tracks and displays removed items  
- Shows total valid weights and affected items  

## Personalization Rule
- PLI = length of name % 3  
- Rule B (PLI = 1): all Very Light items are removed  
- Removed items are displayed separately for clarity  

## Learning Outcome
I learned how to take user inputs, separate values into lists, classify them using loops and conditions, and apply rules to modify lists.
It also helped me practice summarizing data clearly and managing lists in Python.
