# Chap05/gplus_search_web_gui.py
import os
import json
from flask import Flask
from flask import request
from flask import render_template
from apiclient.discovery import build

app = Flask(__name__)
api_key = os.environ.get('GOOGLE_API_KEY')

@app.route('/')
def index():
    return render_template('search_form.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    if not query:
        # query not given, show an error message
        message = 'Please enter a search query!'
        return render_template('search_form.html', message=message)
    else:
        # search
        service = build('plus',
                        'v1',
                        developerKey=api_key)

        people_feed = service.people()
        search_query = people_feed.search(query=query)
        search_results = search_query.execute()
        return render_template('search_results.html',
                               query=query,
                               results=search_results['items'])

if __name__ == '__main__':
    app.run(debug=True)
