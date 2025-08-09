from pprint import pprint
from fetch_vacancy import fetch_vacancy_hh, fetch_vacancy_sj
from salary import predict_salary_hh, predict_salary_sj


def get_statistic_hh(languages):
    vacancies_found = 0
    vacancies_processed = 0
    average_salary = []
    
    for vacancy in fetch_vacancy_hh(languages):      
        vacancies_found += 1
        salary = predict_salary_hh(vacancy)
        if salary:
            average_salary.append(salary)
            vacancies_processed += 1   
                
    average_salary = sum(average_salary) / len(average_salary)
    result = {
        languages: {
            "vacancies_found": vacancies_found,
            "vacancies_processed": vacancies_processed,
            "average_salary": int(average_salary)
        }
    }
    return result


def main():
    languages = [
        'Python',
        'JavaScript',
        'C#',
        'C++',
    ]
    
    # for lang in languages:
    #     pprint(get_statistic_hh(lang))
    
    # for lang in languages:
    #     pprint(get_statistic_hh(lang))
    
    result = fetch_vacancy_sj(languages[0])
    pprint(result)
    

def main33():
    languages = [
        'Python',
        'JavaScript',
        'C#',
        'C++',
    ]    
    
    data_hh = {
        'python': {
            'total': 100,
            'processed': 25,
            'avg_salary': 100000
        },
        'javascript': {
            'total': 100,
            'processed': 25,
            'avg_salary': 100000
        },
    }
    data_sj = {
        'python': {
            'total': 100,
            'processed': 25,
            'avg_salary': 100000
        },
        'javascript': {
            'total': 100,
            'processed': 25,
            'avg_salary': 100000
        },
    }


if __name__ == "__main__":
    main()
