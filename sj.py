import requests
from itertools import count
from salary import predict_salary_sj


MOSCOW = 4
MONTH = 30
DEVELOPER = 48


def fetch_vacancies_sj(lang: str, sj_key: str):
    url= 'https://api.superjob.ru/2.0/vacancies/'
    payload = {
        'town': MOSCOW,
        'period': MONTH,
        'catalogues': DEVELOPER,
        'keyword': lang
    }
    headers = {
        'X-Api-App-Id': sj_key,
    }  
        
    for page in count(0):
        payload['page'] = page
        page_response = requests.get(url, params=payload, headers=headers)
        page_response.raise_for_status()
        page_response = page_response.json()

        yield from page_response['objects'] 
        
        if not page_response['more']:
            return page_response['total']


def get_statistic_sj(lang, sj_key):
    vacancies_found = 0
    average_salaries = []
    vacanies = fetch_vacancies_sj(lang, sj_key)
    while True:
        try:
            vacancy = next(vacanies)
        except StopIteration as e:
            vacancies_found = e.value
            break

        salary = predict_salary_sj(vacancy)
        if salary:
            average_salaries.append(salary)
    
    vacancies_processed = len(average_salaries)
                
    average_salary = 0
    if len(average_salaries) != 0:
        average_salary = sum(average_salaries) / len(average_salaries)

    result = {
        "vacancies_found": vacancies_found,
        "vacancies_processed": vacancies_processed,
        "average_salary": average_salary
    }
    return result
