import requests
from pprint import pprint
from itertools import count


def predict_rub_salary(vacancy: dict):
    if not vacancy['salary']:
        return None    
     
    if not vacancy['salary']['currency'] == 'RUR':
        return None
    
    salary_from = vacancy['salary']['from']
    salary_to = vacancy['salary']['to']
    
    if salary_from and salary_to:
        return (salary_to + salary_from) / 2
    elif not salary_from:
        return salary_to * 0.8
    else: 
        return salary_from * 1.2
    

def fetch_vacancy(url: str, payload: dict):
    for page in count(0):
        payload['page'] = page
        page_response = requests.get(url, params=payload)
        page_response.raise_for_status()
        page_payload = page_response.json()
		
        yield from page_payload['items']
        
        if page >= page_payload['pages']:
            break


def main():
    url = 'https://api.hh.ru/vacancies'
    payload = {
        'professional_role': 96,
        'area': 1,
        'period': 30,
        'text': 'Python разработчик'
    }
    vacancies_found = 0
    vacancies_processed = 0
    average_salary = []
    
    for vacancy in fetch_vacancy(url, payload):      
        vacancies_found += 1
        salary = predict_rub_salary(vacancy)
        if salary:
            average_salary.append(salary)
            vacancies_processed += 1   
                
    average_salary = sum(average_salary) / len(average_salary)
    result = {
        'Python': {
            "vacancies_found": vacancies_found,
            "vacancies_processed": vacancies_processed,
            "average_salary": int(average_salary)
        }
    }
    pprint(result)


if __name__ == "__main__":
    main()
