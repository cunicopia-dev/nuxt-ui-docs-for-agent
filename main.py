#!/usr/bin/env python3
"""
Scrapes component documentation from the Nuxt UI website (https://ui.nuxt.com/components)
and saves each component's documentation as a Markdown file.
"""

import requests
from bs4 import BeautifulSoup
import html2text
import os
import urllib.parse
from typing import Set

BASE: str = "https://ui.nuxt.com"
START: str = f"{BASE}/components"
OUTDIR: str = "nuxt-components-docs"


def fetch_component_links(start_url: str) -> Set[str]:
    """
    Fetches the main components page and extracts URLs for individual component pages.

    Args:
        start_url: The URL of the main components page.

    Returns:
        A set of unique URLs for the component documentation pages.
    """
    print(f"Fetching component links from {start_url}...")
    resp = requests.get(start_url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    main = soup.select_one("main")
    if not main:
        raise ValueError("Could not find the main content area on the page.")

    links = {
        urllib.parse.urljoin(BASE, a["href"].split("#")[0])
        for a in main.select("a[href^='/components/']")
        if a["href"] != "/components/"
    }
    print(f"Found {len(links)} component links.")
    return links


def scrape_component_page(url: str) -> str:
    """
    Scrapes the content of a single component page and converts it to Markdown.

    Args:
        url: The URL of the component page to scrape.

    Returns:
        The component documentation in Markdown format.
    """
    print(f"Scraping {url}...")
    page_resp = requests.get(url)
    page_resp.raise_for_status()
    page_soup = BeautifulSoup(page_resp.text, "html.parser")

    # Target the main documentation content area
    content = (
        page_soup.select_one("main .lg\:col-span-8")  # Specific layout column
        or page_soup.select_one("main")               # Fallback to main tag
        or page_soup.body                             # Fallback to body
    )
    if not content:
         # If even body is not found, something is very wrong
        raise ValueError(f"Could not find content body for URL: {url}")


    # Strip out unwanted elements like navbars, sidebars, footers, etc.
    selectors_to_remove = [
        "header", "nav", "aside", "footer",
        ".on-this-page", ".breadcrumb", ".edit-this-page"
    ]
    for sel in selectors_to_remove:
        for node in content.select(sel):
            node.decompose()

    # Convert the cleaned HTML content to Markdown
    md = html2text.html2text(str(content))
    return md


def save_markdown(md_content: str, source_url: str, outdir: str) -> None:
    """
    Saves the Markdown content to a file, named based on the component slug.

    Args:
        md_content: The Markdown string to save.
        source_url: The original URL the content was scraped from.
        outdir: The directory to save the Markdown file in.
    """
    # Generate a file-system friendly slug from the URL
    slug = source_url.replace(f"{BASE}/components/", "").strip("/").replace("/", "_")
    if not slug:
        print(f"Warning: Could not generate slug for URL: {source_url}. Skipping.")
        return
    filepath = os.path.join(outdir, f"{slug}.md")

    # Write the content, including a source comment
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"<!-- source: {source_url} --> {md_content}")
    print(f"Saved markdown to {filepath}")


def main():
    """
    Main function to orchestrate the scraping process.
    """
    # 1) Fetch landing page and discover component URLs
    try:
        component_links = fetch_component_links(START)
    except (requests.RequestException, ValueError) as e:
        print(f"Error fetching component links: {e}")
        return # Exit if we can't get the links

    # 2) Prepare output directory
    os.makedirs(OUTDIR, exist_ok=True)
    print(f"Output directory '{OUTDIR}' ensured.")

    # 3) Scrape each component page and save as Markdown
    for url in sorted(component_links):
        try:
            markdown_content = scrape_component_page(url)
            save_markdown(markdown_content, url, OUTDIR)
        except requests.RequestException as e:
            print(f"Error scraping {url}: {e}")
        except ValueError as e:
            print(f"Error processing content from {url}: {e}")
        except IOError as e:
            print(f"Error saving file for {url}: {e}")
        # Continue to the next URL even if one fails

    print(f"✅ Done! Markdown files are in the '{OUTDIR}' folder.")


if __name__ == "__main__":
    main()
