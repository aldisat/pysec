# open the file with the read-only permit
f = open('access.log', "r")
# use deadlines to read all lines in the file
# the variable "lines" is a list containing all lines
lines = f.readline()
print(lines)
# close the file after reading the lines
f.close()
