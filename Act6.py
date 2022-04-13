'''import time
outfile = open("out.txt", "w")
outfile.write("Example ")
outfile.write("output ")
outfile.write("text file\n")
outfile.write("xyz Coordinates\n")
outfile.write("MODEL\n")
outfile.write("ATOM %3d" % 1)
seq = "n %5.1f%5.1f%5.1f" % (0, 1, 2)
print("n %5.1f%5.1f%5.1f" % (0, 1, 2))
outfile.write(seq)
outfile.write("\n")
outfile = open("lines.txt", "w")
previous_time = time.time()
for i in range(100):
     outfile.write(f'Line #{i+1} time {time.time() - previous_time}\n')
     # time.sleep(0.0001)
outfile.close()'''

infile = open("names.txt", "r")
for line in infile:
    last_name = line.split()
    print(last_name[1])

infile.close()


