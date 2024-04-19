from calculate.uncertainty import type_a,type_b
if __name__ =="__main__":
    tenperiods = [11.41,11.91,11.87]
    print(type_a(tenperiods))
    #Step on measuring device
    a=0.001
    print("Digital uncertainty:",type_b(a,'digital'))
    print("Analog:", type_b(a,'analog'))
    print("Wrong method:", type_b(a,'Analog'))


#Delete this file later!