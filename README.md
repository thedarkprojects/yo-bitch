
# yo-bitch
Search and Download series from https://www.mobiletvshows.net/ from cli.

## Installation

Download python from https://www.python.org/downloads/

Install the required dependencies with 

```python
pip install -r requirements.txt
```

## Run the script

On windows the `yo-bitch.bat` can be used to execute the yo-bitch.py script natively, on unix 
the `yo-bitch.sh` can be used but ensure you set the yo-bitch.sh to executable on unix system

#### See the list of commands

```bash
yo-bitch help
```

#### Find and Download a series 

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

## Note

Enter `exit` at anytime in the program prompt to end the program

