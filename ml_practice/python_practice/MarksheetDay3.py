

name=input('enter name:')
enr=input('enter enrollment number:')
mathematics=int(input('enter your marks in mathematics:'))
physics=int(input('enter your marks in physics:'))
chemistry=int(input('enter your marks in chemistry:'))
science=int(input('enter your marks in science:'))
biology=int(input('enter your marks in biology:'))
Environment_studies=int(input('enter your marks in environment studies:'))


def printing(name,enr,avg,cgpa,strong,weak):
        print("GSEB BOARD ")
        print("NAME OF THE STUDENT:" , name)
        print('ENROLLMENT NUMBER:',enr)

        if mathematics<35 :
                print("YOU'VE FAILED IN MATHEMATICS")
        if physics<35 :
                print("YOU'VE FAILED IN PHYSICS")
        if chemistry<35 :
                print("YOU'VE FAILED IN CHEMISTRY")
        if biology<35 :
                print("YOU'VE FAILED IN BIOLOGY")    
        if Environment_studies<35 :
                print("YOU'VE FAILED IN ENVIRONNMENT STUDIES") 
        if science<35 :
                print("YOU'VE FAILED IN SCIENCE")     

        print('AVERAGE MARKS:',avg)
        print('CGPA:',cgpa)
        print('HIGHEST MARKS IN SUBJECT',strong)
        print('LOWEST MARK IN SUBJECT',weak)     

       

def calc_sum(name,enr,mathematics,physics,chemistry,science,biology,Environment_studies):
    sum=mathematics+ physics + chemistry + science + biology + Environment_studies
    avg = sum/6
    cgpa=((sum/60))
    strong=max(mathematics,science,physics,Environment_studies,biology,chemistry)
    weak=min(mathematics,science,physics,Environment_studies,biology,chemistry)
    printing(name,enr,avg,cgpa,strong,weak)

calc_sum(name,enr,mathematics,physics,chemistry,science,biology,Environment_studies)
