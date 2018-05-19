#!/usr/bin/env python3
import sys
tax_rate = [0.03, 0.10, 0.20, 0.25, 0.30, 0.35, 0.45]
deduct = [0, 105, 555, 1005, 2755, 5055, 13505]
def calculator(data_list):
    try:
        for worker in data_list[1:]:
            work_list = worker.split(':')
            job_num = work_list[0]
            salary = int(work_list[1])
            in_expenses = salary*0.165
            pay_taxes = salary - in_expenses - 3500
            if salary <= 0 and job_num < 0:
                raise ValueError
            elif pay_taxes <= 0:
                tax_amount_payable = 0
            elif pay_taxes <= 1500:
                tax_amount_payable = pay_taxes * tax_rate[0] - deduct[0]
            elif pay_taxes > 1500 and pay_taxes <= 4500:
                tax_amount_payable = pay_taxes * tax_rate[1] - deduct[1]
            elif pay_taxes > 4500 and pay_taxes <= 9000:
                tax_amount_payable = pay_taxes * tax_rate[2] - deduct[2]
            elif pay_taxes > 9000 and pay_taxes <= 35000:
                tax_amount_payable = pay_taxes * tax_rate[3] - deduct[3]
            elif pay_taxes > 35000 and pay_taxes <= 55000:
                tax_amount_payable = pay_taxes * tax_rate[4] - deduct[4]
            elif pay_taxes > 55000 and pay_taxes <= 80000:
                tax_amount_payable = pay_taxes * tax_rate[5] - deduct[5]
            else:
                tax_amount_payable = pay_taxes * tax_rate[6] - deduct[6]
            income = salary - in_expenses - tax_amount_payable
            print("%s:%.2f"%(job_num,income)) 
    except ValueError:
        print("Parameter Error")

if __name__ == "__main__":
    calculator(sys.argv)


