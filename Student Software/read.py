f = open("hello.txt",'r')
data = f.read()
newdata = str(data.split(" "))

fw = open('hello.txt','w')
fw.write(newdata)
fw.close()