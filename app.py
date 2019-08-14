import strgen

f = open("data.txt", "a")
f.write(strgen.StringGenerator("[\d\w]{3}").render())
f.close()

print("machayenge")
