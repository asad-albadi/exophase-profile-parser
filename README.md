# Exophase Web Scraping Project

![Exophase Logo](exophase-logo.png)

This Python project demonstrates web scraping using the BeautifulSoup library to extract and analyze data from Exophase user profiles. Exophase is a platform that tracks gaming achievements and playtime.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [How it Works](#how-it-works)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

Exophase Web Scraping Project fetches data from Exophase user profiles and provides insights into the games a user has played in the last month, including playtime and last played dates.

## Requirements

Before running the project, make sure you have the following Python libraries installed:

- `requests`
- `beautifulsoup4`
- `pandas`

You can install them using pip:

```bash
pip install requests beautifulsoup4 pandas
```

## Usage

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/exophase-web-scraping.git
```

2. Change the directory to the project folder:

```bash
cd exophase-web-scraping
```

3. Run the Python script:

```bash
python web_scraping.py
```

4. The script will prompt you to enter the Exophase user profile URL to scrape data from.

5. The script will fetch data from the specified URL and display the top 4 most played games in the last month.

## How it Works

- The script sends an HTTP GET request to the Exophase user profile page.
- It parses the HTML content of the page using BeautifulSoup.
- It extracts game names, platform information, playtime, and last played dates from the page.
- The data is stored in a Pandas DataFrame.
- The script filters the DataFrame to display games played in the last month and sorts them by playtime.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Exophase](https://www.exophase.com/) for providing the data used in this project.
- The creators of the [requests](https://docs.python-requests.org/en/latest/) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) libraries for making web scraping easier.
- The [Pandas](https://pandas.pydata.org/) library for data manipulation and analysis.

