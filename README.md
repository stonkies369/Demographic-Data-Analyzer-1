# Demographic Data Analyzer

This project is part of the [freeCodeCamp Data Analysis with Python Certification](https://www.freecodecamp.org/learn/data-analysis-with-python/). It uses the 1994 Census database to analyze demographic data using Python and Pandas.

## Table of Contents
- [Overview](#overview)
- [Questions Answered](#questions-answered)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Testing](#testing)
- [License](#license)

## Overview

The Demographic Data Analyzer answers key demographic questions about a dataset extracted from the 1994 U.S. Census database. The analysis is performed using the Pandas library. The goal is to process the data to answer various questions about demographics and salaries.

## Questions Answered

The following questions are answered by the `calculate_demographic_data` function in the project:

1. **How many people of each race are represented in this dataset?**
   - This is answered using the `race_count` variable, which counts how many people of each race are present in the dataset.

2. **What is the average age of men?**
   - The `average_age_men` variable calculates the average age of men in the dataset.

3. **What is the percentage of people who have a Bachelor's degree?**
   - The percentage of people with a Bachelor's degree is computed and stored in the `percentage_bachelors` variable.

4. **What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than $50K?**
   - The `higher_education_rich` variable calculates the percentage of people with advanced education who earn more than $50K.

5. **What percentage of people without advanced education make more than $50K?**
   - The `lower_education_rich` variable calculates the percentage of people without advanced education who earn more than $50K.

6. **What is the minimum number of hours a person works per week?**
   - The `min_work_hours` variable calculates the minimum number of hours a person works per week, which is retrieved from the `hours-per-week` column.

7. **What percentage of the people who work the minimum number of hours per week have a salary of >50K?**
   - The `rich_percentage` variable calculates the percentage of people who work the minimum number of hours and earn more than $50K.

8. **What country has the highest percentage of people that earn >50K?**
   - The `highest_earning_country` and `highest_earning_country_percentage` variables provide the country with the highest percentage of people who earn more than $50K.

9. **Identify the most popular occupation for those who earn >50K in India.**
   - The `top_IN_occupation` variable gives the most popular occupation in India for people who earn more than $50K.

## Technologies Used

- **Python**: Programming language used for the analysis.
- **Pandas**: Data manipulation library used to process and analyze the dataset.
- **Gitpod**: Development environment used to write and test the code.

## Setup

1. **Clone this repository**:
   - Navigate to your desired directory and clone the repository by running:
   ```bash
   git clone https://github.com/<your-username>/boilerplate-demographic-data-analyzer.git



