import sys
import requests
from bs4 import BeautifulSoup

'''
URL_heart = 'https://docs.google.com/document/d/e/2PACX-1vTg4yGC9sCz1szduFK3_ZHXPlq35e0AMiub-48oo93HRGB29pEehrdv9JBq-1hbypNckt7dCnf2ZvMn/pub'
URL_test = 'https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'
URL = 'https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub'
'''

def print_grid_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find_all('td')
    max_x = 0
    max_y = 0
    temp = []
    group = []
    for i in range(3, len(table)):
        td_text = table[i].get_text()
        if i % 3 == 0:
            td_text = int(td_text)
            if td_text > max_x:
                max_x = td_text
        if i % 3 == 2:
            td_text = int(td_text)
            if td_text > max_y:
                max_y = td_text
        temp.append(td_text)
        if len(temp) == 3:
            group.append(temp)
            temp = []
    grid = [[' ' for i in range(0, max_x+1)] for i in range(0, max_y+1)]
    for sub in group:
        grid[sub[2]][sub[0]] = sub[1]
    #print(grid)
    for row in reversed(grid):
        print(''.join(row))

def main():
    if len(sys.argv) < 2:
        print("Usage: main.py <url>")
        sys.exit(1)
    url = sys.argv[1]
    print_grid_from_url(url)
if __name__ == '__main__':
    main()
 
            


#print_grid_from_url(URL_test)
#print_grid_from_url(URL)
#print_grid_from_url(URL_heart)
        
