s_allowances={"HRA":0.4,"DA":0.3,"TA":0.15}
s_deductions={"PF":0.12,"Insurance":5000}

def calcAllowances(basic):
    total_allowances = 0
    for key in s_allowances:
        total_allowances += s_allowances[key]*basic
    return total_allowances

def calcDeductions(basic):
    total_deductions = 0
    for key in s_deductions:
        if type(s_deductions[key]) is not int:
            total_deductions += s_deductions[key]*basic
        else:
            total_deductions += s_deductions[key]
    return total_deductions


def pTax(msal):
    prof_tax=0
    if msal >= 8500 and msal<=10000:
        prof_tax=200
    elif msal>10000 and msal<=30000:
        prof_tax=300
    elif msal>30000:
        prof_tax=500
    return prof_tax

def calculateSalary():
    bsal = int(input("enter ur basic salary : "))
    gsal = bsal + calcAllowances(bsal)
    p_tax=pTax(gsal)
    nsal=gsal-calcDeductions(bsal)-p_tax
    print("Basic salary : ",bsal)
    print("Allowances : ",calcAllowances(bsal))
    print("Deductions : ",calcDeductions(bsal))
    print("Proffesional Tax : ",p_tax)
    print("Gross salary : ",gsal)
    print("Net salary : ",nsal)
               
calculateSalary()
               
               
               
               
               
                








