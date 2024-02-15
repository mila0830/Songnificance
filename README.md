# Songnificance

### Project made for McWics Hackathon 2024

## Inspiration
Our project delves into a fascinating aspect of music culture: the widespread enjoyment of songs irrespective of language barriers. We're exploring how people groove to tunes, often unaware of the deep lyrical meanings, particularly in foreign languages, especially with McGill being such a diverse community. It's intriguing how these seemingly happy melodies or remixes conceal profound messages, and we're here to unravel those hidden depths.

## What Songnifiance Does
In our project, we ask the user to input the title and the singer of a song and we provide a concise summary of its true meaning. By uncovering the underlying messages within the music, we aim to offer insight into the profound themes and emotions expressed by artists across different languages and genres from all different time periods.

## How We Built It
We built our project using the Spotify API for song data, Genius API for lyric data, OpenAI API for summarization and Python for the backend. We implemented two routes depending on the song's release date: for songs released before 2022, we sent the song title and artist directly to the OpenAI API to retrieve its meaning. However, for more recent songs, we used the Genius API to get the lyrics and then used the OpenAI API to derive the meaning from the lyrics. This was all programmed in Python. For the frontend, we used the React framework alongside JavaScript, CSS and HTML to create a user-friendly interface where users can input song titles and their artists and get back summaries.

## Challenges We Ran Into
One of the main challenges we encountered was with the frontend development, as neither of us had much prior experience with JavaScript. This led to various issues and hurdles in implementing the user interface and functionality. We had to spend extra time learning JavaScript and troubleshooting errors along the way.  The Spotify API is also quite difficult to use, so we spent a lot of time learning how to use it and how it worked. Lastly, all the APIs, we used cost money so we had to limit usage. However, through perseverance and collaboration, we were able to overcome these obstacles and successfully complete the frontend portion of the project.

## Accomplishments 
We are proud of our ability to translate abstract ideas into tangible projects. Despite encountering challenges, particularly with our unfamiliarity with JavaScript for the frontend and all the APIs we used, we were able to pull through our complete project. Through perseverance and collaborative effort, we navigated these obstacles and successfully completed the frontend portion of our project.


## What We Would Do If We Had More TIme
We were thinking about several things :
1. Develop it with over platforms such as Deezer for example.
2. Improve the website by adding the image of the album of the song every time we display the summary.
3. Implement more prompt engineering and use more LangChain functionalities to limit excessive token usage.
4. More general error handling in the backend.


## Pacakages/Items Required
* pip install python-dotenv
* pip install requests 
* must use your own API keys in the .env file (OpenAI, Genius, and Spotify Application)
