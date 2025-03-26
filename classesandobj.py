from functools import reduce
class student:
    studentScores = {}
    scores = []
    def calculateTotalScore(self):
         return reduce(lambda a, b: a + b, self.scores)
    def userInput(self, name):
        self.scores = []
        while len(self.scores) < 5:
            num = input("enter score:")
            if num.isnumeric():
                self.scores.append(int(num))
            else:
                print("enter a valid number")
            print(self.scores)

        scoreSum = self.calculateTotalScore()
        self.studentScores[name] = scoreSum
        print(self.studentScores)
        return self.studentScores
count = 0
s = student()
n = input("enter number of students:")
for i in range(int(n)):
    name = input("enter student name:")
    studentScore = s.userInput(name)
    totalMarks = studentScore[name]
    if i==0:
         myStudentMarks = totalMarks   
    if totalMarks > myStudentMarks:
         count += 1

print("number of students who scored more than me:", count)


         
