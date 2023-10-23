from bs4 import BeautifulSoup

def parse_html_with_error_handling(file_path):
    """
    Parse an HTML file to extract the question, article text, and image sources.

    Parameters:
    - file_path (str): The path to the HTML file to be parsed.

    Returns:
    - dict: A dictionary containing the extracted question, article text, and image sources.
    """

    # Initialize the default return values
    question, article_text, images = None, None, []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'lxml')

        # Safely extract the question using the id="kb_article_question"
        if soup.find(id="kb_article_question"):
            question = soup.find(id="kb_article_question").text.strip()

        # Safely extract the article text using the id="kb_article_text"
        if soup.find(id="kb_article_text"):
            article_text = soup.find(id="kb_article_text").text.strip()

            # Extract the image sources from the article text
            for img in soup.find(id="kb_article_text").find_all("img"):
                image_info = {"src": img["src"]}
                images.append(image_info)

    except Exception as e:
        # Handle any parsing or file reading errors
        print(f"Error parsing file {file_path}: {e}")

    return {
        "question": question,
        "article_text": article_text,
        "images": images
    }
