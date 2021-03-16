# Q1
class Student:
  def __init__(self,entryNo,courses):
    self.entryNo = entryNo
    self._courses = courses
    self.attemptedQuizzes=[]
    self.quizTitle =[]
    self.cc=[]
    self.qc =[]
  def attempt(self, courseCode, quizTitle, attemptedAnswers):
    # assert type(courseCode, quizTitle, attemptedAnswers) = string.
    # self.qc stores the courseCode and quizTitle as lsit of tuples
    self.qc.append((courseCode,quizTitle))
    # self.cc stores the courseCode in a list
    self.cc.append(courseCode)
    # self.quizTitle stores the quizTitle in a list
    self.quizTitle.append(quizTitle)
    if (courseCode,quizTitle) not in self.attemptedQuizzes:
      # self.attemptedQuizzes stores the attempted quizzes in proper format having courseCode, quizTitle, attemptedAnswers
      self.attemptedQuizzes.append([courseCode,quizTitle,attemptedAnswers])
  def getUnattemptedQuizzes(self): 
    # ans = [] is an empty array which subsequently adds quiz name and subject as the loop proceeds.
    ans = []
    for i in self._courses:
      # 1st case when no quiz is attempted of the particular course, or in other words the attempted section doesn't contain the course. We directly 
      # add all the quiz elements and the corresponding course code also.
      if i.courseName() not in self.cc:
        for j in i.objects():
          ans.append((i.courseName(),j.titled()))
      # In this case we check if the user has attempted atleast one quiz and then subsequently append unattempted quizzes
      else:
        for j in i.objects():
          if j.titled() not in self.quizTitle : 
            ans.append((i.courseName(),j.titled()))
          elif (i.courseName(),j.titled()) not in self.qc : 
            ans.append((i.courseName(),j.titled()))
    return ans
  def  getAverageScore(self,courseCode):
    for i in self._courses:
      if i.courseName() == courseCode:
        courseCode = i 
    final = 0
    count = 0
    for i in self.attemptedQuizzes:
      for j in courseCode.objects():
        if i[0] == courseCode.courseName():
        # assert j.score(i[2]) >=0
          count+=1/2
          final+=j.score(i[2])
    # the returned value is the final score / count of quizzes of a particular course.
    return final/count
class Course:
  def __init__(self,courseCode,quizObjects):
    # Initialising name to contents of the class.
    self.courseCode= courseCode
    self.quizObjects = quizObjects
  def courseName(self):
    # To access elements of the class outside the class.
    return self.courseCode
  def objects(self):
    return self.quizObjects
class Quiz:
  def __init__(self,title,correctOpt):
    self.title = title
    self._correctOpt = correctOpt 
  def titled(self):
    return self.title 
  def score(self,selectedOptions):
    count = 0
    for i in range(len(self._correctOpt)):
      if self._correctOpt[i] == selectedOptions[i]:
        count+= 1
        # assert count>=0
    return count
col100q1 = Quiz('Quiz1', ['a','b','b'])
col100q2 = Quiz('Quiz2', ['b', 'd', 'c'])
col100 = Course('COL100', [col100q1, col100q2])
mtl100q1 = Quiz('Quiz1', ['a', 'b', 'd'])
mtl100q2 = Quiz('Quiz2', ['d', 'c', 'a'])
mtl100 = Course('MTL100', [mtl100q1, mtl100q2])
s1 = Student('2019Mcc2562', [col100, mtl100])
s2 = Student('2017cc10377', [col100])
s1.attempt('MTL100', 'Quiz1', ['a', 'b', 'b'])
s1.attempt('COL100', 'Quiz1', ['a', 'b', 'c'])
s1.attempt('MTL100', 'Quiz2', ['b', 'd', 'c'])


print(s1.getUnattemptedQuizzes())
print(s1.getAverageScore('COL100'))



