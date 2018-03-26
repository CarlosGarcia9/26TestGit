M=[[1,3],[2,4]]
N=[[8,9],[10,11]]
S=[[0,0],[0,0]]


for i in list(range(0,len(M))):
	for j in list(range(0,(len(N[0])))):

		aux=0
		for l in list(range((len(N)))):
			aux+=M[i][l]*N[l][j]

		S[i][j]=aux

print(S)


