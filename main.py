from pprint import pprint
from hh import get_statistic_hh
from sj import get_statistic_sj
from terminaltables import AsciiTable
from environs import Env
env = Env()
env.read_env()


def create_table(statistics: dict, title: str):
    headers = ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата']
    table = AsciiTable([headers], title)
    
    for lang, statistic_data in statistics.items():
        table.table_data.append([
            lang,
            statistic_data['vacancies_found'],
            statistic_data['vacancies_processed'],
            statistic_data['average_salary'],
        ]) 

    return table.table


def main():
    sj_key = env.str('SJ_KEY')
    languages = [
        'Python',
        'JavaScript',
        'C#',
        'C++',
    ]
    statistics_hh = {}
    statistics_sj = {}
    
    for lang in languages:
        statistics_hh[lang] = get_statistic_hh(lang)
        statistics_sj[lang] = get_statistic_sj(lang, sj_key)
    
    print(create_table(statistics_hh,'HeadHunter Moscow'))
    print(create_table(statistics_sj, 'SuperJob Moscow'))


if __name__ == "__main__":
    main()
