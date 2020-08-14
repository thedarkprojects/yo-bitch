
import argparse
import requests
import traceback
import os
from bs4 import BeautifulSoup
from tqdm import tqdm
from multiprocessing.dummy import Pool as ThreadPool
import itertools

global_download_path = "C:/Users/azeez/Videos/SIMPSONS/S28" #None

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def accept_cli_input(prefix = "", to_lower=True):
    entry = input(prefix + "$> ")
    if to_lower:
        entry = entry.lower().strip()
    if entry == "exit":
        exit()
    return entry
    
def download_episode(episode):
    global global_download_path
    if global_download_path is None:
        global_download_path = accept_cli_input("Enter the folder to download the video into ", False)
        if not os.path.isdir("/home/el"):
            print("The folder '" + global_download_path + "' does not exists")
            global_download_path = None
            download_episode(episode)
            return None
    
    try:
        session = requests.Session()
        page = session.get(episode['link'])
        soup = BeautifulSoup(page.content, 'html.parser')
        link = soup.find('a', text="A higher quality version (MP4)")
        if link is None:
            link = soup.find('a', text="A higher quality version (WEBM)")
        if link is None:
            link = soup.find('a', text="Click here for the download page")
        if link is None:
            print("Error Cannot Download '" + episode['name'] + "' ")
            return
        link = link['href']
        if not link.startswith("http"):
            link = "https://www.mobiletvshows.net/" + link
        page = session.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')
        link = soup.find('a', text="Download Link 2")
        
        name = os.path.basename(link['href'])
        response = requests.get(link['href'], stream=True)
        with open(global_download_path + "/" + name, "wb") as handle:
            for data in tqdm(response.iter_content(chunk_size=3072), desc="Downloading '" + name + "' "):
                handle.write(data)
    except Exception as e:
        print("Error Cannot Download '" + episode['name'] + "' ")
        traceback.print_exc()
    
def download_episodes(episodes_list):
    pool = ThreadPool(5)
    results = pool.starmap(download_episode, zip(episodes_list))
    pool.close()
    pool.join()
    
def scrap_season_page(scrap_url, back_link = None, super_bl = None):
    cls()
    episodes_list = [ {"padding"} ]
    page = requests.get(scrap_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.title.string)
    seasons = soup.find_all(class_='mainbox')
    index = 1
    for season in seasons:
        link = season.find('a')
        if link is None:
            continue
        url = link['href']
        if not url.startswith("http"):
            url = "https://www.mobiletvshows.net/" + url
        title = link.find('div')['id']
        print("[" + str(index) + "] " + title)
        episodes_list.append({
            "link": url,
            "name": title
        })
        index = index + 1
    
    if index == 0:
        return
        
    if back_link is not None:
        print("[B]ack   ", end='')
        
    next = soup.find_all('a', text="Next")
    if len(next) != 0:
        next = next[0]['href']
        print("[N]ext Page  ", end='')
        
    prev = soup.find_all('a', text="Prev")
    if len(prev) != 0:
        prev = prev[0]['href']
        print("[P]revious Page", end='')
        
    print()
       
    print("This page appears to have " + str(len(episodes_list) - 1) + " downloadable episodes")
    print("[A]ll episodes should be downloaded (yes)?")
    entry = accept_cli_input()
    if (entry == "n" or entry == "next" or entry == "next page") and isinstance(next, str):
        scrap_season_page(next, back_link, super_b)
    elif (entry == "p" or entry == "prev" or entry == "previous" or entry == "prev page") and isinstance(prev, str):
        scrap_season_page(prev, back_link, super_b)
    elif (entry == "b" or entry == "back"):
        scrap_series_page(back_link, super_bl)
    elif (entry == "a" or entry == "yes"):
        episodes_list.pop(0)
        download_episodes(episodes_list)
    else:
        try:
            index_value = int(entry)
            download_episode(episodes_list[index_value])
        except ValueError as e:
            print("Unknown input: " + entry)
    
def scrap_series_page(scrap_url, back_link = None):
    cls()
    seasons_list = ["padding"]
    page = requests.get(scrap_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.title.string)
    seasons = soup.find_all(class_='mainbox3')
    index = 1
    for season in seasons:
        link = season.find('a')
        if link is None:
            continue
        url = link['href']
        if not url.startswith("http"):
            url = "https://www.mobiletvshows.net/" + url
        print("[" + str(index) + "] " + link.text.strip())
        seasons_list.append(url)
        index = index + 1
    
    if index == 0:
        return
        
    if back_link is not None:
        print("[B]ack   ", end='')
        
    next = soup.find_all('a', text="Next")
    if len(next) != 0:
        next = next[0]['href']
        print("[N]ext Page  ", end='')
        
    prev = soup.find_all('a', text="Prev")
    if len(prev) != 0:
        prev = prev[0]['href']
        print("[P]revious Page", end='')
        
    print()
    entry = accept_cli_input()
    if (entry == "n" or entry == "next" or entry == "next page") and isinstance(next, str):
        scrap_series_page(next, back_link)
    elif (entry == "p" or entry == "prev" or entry == "previous" or entry == "prev page") and isinstance(prev, str):
        scrap_series_page(prev, back_link)
    elif (entry == "b" or entry == "back"):
        scrap_series_list_page(back_link)
    else:
        try:
            index_value = int(entry)
            scrap_season_page(seasons_list[index_value], scrap_url, back_link)
        except ValueError as e:
            print("Unknown input: " + entry)

def scrap_series_list_page(scrap_url):
    cls()
    series_list = ["padding"]
    page = requests.get(scrap_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    series = soup.find_all(class_='mainbox')
    index = 1
    for seres in series:
        link = seres.find('a')
        if link is None:
            continue
        url = link['href']
        if not url.startswith("http"):
            url = "https://www.mobiletvshows.net/" + url   
        title = link.find('div')['id']
        print("[" + str(index) + "] " + title)
        series_list.append(url)
        index = index + 1
    
    if index == 0:
        return
        
    next = soup.find_all('a', text="Next")
    if len(next) != 0:
        next = next[0]['href']
        print("[N]ext Page", end='')
        
    prev = soup.find_all('a', text="Prev")
    if len(prev) != 0:
        prev = prev[0]['href']
        print(" [P]revious Page", end='')
        
    print()
    entry = accept_cli_input().lower().strip()
    if (entry == "n" or entry == "next" or entry == "next page") and isinstance(next, str):
        scrap_series_list_page(next)
    elif (entry == "p" or entry == "prev" or entry == "previous" or entry == "prev page") and isinstance(prev, str):
        scrap_series_list_page(prev)
    else:
        try:
            index_value = int(entry)
            scrap_series_page(series_list[index_value], scrap_url)
        except ValueError as e:
            print("Unknown input: " + entry)

def enter_shell():
    print("Search and download like\nyo-bitch find simpson\nyo-bitch -h to view the possible commands")

def main():
    parser = argparse.ArgumentParser(description='Search and Download series from https://www.mobiletvshows.net/ from cli. ')
    parser.add_argument('--find', type=str, nargs='?',
                    help='Find a series on mobiletvshows')
    parser.add_argument('--series', type=str, nargs='?',
                    help='Visit a series page scrap the list of seasons in it')
    parser.add_argument('--season', type=str, nargs='?',
                    help='Visit a series season page scrap the list of episodes in it')
    parser.add_argument('--visit', type=str, nargs='?',
                    help='Visit a page from mobiletvshows and scrap the series and episodes in it')
                    
    args = parser.parse_args()
    if args.find:
        scrap_series_list_page("https://www.mobiletvshows.net/search.php?search=" + args.find)
    elif args.series:
        scrap_series_page(args.series)
    elif args.season:
        scrap_season_page(args.season)
    elif args.visit:
        print("We should visit " + args.visit)
    else:
        enter_shell()

if __name__ == '__main__':
    main()