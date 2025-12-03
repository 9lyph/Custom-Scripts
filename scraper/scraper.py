#!/usr/bin/env python3
"""
"""

import re
import time
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import argparse
import sys
from typing import Set, List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class ContactScraper:
    def __init__(self, delay: float = 1.0, max_pages: int = 50):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (compatible; ContactScraper/1.0; +https://yourdomain.com/bot)'
        })
        self.delay = delay
        self.max_pages = max_pages
        self.visited = set()
        self.emails = set()
        self.phones = set()
        self.social_links = {}
        self.addresses = set()
        self.company_name = None

        # Common social media patterns
        self.social_patterns = {
            'linkedin': r'(?:linkedin\.com/(?:in|company)/([^/\s]+))',
            'twitter': r'(?:twitter\.com|x\.com)/([@a-zA-Z0-9_]{1,15})',
            'facebook': r'facebook\.com/([a-zA-Z0-9.\-]+)',
            'instagram': r'instagram\.com/([a-zA-Z0-9_.\-]+)',
            'youtube': r'youtube\.com/(?:channel/|user/|@)([^/\s]+)',
            'tiktok': r'tiktok\.com/@([a-zA-Z0-9_.\-]+)',
        }

    def normalize_url(self, url: str, base_url: str) -> str:
        return urljoin(base_url, url)

    def is_valid_url(self, url: str, domain: str) -> bool:
        if url in self.visited:
            return False
        if not url.startswith(('http://', 'https://')):
            return False
        parsed = urlparse(url)
        if parsed.netloc != domain:
            return False
        if parsed.path.endswith(('.pdf', '.jpg', '.png', '.zip', '.exe')):
            return False
        return True

    def extract_emails(self, text: str):
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        found = re.findall(email_pattern, text, re.IGNORECASE)
        for email in found:
            email = email.lower().strip()
            if self.is_valid_email(email):
                self.emails.add(email)

    def is_valid_email(self, email: str) -> bool:
        # Filter out obvious fakes
        fake_domains = ['example.com', 'test.com', 'domain.com', 'yoursite.com']
        if any(fake in email for fake in fake_domains):
            return False
        if email.count('@') != 1:
            return False
        return True

    def extract_phones(self, text: str):
        # International phone patterns
        phone_patterns = [
            r'\+?[\d\s\-\(\)]{10,20}',  # General
            r'\+?\d{1,4}[\s.-]?\(?\d{1,4}\)?[\s.-]?\d{1,4}[\s.-]?\d{1,9}',  # Complex
        ]
        for pattern in phone_patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                cleaned = re.sub(r'[^\d+]', '', match)
                if len(cleaned.replace('+', '')) >= 8:
                    self.phones.add(match.strip())

    def extract_social(self, text: str, url: str):
        for platform, pattern in self.social_patterns.items():
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                username = match.strip('/ ')
                if platform not in self.social_links:
                    self.social_links[platform] = set()
                self.social_links[platform].add(username)

    def extract_address(self, text: str):
        # Simple address detection (street, city, zip, country)
        address_indicators = ['street', 'ave', 'avenue', 'road', 'rd', 'blvd', 'lane', 'ln', 'drive', 'dr',
                              'suite', 'ste', 'apt', 'po box', r'\d{5,}', r'[A-Z]{2}\s+\d{5}']
        lines = text.split('\n')
        for line in lines:
            lower = line.lower()
            if any(indicator in lower for indicator in address_indicators):
                if len(line.strip()) > 20:
                    self.addresses.add(line.strip())

    def get_company_name(self, soup: BeautifulSoup, url: str):
        if self.company_name:
            return

        # Try multiple methods
        title = soup.find('title')
        if title and title.text:
            name = title.text.split('|')[0].split('-')[0].strip()
            if len(name) > 2 and not name.lower().startswith('home'):
                self.company_name = name

        # OpenGraph / Meta
        og_title = soup.find('meta', property='og:site_name')
        if not og_title and soup.find('meta', attrs={'name': 'application-name'}):
            og_title = soup.find('meta', attrs={'name': 'application-name'})
        if og_title and og_title.get('content'):
            self.company_name = og_title['content'].strip()

    def scrape_page(self, url: str):
        if url in self.visited:
            return
        self.visited.add(url)

        try:
            logging.info(f"Scraping: {url}")
            response = self.session.get(url, timeout=10)
            if response.status_code != 200:
                return

            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text(separator='\n')

            # Extract data
            self.extract_emails(text + response.text)
            self.extract_phones(text)
            self.extract_social(response.text, url)
            self.extract_address(text)
            self.get_company_name(soup, url)

            # Follow internal links (same domain)
            domain = urlparse(url).netloc
            for link in soup.find_all('a', href=True):
                href = self.normalize_url(link['href'], url)
                if (self.is_valid_url(href, domain) and 
                    len(self.visited) < self.max_pages and 
                    href not in self.visited):
                    time.sleep(self.delay)
                    self.scrape_page(href)

        except Exception as e:
            logging.warning(f"Error scraping {url}: {e}")

    def scrape(self, start_url: str):
        parsed = urlparse(start_url)
        if not parsed.scheme:
            start_url = 'https://' + start_url
        self.scrape_page(start_url)

    def print_results(self):
        print("\n" + "="*60)
        print(f"SCRAPING RESULTS FOR: {list(self.visited)[0] if self.visited else 'N/A'}")
        print("="*60)

        if self.company_name:
            print(f"Company Name: {self.company_name}")

        print(f"\nEmails Found ({len(self.emails)}):")
        for email in sorted(self.emails):
            print(f"   • {email}")

        print(f"\nPhone Numbers ({len(self.phones)}):")
        for phone in sorted(self.phones):
            print(f"   • {phone}")

        print(f"\nSocial Media:")
        for platform, handles in self.social_links.items():
            for handle in handles:
                print(f"   • {platform.capitalize()}: {handle}")

        if self.addresses:
            print(f"\nPossible Addresses:")
            for addr in self.addresses:
                print(f"   • {addr}")

        print(f"\nPages crawled: {len(self.visited)}")
        print("="*60)

def main():
    parser = argparse.ArgumentParser(description="Extract contact info from a website")
    parser.add_argument("url", help="Target website (e.g. example.com or https://example.com)")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay between requests (seconds)")
    parser.add_argument("--max-pages", type=int, default=50, help="Maximum pages to crawl")
    
    args = parser.parse_args()

    scraper = ContactScraper(delay=args.delay, max_pages=args.max_pages)
    scraper.scrape(args.url)
    scraper.print_results()

    # Optional: save to file
    if scraper.emails:
        with open("scraped_emails.txt", "w") as f:
            for email in scraper.emails:
                f.write(email + "\n")
        print(f"\nEmails saved to scraped_emails.txt")

if __name__ == "__main__":
    # Install required packages:
    # pip install requests beautifulsoup4 lxml
    main()
