import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from scraper import Website, get_links_user_prompt

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
MODEL = 'gpt-4o-mini'
openai = OpenAI()

link_system_prompt = (
    "You are provided with a list of links found on a webpage. "
    "You are able to decide which of the links would be most relevant to include in a brochure about the company, "
    "such as links to an About page, or a Company page, or Careers/Jobs pages.\n"
    "Do NOT make up any links that are not available on the website.\n"
    "You should respond in JSON as in this example:"
    """
    {
        \"links\": [
            {\"type\": \"about page\", \"url\": \"https://full.url/goes/here/about\"},
            {\"type\": \"careers page\", \"url\": \"https://another.full.url/careers\"}
        ]
    }
    """
)

def get_links(url):
    website = Website(url)
    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": link_system_prompt},
            {"role": "user", "content": get_links_user_prompt(website)}
        ],
        response_format={"type": "json_object"}
    )
    result = response.choices[0].message.content
    return json.loads(result)

def get_all_details(url):
    result = "Landing page:\n"
    result += Website(url).get_contents()
    links = get_links(url)
    for link in links["links"]:
        result += f"\n\n{link['type']}\n"
        result += Website(link["url"]).get_contents()
    return result

def get_brochure_user_prompt(company_name, url):
    user_prompt = f"You are looking at a company called: {company_name}\n"
    user_prompt += f"Here are the contents of its landing page and other relevant pages; use this information to build a short brochure of the company in markdown.\n"
    user_prompt += get_all_details(url)
    user_prompt = user_prompt[:1_000] # Truncate if more than 1,000 characters
    return user_prompt

def create_brochure(company_name, url, language):
    system_prompt_english = (
        "You are an assistant that analyzes the contents of a company website landing page "
        "and creates a short brochure about the company for prospective customers, investors and recruits. Respond in markdown."
    )
    system_prompt_bengali = (
        "You are an assistant that analyzes the contents of a company website landing page "
        "and creates a short brochure about the company for prospective customers, investors and recruits. Respond in markdown and in Bengali language."
    )
    if language == "English":
        message = [
            {"role": "system", "content": system_prompt_english},
            {"role": "user", "content": get_brochure_user_prompt(company_name, url)}
        ]
    elif language == "Bengali":
        message = [
            {"role": "system", "content": system_prompt_bengali},
            {"role": "user", "content": get_brochure_user_prompt(company_name, url)}
        ]
    stream = openai.chat.completions.create(
        model=MODEL,
        messages=message,
        stream=True
    )
    result = ""
    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result
