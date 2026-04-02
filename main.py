from scraper import scrape_page
from exporter import export_to_csv, export_to_json
import time

def main():
    all_books = []

    for page in range(1, 6):  # 5 pages
        print(f"Scraping page {page}...")
        data = scrape_page(page)
        all_books.extend(data)
        time.sleep(1)  # éviter blocage serveur

    print(f"Total books scraped: {len(all_books)}")

    export_to_csv(all_books)
    export_to_json(all_books)

    print("Data exported successfully!")

if __name__ == "__main__":
    main()
