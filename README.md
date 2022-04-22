# SC1015proj

## SCSE 21/22 Semester 2

### SC1015 Mini Project created by Valencino Tan, Tan Jing Han & Ronald Tan


**Navigation**

  - [Twitch_SERIOUS.ipynb - Codes with Exploratory Data Analysis & Machine Learning Models](https://github.com/whysilon/SC1015proj/edit/main/README.md#our-jupyter-notebook)

  - [test_data2.csv - Data collected from Twitch API](https://github.com/whysilon/SC1015proj/edit/main/README.md#our-data)

  - [new_scraper.py - Python code used to scrape data from Twitch](https://github.com/whysilon/SC1015proj/edit/main/README.md#our-data-scraper)

## Our data scraper

Thanks to the [Twitch API for python](https://github.com/Teekeks/pyTwitchAPI), we were able to code a script to scrape data from Twitch in order to start our data analysis. Initially, [our first scraper](./twitch_api.py) used to only scrape top 100 streams which was not meaningful as it does not help the lower less established streamers based on our problem that we formulated. We then decided to design another script to scrape data from the top 100 streams every 25 pages of stream which also did not work as the data became too skewed to the streamers with low view count. Hence, [our new scraper](./new_scraper.py) samples the top 25 streams of each page up to first 100 pages. This is able to give us a sample of the first 100 pages of streams which thus allows us to see a fuller picture as compared to the previous scrapers

## Our data

The data that are useful in the scraped data are as follows:

| Variables | Description |
| --- | --- |
| viewer_count | The no. of active viewers at the time we scraped data |
| total_views | Total views of all videos on channel, including after the stream has ended |
| follow_count | Number of followers for the particular channel|
| is_mature | Whether the stream is mature or not |
| Tags | Descriptors to classify streams (?) |
| Language | Language of the stream |
| game_name | Name of the game that the channel is streaming |
| Title | Title of the stream |

## Our Jupyter Notebook



