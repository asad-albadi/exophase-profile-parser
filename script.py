import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
# The URL of the page you want to fetch
url = "https://www.exophase.com/user/deava/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the element with class "list-unordered-base row gx-0 overview"
    list_element = soup.find('ul', class_='list-unordered-base row gx-0 overview')

    # Check if the element was found
    if list_element:
        # Extract the list items (represented as <li> elements) from the list
        list_items = list_element.find_all('li')

        data_list = []
        for item in list_items:
            try:
                     # Parse the sample HTML
                soup = BeautifulSoup(str(item), 'html.parser')

                # Extract data from the sample item
                data = {}

                # Extract game name
                game_name = soup.find('h3').get_text(strip=True)
                data['game_name'] = game_name

                # Extract image URL
                image_url = soup.find('img')['src']
                #data['image_url'] = image_url
                
                # Extract image URL
                image_url = soup.find('div', class_='platforms').get_text(strip=True)
                data['platform'] = image_url


                # Extract playtime (e.g., 1.28h)
                playtime = soup.find('span', class_='hours').get_text(strip=True)
                data['playtime'] = playtime

                # Extract last played date
                last_played = soup.find('div', class_='lastplayed').get_text(strip=True)
                data['last_played'] = last_played
                data_list.append(data)
            except:
                continue
        df = pd.DataFrame(data_list)
    else:
        print("Element with class 'list-unordered-base row gx-0 overview' not found on the page.")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Convert 'last_played' column to datetime format
df['last_played'] = pd.to_datetime(df['last_played'])

# Calculate the date one month ago from the current date
last_month = datetime.now() - timedelta(days=7)

# Filter the DataFrame for games played in the last month
filtered_df = df[df['last_played'] >= last_month]

# Sort the filtered DataFrame by 'playtime' in descending order
filtered_df['playtime'] = filtered_df['playtime'].str.rstrip('h').astype(float)
top_4_played_games = filtered_df.sort_values(by='playtime', ascending=False).head(4)

# Reset the index if needed
top_4_played_games = top_4_played_games.reset_index(drop=True)

print(top_4_played_games)
