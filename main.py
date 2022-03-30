import os
cur_dir = os.getcwd()
dict={}
for i in os.listdir(cur_dir):
    dir_one=os.path.join(cur_dir,i)
    if os.path.isdir(dir_one):
        for j in os.listdir(dir_one):
            if ".out" in j:
                file_to_read = os.path.join(dir_one,j)
                r=open(file_to_read, "r")
                text = r.readlines()
                for line in text:
                    if "PWSCF        :" in line:
                        time = line.split()[-2]
                        print(time)
                        if "m" in time and "h" in time:
                            hours=float(time.split("h")[0])
                            residual=time.split("h")[1]
                            minutes=float(residual.split("m")[0])
                            residual=residual.split("m")[1]
                            try:
                                seconds=float(residual.replace("s", ""))
                            except:
                                seconds=0.0
                            second_to_write=3600*hours+60*minutes+seconds
                        if "m" in time and "h" not in time:
                            minutes = float(time.split("m")[0])
                            residual = time.split("m")[1]
                            try:
                                seconds = float(residual.replace("s", ""))
                            except:
                                seconds = 0.0
                            second_to_write =  60 * minutes + seconds
                        if "m" not in time and "h" not in time:
                            try:
                                seconds = float(time.replace("s", ""))
                            except:
                                seconds = 0.0
                            second_to_write = seconds
                        dict[file_to_read.split(os.sep)[-2]] = second_to_write
write_dir=os.path.join(cur_dir, "time_analysis.csv")
w=open(write_dir, "w")
for i in dict:
    w.write("{},{}\n".format(i,dict[i]))
w.close()