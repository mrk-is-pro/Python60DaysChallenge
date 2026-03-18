# Day 7: Smart Campus Energy Analyzer

This program is designed to analyze energy usage in a smart campus. It takes a number of energy readings as input, where each reading represents the energy consumed by a building. The readings are stored in a list and processed using loops and conditions.

Each energy value is checked and classified into one of four categories: efficient, moderate, high consumption, or invalid. A dictionary is used to store these categorized readings. Any invalid values (less than 0) are separated so that they do not affect further calculations.

The program then uses list comprehension to filter only valid readings and calculates the total energy consumption and the number of buildings. This information is stored using a tuple for easy access.

Based on different conditions, such as total energy usage, number of high consumption readings, and the balance between efficient and moderate readings, the program determines the overall energy status of the campus. The final result is displayed as Efficient Campus, Moderate Usage, or Energy Waste Detected.

A small personalization is also included using the length of the name. If the name length is even, the program displays the number of invalid entries; otherwise, it shows the number of high consumption readings.

Overall, this task helped in understanding how to work with lists, dictionaries, and tuples, and how to apply loops, conditions, and list comprehension to solve a real-world problem in a simple way.