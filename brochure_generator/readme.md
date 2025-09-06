# AI Brochure Generator

Generate professional company brochures in English or Bengali using AI and website content scraping.

## Features

- Scrapes company websites for relevant information and links
- Uses OpenAI GPT-4o to generate concise, informative brochures
- Supports English and Bengali output
- Gradio web UI for easy interaction
- Customizable dark mode UI

## How It Works

1. Enter the company name and website URL.
2. The app scrapes the landing page and relevant subpages (like About, Careers).
3. AI summarizes the content and generates a Markdown brochure.
4. The result is displayed in the browser and can be copied or saved.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your OpenAI API key in a `.env` file:
   ```env
   OPENAI_API_KEY=sk-...
   ```
3. Run the app:
   ```bash
   python main.ipynb
   # or open main.ipynb in Jupyter/VS Code and run all cells
   ```
4. The Gradio UI will open in your browser.
