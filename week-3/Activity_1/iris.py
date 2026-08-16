file = open("./iris.data", "r")
count = 0
flowers = set() #(duplicate values are not allowed in set so we can use set to get unique flower names)
for line in file:
    count = count + 1
    data = line.strip().split(',') #take 1 row and seperate it into pieces last 
    #ani , vayo vane kati kun samma tukraune vanne thahunxa
    
    if len(data) > 4:
        flowers.add(data[4])

print("Total records:", count)
print("Total different flowers:", len(flowers))
print("Flower names:", flowers)
file.close()




