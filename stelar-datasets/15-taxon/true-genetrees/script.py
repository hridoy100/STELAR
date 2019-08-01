import os,sys
import numpy as np
import os.path
import matplotlib.pyplot as plt

def run(command):
	p1 = os.popen(command)
	temp = p1.readline()
	p1.close()
	return temp.rstrip()


if __name__=="__main__":
   for i in range(1,11):
      f = open("t.text","w+")
      res = run("cat R"+str(i)+"/all_gt.tre")
      res = res.replace('"',"").replace(" ","")
      #command = "printf "+res+" > R"+str(i)+"/all_gt.tre" 
      print(res)
      print("-------------------------")
      f.write(res)
      f.close()
      #run("cp t.text R"+str(i)+"/all_gt.tre")
