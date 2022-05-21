import pickle
outfile = open("test.dat", "wb")
pickle.dump(12, outfile)
pickle.dump(3.14, outfile)
pickle.dump([1,2,3,4,5], outfile)
outfile.close()

infile = open("test.dat", "rb")
Data_list = []
while True:
    try:
        Data = pickle.load(infile)
    except EOFError:
        break
    Data_list.append(Data)

for line in Data_list:
    print(line)
infile.close()
