
# yo-bitch
Search and Download series from https://www.mobiletvshows.net/ from cli.

[![Watch the video](https://repository-images.githubusercontent.com/287421797/01cf0e80-ddfe-11ea-98b8-afd5659259ae)](https://github.com/thedarkprojects/yo-bitch/blob/main/demo.mp4)

```bash
usage: yo-bitch.py [-h] [--find [FIND]] [--series [SERIES]] [--season [SEASON]]

Search and Download series from https://www.mobiletvshows.net/ from cli. example: yo-bitch --find simpson

optional arguments:
  -h, --help         show this help message and exit
  --find [FIND]      Find a series on mobiletvshows
  --series [SERIES]  Visit a series page scrap the list of seasons in it
  --season [SEASON]  Visit a series season page scrap the list of episodes in it
```

## Installation

Clone the repo or download the repo whichever way.

Download python from https://www.python.org/downloads/

Install the required dependencies with 

```python
pip install -r requirements.txt
```

## Run the script

On windows the `yo-bitch.bat` can be used to execute the yo-bitch.py script natively, on unix 
the `yo-bitch.sh` can be used but ensure you set the yo-bitch.sh to executable on unix system

### See the list of commands

```bash
yo-bitch help
```

### Find and Download a series 

It will list all the series returned by the query, type the corresponding index number of the series to select it, for example to downlad the simpsons season 29:

```bash
yo-bitch --find simpsons

[1] The Simpsons
[2] The Barrys
[N]ext Page  [P]revious Page
$> 1

The Simpsons
[1] Season 1
[2] Season 2
[x] Season x
[28] Season 28
$> 28

The Simpsons - Season 28 
This page appears to have 21 downloadable episodes do you 
want to download the episodes? 
[Y]es   [N]o
$> Yes
Enter the folder you want to download the episodes into $> C:/your/folde/videos/simpsons/S28/
Downloading the episodes, 
Done 21 episodes downloaded
```

### Visit a series page directly

Visit a series page directly without the need to search for it usin the `--series` flag 

```bash
yo-bitch --series https://www.mobiletvshows.net/subfolder-The%20Simpsons.htm

The Simpsons - MobileTvShows
[1] Season 1
[2] Season 2
[X] Season X
[30] Season 30

$>
```

### Visit a Season directly

Visit a series season page to list it episode and download a single episode or download all the episodes at once

```bash
yo-bitch --season https://www.mobiletvshows.net/files-The%20Simpsons--6668.htm

The Simpsons TV series, shows/cartoon,anime,magma/Documentaries - MobileTVshows
[1] The Simpsons - S28E01 - Monty Burns
[2] The Simpsons - S28E02 - Friends and Family
[X] The Simpsons - S28E03 - The Town
[22] The Simpsons - S28E22 - Dogtown

This page appears to have 22 downloadable episodes
[A]ll episodes should be downloaded (yes)?
$>
```

type `A` and press enter to download all the episode you will be propmt to enter the folder to download the videos into, or type the episode index to download a single episode e.g `1` to  download only the episode `The Simpsons - S28E01 - Monty Burns`.

## Note

Enter `exit` at anytime in the program prompt to end the program

# Disclamer

This project is licence with `The Unlicenced` whatever you use this script for is not a concern of the author or any contributor to the project or thedarkproject organization. 

The user is liable for any charges that might arise downloading pirated copy of series.

This script is not guaranteed to work as you expected, Issues raised in this repository will not be on the author or contributors priority. 
