from math import sqrt

# Here we read in the file
def readfile(filename):
	lines=[line for line in file(filename)]

	# First line is the column titles
	colnames=lines[0].strip().split('\t')[1:]
	rownames=[]
	data=[]
	for line in lines[1:]:
		p=line.strip().split('\t')
		# First column in each row is the rownames
		rownames.append(p[0])
		# The data for this row is the remainder of the row
		data.append([float(x) for x in p[1:]])
	return rownames[0],colnames[0],data[0]
# The top row is the list of column names 
# The leftmost row is now the list of rownames
# Everything to the right of the leftmost row is now a list of data

# We will be using the pearson correlation score to measure blog similarity
def pearson(v1,v2):
	# Simple sums
	sum1=sum(v1)
	sum2=sum(v2)

	# Sum of the squares
	sum1Sq=sum([pow(v,2) for v in v1])
	sum2Sq=sum([pow(v,2) for v in v2      ])