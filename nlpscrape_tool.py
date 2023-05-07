import transformers
import re
from collections import Counter
from bs4 import BeautifulSoup
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout

model = transformers.pipeline('text-classification', model='bert-base-uncased')
entity_recognition = transformers.pipeline('ner', model='dslim/bert-base-NER')

def analyze_text(text, task='sentiment-analysis'):
    # Sentiment analysis
    sentiment = model(text)[0]['label']
    if sentiment == 'LABEL_0':
        sentiment = 'Negative'
    elif sentiment == 'LABEL_1':
        sentiment = 'Positive'
    else:
        sentiment = 'Unknown'
    
    # Organization discovery
    entities = entity_recognition(text)
    organizations = [entity['word'] for entity in entities if entity['entity'] == 'ORG']
    organization_count = Counter(organizations)
    top_organizations = organization_count.most_common(5)
    
    # Contact information extraction
    emails = re.findall(r'\b[\w.-]+?@\w+?\.\w+?\b', text)
    phone_numbers = re.findall(r'\d{3}[-.\s]??\d{3}[-.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-.\s]??\d{4}|\d{3}[-.\s]??\d{4}', text)
    
    # Reporting and visualization
    result = f'Sentiment: {sentiment}\n\n'
    result += 'Top Organizations:\n'
    for organization in top_organizations:
        result += f'- {organization[0]} ({organization[1]} mentions)\n'
    result += '\n'
    result += f'Emails: {", ".join(emails)}\n'
    result += f'Phone numbers: {", ".join(phone_numbers)}'
    
    return result

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    # Extract text content from HTML tags
    text = ' '.join([tag.text for tag in soup.find_all('p')])
    return text

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My NLP Tool')
        self.setGeometry(300, 300, 400, 300)

        self.url_label = QLabel('Enter URL:')
        self.url_input = QLineEdit(self)
        self.text_label = QLabel('Text:')
        self.text_input = QTextEdit(self)
        self.analyze_button = QPushButton('Analyze', self)
        self.analyze_button.clicked.connect(self.analyze_text)
        self.result_label = QLabel('')

        vbox = QVBoxLayout()
        vbox.addWidget(self.url_label)
        vbox.addWidget(self.url_input)
        vbox.addWidget(self.text_label)
        vbox.addWidget(self.text_input)
        vbox.addWidget(self.analyze_button)
        vbox.addWidget(self.result_label)
        self.setLayout(vbox)

        self.show()

    def analyze_text(self):
        url = self.url_input.text()
        text = scrape_website(url)
        self.text_input.setText(text)
        result = analyze_text(text)
        self.result_label.setText(result)

if __name__ == '__main__':
    app = QApplication([])
    ex = MyApp()
    app.exec_()
