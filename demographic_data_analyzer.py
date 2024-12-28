import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv', header=None, names=[
        'age', 'workclass', 'fnlwgt', 'education', 'education-num', 
        'marital-status', 'occupation', 'relationship', 'race', 
        'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 
        'native-country', 'salary'
    ])

    # Ensure all relevant columns are properly formatted
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['hours-per-week'] = pd.to_numeric(df['hours-per-week'], errors='coerce')

    # How many of each race are represented in this dataset?
    # How many of each race are represented in this dataset?
    race_order = ["White", "Black", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other"]
    race_count = df['race'].value_counts()[race_order]

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((len(df[df['education'] == 'Bachelors']) / len(df)) * 100, 1)

    # Advanced education includes Bachelors, Masters, and Doctorate
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Percentage of higher education people earning >50K
    higher_education_rich = round(
        (len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education)) * 100, 1
    )

    # Percentage of lower education people earning >50K
    lower_education_rich = round(
        (len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education)) * 100, 1
    )

    # Minimum number of hours a person works per week
    min_work_hours = df['hours-per-week'].min()

    # Percentage of people working minimum hours and earning >50K
    num_min_workers = len(df[df['hours-per-week'] == min_work_hours])
    rich_percentage = round(
        (len(df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]) / num_min_workers) * 100, 1
    )

    # Country with highest percentage of people earning >50K
    country_stats = df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()
    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = round(country_stats.max() * 100, 1)

    # Most popular occupation for those earning >50K in India
    top_IN_occupation = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
