# SC1015 SCSE 21/22 Semester 2 Mini-Project

## About

This is a SC1015 mini project which focuses on Twitch, a game streaming platform for everyone.

**Navigation**

To understand the project in-depth, you may want to look at the source code as linked below: 
  - [twitch_api_final_script.py - Python code used to scrape data from Twitch](https://github.com/whysilon/SC1015proj/edit/main/README.md#our-data-scraper)
  - [test_data2.csv - Data collected from Twitch API](https://github.com/whysilon/SC1015proj/edit/main/README.md#our-data)
  - [Twitch_SERIOUS.ipynb - Codes with Exploratory Data Analysis & Machine Learning Models](https://github.com/whysilon/SC1015proj/edit/main/README.md#our-jupyter-notebook)

## Contributors
  - @harpervin - Tan Jing Han --> Created our python scraper + did the basic exploration of the data
  - @MoriyaHiroshi - Ronald Tan --> Did the presentation logistics
  - @whysilon - Valencino Tan --> Created the relevant machine learning models

## Problem Definition
What can help increase Twitch viewership?

## Models Used
  - Linear Regression
  - Decision Tree Classifier
  - Random Forest

## Conclusion
  - Relationship of the numeric data is not strong. 
  - Most of the data points congregate towards the lower spectrum of Twitch.
  - Streaming niche games can help to bring viewership.
  - Adding emojis may help to bring incremental improvement to viewership
  - There are significant non-English speaking audiences on Twitch, reaching out to these groups could be beneficial.

## What did we learn
  - Random Forest modelling
  - API usage
  - Learning how to process titles to find emojis
  - Mean Decrease in Impurity to determine importance of features
  - Github features like this Readme and how to collaboration

## Our data scraper

Thanks to the [Twitch API for python](https://github.com/Teekeks/pyTwitchAPI), we were able to code a script to scrape data from Twitch in order to start our data analysis. Initially, [our first scraper](./data_scrapers/twitch_api.py) used to only scrape top 100 streams which was not meaningful as it does not help the lower less established streamers based on our problem that we formulated. We then decided to design another script to scrape data from the top 100 streams every 25 pages of stream which also did not work as the data became too skewed to the streamers with low view count. Hence, [our new scraper](./data_scrapers/twitch_api_final_script.py) samples the top 25 streams of each page up to first 100 pages. This is able to give us a sample of the first 100 pages of streams which thus allows us to see a fuller picture as compared to the previous scrapers

## Our data

The [data](./twitch_data/test_data2.csv) that are useful in the scraped data are as follows:

| Variables | Description |
| --- | --- |
| viewer_count | The no. of active viewers at the time we scraped data |
| total_views | Total views of all videos on channel, including after the stream has ended |
| follow_count | Number of followers for the particular channel|
| is_mature | Whether the stream is mature or not |
| Tags | Descriptors to classify streams |
| Language | Language of the stream |
| game_name | Name of the game that the channel is streaming |
| Title | Title of the stream |

## Our Jupyter Notebook
Inside our final [Jupyter Notebook](./Twitch_SERIOUS.ipynb), we have detailed our data analysis process and the conclusions that we have drawn from it. Please take a look if you are interested.

# Thank you for reading!

# References
  - https://datascience.stackexchange.com/questions/40067/confusion-matrix-three-classes-python
  - https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html
  - https://pytwitchapi.readthedocs.io/en/v2.5.3/
  - https://dev.twitch.tv/docs/api/reference/
  - https://github.com/Teekeks/pyTwitchAPI

