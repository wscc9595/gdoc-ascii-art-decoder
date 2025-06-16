# gdoc-ascii-art-decoder
 Python script that renders ASCII art from unicode characters in public Google Doc url

## Example

👉 [Live Doc Link](https://docs.google.com/document/d/e/2PACX-1vTg4yGC9sCz1szduFK3_ZHXPlq35e0AMiub-48oo93HRGB29pEehrdv9JBq-1hbypNckt7dCnf2ZvMn/pub)

## Features
- fetch table from public Google Doc url
- Parse table data using `BeautifulSoup`
- Group Unicode characters with their x- and y-coordinates
- Construct a 2D grid and print it as ASCII art
- Can decode any similar structure by changing the gdoc link

## Getting Started
```bash
pip install -r requirements.txt
python main.py [url]
