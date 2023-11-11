import random

f = open("data.csv", "w")
f.write("First Name [Required],Last Name [Required],Email Address [Required],Password [Required],Class \n")

classList = ["Willow", "Oak", "Cherry", "Redwood", "Birch", "Pine", "Spruce"]

with open("names.txt") as file:
    for line in file:
        #print(line.rstrip())
        txt = line.rstrip()
        x = txt.split()

        first = x[0]
        last = x[1]

        lineInfo = first + "," + last + "," + first[0]+last+"@test.com" + "," + "dog123456" + "," + classList[random.randint(0,6)] + "," + "\n"
        f.write(lineInfo)
