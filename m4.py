import requests
import csv
import random
import concurrent.futures
from bs4 import BeautifulSoup
from time import sleep, time

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
}
MAX_THREADS = 10
BASE_URL = 'https://www.imdb.com'

def extract_movie_details(url):
    sleep(random.uniform(0, 0.2))
    soup = BeautifulSoup(requests.get(url, headers=HEADERS).content, 'html.parser')
    
    section = soup.find('section', class_='ipc-page-section')
    if not section:
        return
    
    div = section.find_all('div', recursive=False)[1] if len(section.find_all('div', recursive=False)) > 1 else None
    if not div:
        return

    title = div.find('h1').find('span').text if div.find('h1') else None
    date = div.find('a', href=lambda x: x and 'releaseinfo' in x).text.strip() if div.find('a', href=lambda x: x and 'releaseinfo' in x) else None
    rating = soup.find('div', attrs={'data-testid': 'hero-rating-bar__aggregate-rating__score'}).text if soup.find('div', attrs={'data-testid': 'hero-rating-bar__aggregate-rating__score'}) else None
    plot = soup.find('span', attrs={'data-testid': 'plot-xs_to_m'}).text.strip() if soup.find('span', attrs={'data-testid': 'plot-xs_to_m'}) else None

    if all([title, date, rating, plot]):
        print(title, date, rating, plot)
        with open('movies.csv', 'a', newline='', encoding='utf-8') as f:
            csv.writer(f).writerow([title, date, rating, plot])

def scrape_movies():
    start = time()
    soup = BeautifulSoup(requests.get(f'{BASE_URL}/chart/moviemeter/?ref_=nv_mv_mpm', headers=HEADERS).content, 'html.parser')
    
    movie_links = [f"{BASE_URL}{li.find('a')['href']}" for li in soup.find('div', attrs={'data-testid': 'chart-layout-main-column'}).find('ul').find_all('li')]
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(MAX_THREADS, len(movie_links))) as executor:
        executor.map(extract_movie_details, movie_links)
    
    print(f'Total time: {time() - start:.2f} seconds')

if __name__ == '__main__':
    scrape_movies()