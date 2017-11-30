
import pickle

shopListFile = 'shopList.data'

shopList = ['apple','mango','carrot']

f = open(shopListFile,'wb',-1)
pickle.dump(shopList,f)
f.close()

del shopList

f = open(shopListFile,'rb')
storiedList = pickle.load(f)
print(storiedList)
