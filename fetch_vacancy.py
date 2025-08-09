import requests
from itertools import count
from environs import Env
env = Env()
env.read_env()


def fetch_vacancy_sj(lang: str):
    url= 'https://api.superjob.ru/2.0/vacancies/'
    payload = {
        'town': 4,
        'period': 30,
        'catalogues': 48,
        'keyword': lang
    }
    headers = {
        'X-Api-App-Id': env.str('SJ_KEY'),
    }  
        
    for page in count(0):
        page_response = requests.get(url, params=payload, headers=headers)
        page_response.raise_for_status()
        page_response = page_response.json()
		
        yield from page_response['objects']
        
        if not page_response['more']:
            break


def fetch_vacancy_hh(lang: str):
    url = 'https://api.hh.ru/vacancies'
    payload = {
        'professional_role': 96,
        'area': 1,
        'period': 30,
        'text': lang
    }
    
    for page in count(0):
        payload['page'] = page
        page_response = requests.get(url, params=payload)
        page_response.raise_for_status()
        page_response = page_response.json()
		
        yield from page_response['items']
        
        if page >= page_response['pages']:
            break
