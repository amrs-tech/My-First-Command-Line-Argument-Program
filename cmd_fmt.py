import sys
#getting the argument as starting number for staircase
tri_word = int(sys.argv[1])	
#length of staircase
for i in range(5):
	#print consecutive numbers in the staircase starting from tri_word
	print('{:>{i}}'.format(tri_word,i=i+1))
	tri_word+=1