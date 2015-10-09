# -*- encoding utf-8 -*-
# Levenshtein distance

def levenshtein_distance(s1, s2):
	linecurrent = [i for i in range(len(s2)+1)]

	i = 0 # < len(s1)
	while i <len(s1):
		linelast = linecurrent[:] #There are must use deep copy, if I use linelast = linecurrent will get the save refrence for the same object
		linecurrent[0] = linelast[0] + 1
		for k in range(1, len(s2)+1):
			linecurrent[k] = min(linelast[k-1]+(0 if s1[i] == s2[k-1] else 1), linelast[k]+1, linecurrent[k-1]+1)
		i += 1
	return linecurrent[len(s2)]

if __name__ == '__main__':
	print levenshtein_distance("hello","cat")
