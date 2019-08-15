import strgen

f = open("data.txt", "a")
f.write(strgen.StringGenerator("[\d\w]{3}").render())
f.close()

print("machayenge")
import os
os.system("git init")
print(1)
os.system("git remote add origin https://github.com/globefire/Goals.git")
print(2)
os.system("git add .")
print(3)
os.system('git commit -m "a new commit"')
print(4)
os.system('git push origin master')
print(5)
