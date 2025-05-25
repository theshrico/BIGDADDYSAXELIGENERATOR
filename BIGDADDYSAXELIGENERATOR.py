import random
import time
print("               welcome to               ")
print("========================================")
print("       BIG DADDY SAXELI GENERATOR")
key = input("sex: type 'm' for male 'f' for female:")
if key == "m":
    while True:
        input("press enter to run:")
        saxelebi = ["vaso","imeda","zaura","vasoia","merab","grigola","avto","gocha","givi","shota"]
        num = random.randrange(0,len(saxelebi))
        gvarebi = ["walaxashvili","imerlishvili","avtandiluzbekishvili","ghomimcxobiashvili","doundobelishvili","laphshamiashvili","dzroxasadaishvili","virismoyvarulishvili"]
        num2 = random.randrange(0,len(gvarebi))
        print(saxelebi[num] + " " + gvarebi[num2])
elif key == "f":
    while True:
        input("press enter to run:")
        saxelebi = ["lamara","nargiza","leila","nunu","natela","nedejda","nazibrola"]
        num = random.randrange(0,len(saxelebi))
        gvarebi = ["walaxashvili","imerlishvili","avtandiluzbekishvili","ghomimcxobiashvili","mchadimcxobiashvili","kuxnashivarmeishvili","laphshamiashvili","dzroxasadaishvili","virismoyvarulishvili"]
        num2 = random.randrange(0,len(gvarebi))
        print(saxelebi[num] + " " + gvarebi[num2])
else:
    print("that is not a correct response, exiting...")
    time.sleep(5)
    exit()
