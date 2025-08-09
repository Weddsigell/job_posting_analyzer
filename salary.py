def predict_salary(salary_from: int = 0, salary_to: int = 0):
    if salary_from and salary_to:
        return (salary_to + salary_from) / 2
    elif not salary_from:
        return salary_to * 0.8
    elif not salary_to: 
        return salary_from * 1.2
    else:
        return None
    

def predict_salary_hh(vacancy: dict):
    if (not vacancy['salary']) or (not vacancy['salary']['currency'] == 'RUR'):
        return None
    
    return predict_salary(vacancy['salary']['from'], vacancy['salary']['to'])


def predict_salary_sj(vacancy: dict):
    if not vacancy['currency'] == 'rub':
        return None
    
    return predict_salary(vacancy['payment_from'], vacancy['payment_to'])
