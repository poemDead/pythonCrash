with open('PythonCrashCourse/Chapter10-FileAndErrors/learninig_python.txt') as file:
    lines = file.readlines()

for line in lines:
    line = line.replace('Python','C')
    print(line.rstrip())