whoami
pwd # print working directory

# / is the root directory
# /bin is  where built in programs are stored
# /data is for misc data files 
# /users is where users' personal files are stored 
# /tmp is for temporary files that don't need to be stored

#wget https://www.uhpc-training.co.uk/material/technology_and_tooling/bash_shell/shell-novice.zip

ls -F ./shell-novice # -F flag adds / to end of directories

ls -F ./shell-novice/shell/test_directory

# NB: * and ? are called wildcards 
# * - anything  
# ? - any character 

# sort sorts the contents of a file 
# default is to sort by alphabetical 
# -n flag changes to sort numerical

# head shows us the head of a file 
# -1 flag shows first line etc

# piping
# pipe just means use the output of the thing before the pipe as the input of the thing after the pipe  

# filtering 
# filters are simple functions that turn lines of bash input into lines of bash output 
# one should write all bash programs in this way 
# since then the filter can become part of a pipeline
# piping filters is why unix (now bash) have been so succesful 
# exmaples are: 
# - wc: word count (with arguments like -l for length, -c for characters...)
# - sort: sorts files, in alphabetical order or numerically with the flag -n


# < and > mean read from and write to
# for example: 
# wc < *.csv means count the contents of any file ending in .csv 
# wc *.csv > lengths.txt means output ls information to lenghts.csv


# overwriting and appending 
# single chevron > overwrites a file if it already exists
# double chevron >> appends to a file if it already exists


# Writing shell scripts 
# Shell scripts are programs written in bash 

# $1 means the first argument after the script name will be parsed as an argument 


# for loops 
# variables are used to store info that we want to use later 
# a variable is a container that we put something inside that we give a label
# changing a variable's value is like changing what's inside the container
# $ tells the command line to treat what comes after it as a variable
# ${variable} -- note {} are used to clearly indicate what the variable name is
# it is good practive to echo the commands inside a loop to check before running