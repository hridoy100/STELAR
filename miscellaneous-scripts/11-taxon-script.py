import os,sys
import numpy as np
import os.path
import matplotlib.pyplot as plt
import re
import time

#def run(command):
#      #print(command)
#      p1 = os.popen(command)
#      temp = p1.readlines()
#      p1.close()
      #print(temp)
#      return temp

def run(command):
     # print(command)
      p1 = os.popen(command)
      temp = p1.readline()
      p1.close()
      #print(temp)
      return temp.rstrip()

RFRate_file = open("11-taxa-time.csv","w+")
time_file = open("11-RFRateFile.csv","w+")


RFRate_file.write("name,RF_rate\n")
time_file.write("method,name,time\n")

folders = ["estimated_Xgenes_strongILS", "simulated_Xgenes_strongILS"]
genes = ["5", "15", "25", "50", "100"]


true_gene_tree = "model_tree_trimmed.label"

if __name__=="__main__":
      #folders = next(os.walk('.'))[1] # get the folder list
      for  folder in folders:
            for gene in genes:
                        gt = folder + "/" + folder.replace("X", gene)
                        print(gt)
                        #if gene != 15 and folder != "estimated_Xgenes_strongILS": continue
                        for i in range(1,21):
                              #run("rm -r con*")
                              run("rm -r root.gt*")
                              location = gt + "/Rep"+str(i)+"_"+gene+"genes.strip.labeled"
                              speciestree = gt + "/Rep"+str(i)+"_"+gene+"genes"
                              #print(location)
                              run("cp "+location+" gt")
                              run("./reroot_tree.pl -t gt -r K -o root.gt")
                              run("cp root.gt "+location)

                              # running MPEST
                              timestamp = time.time()
                              run("./mpest ./root.gt ./specieslist11 1")
                              run("cp root.gt.best.of.10.tre "+speciestree+".mpest")
                              time_file.write("MPEST"+gt+", "+str(time.time()-timestamp)+"\n")

                              # Running STELAR
                              timestamp = time.time()
                              res = run("java -jar stelar.jar -i "+location+" -st "+speciestree+".stelar")
                              time_file.write("STELAR"+gt+", "+str(time.time()-timestamp)+"\n")

                              #running ASTRAL
                              timestamp = time.time()
                              run("java -jar astral.5.5.6.jar -i root.gt -o "+speciestree+".astral -x")
                              time_file.write("ASTRAL"+gt+", "+str(time.time()-timestamp)+"\n")


                              #running ASTRAL
                              timestamp  = time.time()
                              run("java -jar SuperTriplets_v1.1.jar root.gt "+speciestree+".SuperTriplets")
                              time_file.write("SuperTriplets_v1"+gt+", "+str(time.time()-timestamp)+"\n")



                              RF_rate = run("python2 getFpFn.py -e  "+speciestree+".mpest -t  "+ true_gene_tree +"  | sed 's/.//; s/,//' |awk '{print $3}'")
                              RFRate_file.write("MPEST,"+gt+","+RF_rate+"\n")

                              RF_rate = run("python2 getFpFn.py -e  "+speciestree+".stelar -t  " + true_gene_tree + "  | sed 's/.//; s/,//' |awk '{print $3}'")
                              RFRate_file.write("MPEST,"+gt+","+RF_rate+"\n")

                              RF_rate = run("python2 getFpFn.py -e  "+speciestree+".astral -t  " + true_gene_tree + "  | sed 's/.//; s/,//' |awk '{print $3}'")
                              RFRate_file.write("MPEST,"+gt+","+RF_rate+"\n")

                              RF_rate = run("python2 getFpFn.py -e  "+speciestree+".SuperTriplets -t  " + true_gene_tree + "  | sed 's/.//; s/,//' |awk '{print $3}'")
                              RFRate_file.write("SuperTriplets,"+gt+","+RF_rate+"\n")



            #break
