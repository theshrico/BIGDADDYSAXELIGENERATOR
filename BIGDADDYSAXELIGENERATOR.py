import random
import time
print("               welcome to               ")
print("========================================")
print("       BIG DADDY SAXELI GENERATOR")
key = input("sex: type 'm' for male 'f' for female:")
def randomtable(names, surnames):
            input("press enter to run:")
            
            num = random.randrange(0,len(names))
            num2 = random.randrange(0,len(surnames))
        
            print(names[num]+ " " + surnames[num2])
if key == "m":
     while True:
        randomtable(["vaso","imeda","zaura","vasoia","merab","grigola","avto","gocha","givi","shota"],  ["walaxashvili","imerlishvili","avtandiluzbekishvili","ghomimcxobiashvili","doundobelishvili","laphshamiashvili","dzroxasadaishvili","virismoyvarulishvili"])
elif key == "f":
    while True:      
        randomtable(["lamara","nargiza","leila","nunu","natela","nedejda","nazibrola"],["walaxashvili","imerlishvili","avtandiluzbekishvili","ghomimcxobiashvili","mchadimcxobiashvili","kuxnashivarmeishvili","laphshamiashvili","dzroxasadaishvili","virismoyvarulishvili"])
else:
    print("that is not a correct response, exiting...")
    time.sleep(5)
    exit()
