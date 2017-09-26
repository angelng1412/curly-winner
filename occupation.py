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
        return render_template("ace.html", table = reader, randjob = randJob())

reader = csv.reader(open(file))


f = open("occupations.csv", 'r')
s = f.read()
data = s.split("\n")
data = data[1:-1]

def makeDict(): 
        jobDict = {}
        for job in data:
                if job.find('"') >= 0:
                        thing = job.split('"')
                        jobDict[thing[1]] = float(thing[2][1:])
                else:
                        thing = job.split(',')
                        jobDict[thing[0]] = float(thing[1])
        return jobDict

def randJob():
        dict = makeDict()
        num = random.uniform(0,99.8)
        tmp = 0 
        for job, percent in dict.iteritems():
                tmp += percent
                if num < tmp:
                        return job        
                
if __name__ == "__main__":
        app.debug = True
        app.run()
                        
