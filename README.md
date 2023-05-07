# Culture-Scout---Hackathon

# NLP Scraping Tool

This NLP Tool is a simple graphical user interface (GUI) application that uses natural language processing (NLP) techniques to perform sentiment analysis, organization discovery, and contact information extraction on text from websites by providing the website's URL.

## Installation

This application requires Python 3.x and the following packages:

- transformers
- beautifulsoup4
- lxml
- PyQt5

You can install these packages using pip:

```
pip install transformers beautifulsoup4 lxml PyQt5
```

Alternatively, install the required packages by running the following command in your terminal or command prompt:

```
pip install -r requirements.txt
```

## Usage

To run the application, simply execute the following command:

```
python nlpscrape_tool.py
```

This will launch the GUI window. You can enter a URL to scrape text from a website, or you can enter your own text in the text input area. Clicking the "Analyze" button will perform the NLP analysis and display the results in the result label area.

The results include the sentiment label, the top 5 organizations mentioned in the text along with the number of mentions, and any email addresses and phone numbers found in the text.

## Credits

This application was developed as a project for CultureScout Hackathon. It uses the following open-source packages:

- [transformers](https://github.com/huggingface/transformers)
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/)
- [lxml](https://lxml.de/)
- [PyQt5](https://www.riverbankcomputing.com/software/pyqt/))

To run the code on your system, install the required packages by running the following command in the terminal or command prompt:
pip install -r requirements.txt


