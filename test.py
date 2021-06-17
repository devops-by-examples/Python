colors = ["white", "red", "blue", "green", "white"]

count = 0 
for c in colors:
  if c == "white":
    count += 1

for n in range(count):
	colors.remove("white")

print(str(colors))
