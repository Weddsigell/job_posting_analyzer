import requests
from itertools import count
from environs import Env
from salary import predict_salary_sj
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
        payload['page'] = page
        page_response = requests.get(url, params=payload, headers=headers)
        page_response.raise_for_status()
        page_response = page_response.json()
		
        yield from page_response['objects']
        
        if not page_response['more']:
            break


def get_statistic_sj(lang):
    vacancies_found = 0
    vacancies_processed = 0
    average_salary = []
    
    for vacancy in fetch_vacancy_sj(lang):      
        vacancies_found += 1
        salary = predict_salary_sj(vacancy)
        if salary:
            average_salary.append(salary)
            vacancies_processed += 1   
                
    average_salary = sum(average_salary) / len(average_salary)
    result = {
        lang: {
            "vacancies_found": vacancies_found,
            "vacancies_processed": vacancies_processed,
            "average_salary": int(average_salary)
        }
    }
    return result
