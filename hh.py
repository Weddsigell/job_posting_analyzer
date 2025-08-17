import requests
from itertools import count
from salary import predict_salary_hh


MOSCOW = 1
MONTH = 30
DEVELOPER = 96


def fetch_vacancies_hh(lang: str):
    url = 'https://api.hh.ru/vacancies'
    payload = {
        'professional_role': DEVELOPER,
        'area': MOSCOW,
        'period': MONTH,
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


def get_statistic_hh(lang):
    vacancies_found = 0
    vacancies_processed = 0
    average_salaries = []
    
    for vacancy in fetch_vacancies_hh(lang):      
        vacancies_found += 1
        salary = predict_salary_hh(vacancy)
        if salary:
            average_salaries.append(salary)
            vacancies_processed += 1   
                
    average_salary = sum(average_salaries) / len(average_salaries)
    result = {
        "vacancies_found": vacancies_found,
        "vacancies_processed": vacancies_processed,
        "average_salary": average_salary
    }
    return result