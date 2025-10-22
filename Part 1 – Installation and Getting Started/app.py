from flask import Flask, render_template
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

def get_live_scores():
    url = "https://static.cricinfo.com/rss/livescores.xml"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        root = ET.fromstring(response.content)
        
        scores = []
        for item in root.findall('.//item'):
            title = item.find('title').text if item.find('title') is not None else 'N/A'
            link = item.find('link').text if item.find('link') is not None else '#'
            description = item.find('description').text if item.find('description') is not None else 'N/A'
            scores.append({'title': title, 'link': link, 'description': description})
        return scores
    except requests.exceptions.RequestException as e:
        print(f"Error fetching RSS feed: {e}")
        return []
    except ET.ParseError as e:
        print(f"Error parsing RSS feed: {e}")
        return []

@app.route('/')
def index():
    scores = get_live_scores()
    return render_template('index.html', scores=scores)

if __name__ == '__main__':
    app.run(debug=True)
