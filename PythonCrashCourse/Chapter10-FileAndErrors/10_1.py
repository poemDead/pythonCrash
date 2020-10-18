with open('PythonCrashCourse/Chapter10-FileAndErrors/learninig_python.txt') as file:
    print(file.read())

with open('PythonCrashCourse/Chapter10-FileAndErrors/learninig_python.txt') as file:   
    for line in file:
        print(line.rstrip())

with open('PythonCrashCourse/Chapter10-FileAndErrors/learninig_python.txt') as file:
    lines = file.readlines()

for line in lines:
    print(line.rstrip())