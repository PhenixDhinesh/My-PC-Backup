import pickle

my={"1": 1,"2":2}
fi=open("picklke.txt","wb")
#wb- write binary,writes in binary form
pickle.dump(my,fi)
fi.close()

bi=open("picklke.txt","rb")
print(pickle.load(bi))