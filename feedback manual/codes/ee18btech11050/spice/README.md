# Details regarding files in the directory:
'ee18btech11050_sim.net' is the netlist for simulating the phase-shift oscillator in question.

'ee18btech11050_sim.py' and 'ee18btech11050_sim2.py' are python files to plot 'ee18btech11050.dat'.

## Instructions for Simulation and plotting the output:

### Setup

--> Make Sure that all the .net, .dat, .py files are present in the same folder. LM741.MOD should be present in the same folder as well.

--> In the terminal use the 'cd' command to move to the folder where all the above files are present. 
### Simulation : 

 -->Enter the following command . This simulates the 'ee18btech11050_sim.net' file and creates a 'ee18btech11050.dat' file.
  ``` 
ngspice ee18btech11050_sim.net
```

--> Exit from ngspice cmd line using the following code . This gets you back to the present working directory.
 ``` 
exit
```

--> Enter the following commands. This runs 'ee18btech11050_sim.py' and 'ee18btech11050_sim2.py'  which plots 'ee18btech11028_sim.dat' file and saves it as 'ee18btech11050_sim.pdf' and 'ee18btech11050_sim2.pdf' respectively.
``` 
python3 ee18btech11050_sim.py
python3 ee18btech11050_sim2.py
```
