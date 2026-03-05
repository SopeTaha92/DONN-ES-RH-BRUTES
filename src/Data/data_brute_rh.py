


import pandas as pd
from pathlib import Path
from datetime import datetime


today = datetime.now().strftime('%d_%m_%Y-%H_%M')
dir_path = Path(__file__).parent
dir_path.mkdir(parents=True, exist_ok=True)
file = dir_path / f"donnee_brute_rh{today}.csv"


def brute_data():
    
    data_rh = {
        'employee_id': ['EMP-001', 'EMP-002', 'EMP-003', 'EMP-004', 'EMP-005', 'EMP-006', 'EMP-007', 'EMP-008', 'EMP-009', 'EMP-010'],
        'full_name': ['alice martin', 'BOB DUPONT', 'charlie legrand', 'DIANA ROY', 'EVELYN TREMBlAY', 'FRANK KLEIN', 'GRACE LEROY', 'HENRY GAUTHIER', 'IVANA PETROV', 'JACK WILSON'],
        'department': ['IT', 'MARKETING', 'IT', 'SALES', 'HR', 'IT', 'MARKETING', 'SALES', 'IT', 'FINANCE'],
        'position': ['Data Analyst', 'Marketing Manager', 'Software Engineer', 'Sales Rep', 'HR Specialist', 'DevOps Engineer', 'Content Manager', 'Sales Director', 'Data Scientist', 'Financial Analyst'],
        'salary': ['45000€', '52000', '58000€', '38000', '42000€', '62000', '48000€', '65000', '70000€', '55000'],
        'experience_years': ['3', '5', '7', '2', '4', '8', '6', '10', '9', '5'],
        'hire_date': ['2021-03-15', '2019-06-20', '2017-11-10', '2022-01-08', '2020-08-25', '2016-04-12', '2018-09-30', '2014-07-18', '2015-12-01', '2019-03-22'],
        'city': ['paris', 'LYON', 'MARSEILLE', 'LILLE', 'TOULOUSE', 'BORDEAUX', 'NICE', 'STRASBOURG', 'MONTPELLIER', 'RENNES'],
        'performance_rating': ['A', 'B', 'A', 'C', 'B', 'A', 'B', 'A', 'A', 'B'],
        'bonus': ['10%', '8%', '12%', '5%', '7%', '15%', '9%', '18%', '20%', '10%']
    }

    df_data_brute_rh = pd.DataFrame(data_rh)
    df_data_brute_rh.to_csv(file, index=False)
    return df_data_brute_rh


