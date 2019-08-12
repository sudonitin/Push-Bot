import strgen

f = open("data.txt", "a")
f.write(strgen.StringGenerator("[\d\w]{3}").render())
f.close()

print("machayenge")
import os
os.system('git init')
os.system('git remote add origin https://github.com/globefire/Goals.git')
os.system('git add .')
os.system('git commit -m "some chang"')
os.system('git push origin master')
