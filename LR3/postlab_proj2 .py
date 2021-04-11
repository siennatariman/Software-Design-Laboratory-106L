import random
from operator import attrgetter

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        
        for count in range(number):
            self.scores.append(0)

        

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i-1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        averageScore = sum(self.scores) / len(self.scores)
        return averageScore
    
    def getHighScore(self):
        """Returns the highest score."""
        highestScore = max(self.scores)
        return highestScore
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
    
    def Display(self):
        self.averageScore = sum(self.scores) / len(self.scores)
        self.highestScore = max(self.scores)

        print("Student Name: ", self.name)
        print("Score: ", self.scores)
        print("Highest Score: ", self.highestScore)
        print("Average Score: ", self.averageScore)


def main():
    

    student_1 = Student("Ken", 3)
    student_2 = Student("Benny", 3)
    student_3 = Student("Lisa", 3)
    student_4 = Student("Wendy", 3)
    student_5 = Student("Chaeyoung", 3)
    student_6 = Student("Seulgi", 3)

    

    for i in range(3):
        student_1.setScore(i, 80+i)

    for i in range(3):
        student_2.setScore(i, 70+i)

    for i in range(3):
        student_3.setScore(i, 91+i)
    
    for i in range(3):
        student_4.setScore(i, 75+i)

    for i in range(3):
        student_5.setScore(i, 86+i)

    for i in range(3):
        student_6.setScore(i, 95+i)
 
        

    list_of_Students = [student_1, student_2, student_3, student_4, student_5, student_6]

    print("\n ORDER OF ELEMENTS BEFORE SHUFFLING")
    for x in range(len(list_of_Students)):
        list_of_Students[x].Display()

    
    random.shuffle(list_of_Students)

    print("\n ORDER OF ELEMENTS AFTER SHUFFLING")
    for y in range(len(list_of_Students)):
        list_of_Students[y].Display()

    list_of_Students.sort(key=attrgetter('highestScore'), reverse=True)

    print("\n ORDER OF ELEMENTS AFTER SORTING - By highest score")
    for y in range(len(list_of_Students)):
        list_of_Students[y].Display()

    

if __name__ == "__main__":
    main()


