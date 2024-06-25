# Approach -1
class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def gcd(self, A, B):
        if A==0:
            return B
        if B==0:
            return A
        if A==0 and B==0:
            return 0
        hcf=0
        if A<B:
            mini=A
            maxi=B
        else:
            mini=B
            maxi=A
        for i in range(2,mini+1):
            if A%i==0 and B%i==0:
                hcf=i
                
        if hcf: return hcf
        return 1
     
# Approach -2
class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def gcd(self, A, B):
        if A<B:
            mini=A
            maxi=B
        else:
            mini=B
            maxi=A
        def dfs(a,b):
            if b==0:
                return a 
            else:
                return dfs(b, a%b)
                
        return dfs(maxi,mini)