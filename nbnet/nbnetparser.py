import os

from bs4 import BeautifulSoup

from .forms import MovementForm


html_path = '/home/j1figuei/Documents/NBnetextract_files/tpl.html'

with open(html_path) as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')
    for result in soup.find_all('tr'):
        if result.td:
            movement_data = {}
            movement_data['account'] = result.contents[1].string
            movement_data['date'] = result.contents[2].string
            movement_data['description'] = result.contents[3].string
            movement_data['amount'] = result.contents[5].string
            form = MovementForm(movement_data)
            if form.is_valid():
                form.save()
