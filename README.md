# Tech Jobs Intelligence

System for collecting and analyzing remote tech job opportunities in the international market.

## What the project does

* Automatically collects job listings from the [Remotive](https://remotive.com) website
* Extracts job title, company, category, contract type, salary, and location
* Saves the collected data into a CSV file
* Generates charts for tech market analysis

## Technologies Used

* `requests` — accesses web pages
* `beautifulsoup4` — parses HTML content
* `fake-useragent` — simulates a real browser
* `pandas` — organizes and analyzes data
* `matplotlib` — generates charts and visualizations

## How to Run

1. Clone the repository and open it in VS Code
2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the project:

```bash
python main.py
```

## Results

The charts are automatically saved in `output/charts/`:

* `countries.png` — Top 10 countries with the most job openings
* `contracts.png` — Most common contract types
* `positions.png` — Top 10 job titles with the most openings
* `salaries.png` — Job listings with salary information available
