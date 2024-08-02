class Salary:
    def __init__(self,bsal):
        self._bsal=bsal

    def getBasicSalary(self):
        print("Basic salary:",self._bsal)
        

class Allowances(Salary):
    s_allowances={"HRA":0.4,"DA":0.3,"TA":0.15}
    def __init__(self,bsal):
        super().__init__(bsal)
        self.calAllowances()

    def calAllowances(self):
        for key in s_allowances:
           total_allowances += self.s_allowances[key]*self._basic
        return total_allowances

class Deductions(Salary):
    s_deductions={"PF":0.12,"Insurance":5000}
    def __init__(self,bsal):
        super().__init__(bsal)
        self.calDeductions()
            
        

    def calDeductions(self):
        total_deductions = 0
        for key in self.s_deductions:
            if type(self.s_deductions[key]) is not int:
                total_deductions += self.s_deductions[key]*self._basic
            else:
                total_deductions += self.s_deductions[key]
        return total_deductions
    
        
class calculateSalary(Allowances,Deductions):
    def __init__(self,bsal):
         super().__init__(bsal)
         self.getSalary()

    def pTax(msal):
        prof_tax=0
        if msal >= 8500 and msal<=10000:
            prof_tax=200
        elif msal>10000 and msal<=30000:
            prof_tax=300
        elif msal>30000:
            prof_tax=500
        return prof_tax
    

    def getSalary(self):


        
        gsal = self.bsal + self.calcAllowances(bsal)
        p_tax=pTax(gsal)
        nsal=gsal-self.calcDeductions(self._bsal)-p_tax
        print("Basic salary : ",self.bsal)
        print("Allowances : ",self.calcAllowances())
        print("Deductions : ",self.calcDeductions())
        print("Proffesional Tax : ",p_tax)
        print("Gross salary : ",gsal)
        print("Net salary : ",nsal)


sal=calculateSalary(8000)





             
            
            
            
