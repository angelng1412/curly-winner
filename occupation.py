from flask import Flask, render_template
import csv
import random


file = "occupations.csv"
app = Flask(__name__)

@app.route("/")
def root():
        return "root"

@app.route("/occupations")
def occupation():
        jobs = {}
        createDict(reader)
        return render_template("ace.html", table = reader)

reader = csv.reader(open(file))


#Job dictionary


#creates Dictionary consisting of Jobs as keys and percents as its values
def createDict(csv):
        for rows in csv:
                if rows[0] == "Job Class" or rows[0] == "Total":
                        continue
                else:
                        jobs[rows[0]] = float(rows[1])


#pick a random job based off percentages.
def randomJob(dict):
        randNum = float(random.randint(1,998)/10) #create a random float
        #print randNum
        for keys in dict.keys():
                #pick a random key to make it more random.
                #  
                #Say two jobs have the same percentage, if picking random job is not added, then the job that 
                #       appears first will always be printed.
                key = random.choice(dict.keys())
                randNum = randNum - dict[key]
                #everytime time a job is picked, subtract its percentage from randNUM
                del dict[key]
                #delete the job name to avoid pciking it again
                #print key
                if randNum <= 0:
                        #if randNum <0, print out the job that caused this and break the loop
                        return key
                        break


           

if __name__ == "__main__":
        app.debug = True
        app.run()