class Site1Scraper:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        print(f'Scraping {self.url}')