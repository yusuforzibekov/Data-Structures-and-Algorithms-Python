"""Template for programming assignment: Print salary table"""
from typing import Tuple, List


def make_salary_table_string(
        humans_and_salaries: List[Tuple[str, str, int]]) -> str:
    def make_salary_row(i, first_name, last_name, annual_salary):
        monthly_salary = annual_salary / 12
        person_name = f"{last_name} {first_name[0]}."
        annual_str = f"{annual_salary:,}$"
        monthly_str = f"{monthly_salary:,.1f}$"
        return (
            f"{i:>5} | "
            f"{person_name:<20} | "
            f"{annual_str:^20} | "
            f"{monthly_str:^20}"
        )

    table = [
        "    # | Person Name          |    Annual Salary     |    Monthly Salary   ",
        "--------------------------------------------------------------------------"
    ]
    
    for i, (first_name, last_name, annual_salary) in enumerate(humans_and_salaries, 1):
        table.append(make_salary_row(i, first_name, last_name, annual_salary))
    
    return "\n".join(table)
