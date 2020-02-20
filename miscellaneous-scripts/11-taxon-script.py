import os,sys
import numpy as np
import os.path
import matplotlib.pyplot as plt
import re
import time
def run(command):
      #print(command)
      p1 = os.popen(command)
      temp = p1.readlines()
      p1.close()
      #print(temp)
      return temp


folders = ["estimated_Xgenes_strongILS", "simulated_Xgenes_strongILS"]
genes = ["5", "15", "25", "50", "100"]
#f1 = open("mpest.time","w+")
f2 = open("bristy.csv","w+")
#f3 = open("stelar.time","w+")
#f4 = open("SuperTriplets.time", "w+")
if __name__=="__main__":
      #folders = next(os.walk('.'))[1] # get the folder list
      for  folder in folders:
            for gene in genes:
                        gt = folder + "/" + folder.replace("X", gene)
                        print(gt)
                        #if gene != 15 and folder != "estimated_Xgenes_strongILS": continue
                        for i in range(1,21):
                              #run("rm -r con*")
                              #run("rm -r root.gt*")
                              location = gt + "/Rep"+str(i)+"_"+gene+"genes.strip.labeled"
                              speciestree = gt + "/Rep"+str(i)+"_"+gene+"genes"
                              #print(location)
                              run("cp "+location+" gt")
                              run("./reroot_tree.pl -t gt -r K -o root.gt")
                              run("cp root.gt "+location)

                              # running MPEST
                              #timestamp = time.time()
                              #run("./mpest ./root.gt ./specieslist11 1")
                              #run("cp root.gt.best.of.10.tre "+speciestree+".mpest")
                              #f1.write(gt+", "+str(time.time()-timestamp)+"\n")

                              # Running STELAR
                              #timestamp = time.time()
                              #run("java -jar stelar.bristy.jar -i root.gt -o "+speciestree+".stelar.bristy -x")
                              #f3.write(gt+", "+str(time.time()-timestamp)+"\n")

                              #running ASTRAL
                              #timestamp = time.time()
                              run("java -jar astral.5.6.3.jar -i root.gt -o "+speciestree+".astral.mp -x")
                              #f2.write(gt+", "+str(time.time()-timestamp)+"\n")


                              #break
                              #timestamp  = time.time()
                              #run("java -jar SuperTriplets_v1.1.jar root.gt "+speciestree+".SuperTriplets")
                              #f4.write(gt+", "+str(time.time()-timestamp)+"\n")
                              run("java -jar stelar.bristy.jar -i "+location+" -o st -x")
                              run("./strip_edge_support2.pl -i st -o "+speciestree+".stelar.bristy")
                              run("rm st")
            #break
