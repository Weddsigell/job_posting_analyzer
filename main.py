from pprint import pprint
from hh import get_statistic_hh
from sj import get_statistic_sj
from salary import predict_salary_hh, predict_salary_sj


def main():
    languages = [
        'Python',
        'JavaScript',
        'C#',
        'C++',
    ]
    
    for lang in languages:
       pprint (get_statistic_sj(lang))
    

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
