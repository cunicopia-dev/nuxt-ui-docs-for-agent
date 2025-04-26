# Nuxt UI Component Documentation Scraper

**Purpose:** This project provides a way to download the Nuxt UI component documentation in Markdown format. This is particularly useful for feeding into AI/LLM workflows, enabling agents or language models to access and reason about Nuxt UI component usage, props, and examples as part of their knowledge base.

This project contains a Python script (`main.py`) designed to scrape component documentation from the official [Nuxt UI website](https://ui.nuxt.com/components). It extracts the documentation content for each component and saves it as an individual Markdown file.

## Features

*   Fetches the list of available components from the main components page.
*   Scrapes the primary content area of each component's documentation page.
*   Cleans the HTML by removing navigation, sidebars, footers, and other non-essential elements.
*   Converts the cleaned HTML to Markdown format using the `html2text` library.
*   Saves each component's documentation into a separate `.md` file within the `nuxt-components-docs` directory.
*   Includes the source URL as a comment at the top of each generated Markdown file.

## Prerequisites

*   Python 3.x
*   Required Python packages (see `requirements.txt`)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <repository-directory>
    ```

2.  **Install dependencies:**
    It's recommended to use a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

## Usage

Simply run the main script from the project's root directory:

```bash
python main.py
```

The script will:
1.  Fetch the list of component URLs from `https://ui.nuxt.com/components`.
2.  Create the output directory `nuxt-components-docs` if it doesn't exist.
3.  Iterate through each component URL, scrape its content, convert it to Markdown, and save it as `nuxt-components-docs/<component-name>.md`.
4.  Print progress messages to the console.

Upon completion, the scraped Markdown files will be available in the `nuxt-components-docs` folder.

## Dependencies

*   `requests`: For making HTTP requests to fetch web pages.
*   `beautifulsoup4`: For parsing HTML content.
*   `html2text`: For converting HTML to Markdown.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## License

This project is licensed under the terms of the LICENSE file.
