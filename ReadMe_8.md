# Day 8: Autonomous Smart City Data Intelligence System

This program simulates a smart city system where each zone has data like traffic, air quality, and energy consumption. The values are generated randomly to represent different real-life scenarios.

The data is stored using a list of dictionaries and then processed step by step. Each zone is classified into categories such as high risk, energy critical, or safe based on certain conditions.

A custom risk score is calculated using traffic, air quality, and energy values. Some small changes are made to the formula to make it unique. The program also applies a mathematical transformation using the math module.

For analysis, the data is converted into a Pandas DataFrame, and NumPy is used to calculate mean values. A custom sorting logic is used to find the top 3 risky zones instead of using built-in functions.

Based on the average risk score, the program decides the overall condition of the city, such as City Stable, Moderate Risk, High Alert, or Critical Emergency.

Some personalization is included using name length and register number to slightly modify the behavior of the program.

This task helped in understanding how to simulate data, process it, and perform basic analysis using Python along with NumPy and Pandas.