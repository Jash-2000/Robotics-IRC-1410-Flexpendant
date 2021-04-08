###################################

## Robotics Assignment
## Author : Jash Shah

###################################

from sympy import *


Q1 = Matrix([
			[0,-1,0,0],
			[1,0,0,0],
			[0,0,0,0],
			[0,0,0,0]
	])

Q2 = Q1 

#########################################3

var('m1 L1 m2 L2 a b')

a = m1*L1
b = m2*L2

I1 = Matrix([
			[a*L1/3, 0, 0, -a/2],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[-a/2, 0, 0, m1]
	])

I2 = Matrix([
			[b*L2/3, 0, 0, -b/2],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[-b/2, 0, 0, m2]
	])


##############################################

var('X1 X2')
var('S1 C1 S2 C2')

S1 = sin(X1)
S2 = sin(X2)
C1 = cos(X1)
C2 = cos(X2)

d11 = Matrix([
			[-S1, 0, C1, -L1*S1],
			[C1, 0, S1, C1*L1],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
	])


d12 = Matrix([
			[0,0,0,0],
			[0,0,0,0],
			[0,0,0,0],
			[0,0,0,0]
	])

d21 = Matrix([
			[-S1*C2, S1*S2, C1, ((-L2*S1*C2) - (L1*S1))],
			[C2*C1, -C1*S2, S1, ((L2*C2*C1) + (L1*C1))],
			[0,0,0,0],
			[0,0,0,0]
	])

d22 = Matrix([
			[-C1*S2, -C1*C2, 0, -L2*C1*S2],
			[-S1*S2, -S1*C2, 0, -L2*S1*S2],
			[C2, -S2, 0, L2*C2],
			[0, 0, 0, 0]
	])	

#####################################################


M11 = ( ( d11.multiply(I1) ).multiply(d11.T) ) + ( ( d21.multiply(I2)).multiply(d21.T) )

M22 = ( d22.multiply(I2) ).multiply(d22.T)

M21 = ( d22.multiply(I2) ).multiply(d21.T)
M12 = M21


print( "\n M11 = \n\n", trigsimp(trace(M11) ))
print( "\n M21 = \n\n", trigsimp(trace(M21)) )
print( "\n M12 = \n\n", trigsimp(trace(M12)) )
print( "\n M22 = \n\n", trigsimp(trace(M22)) )


##############################################################################


T01 = Matrix([
			[C1, 0, S1, L1*C1],
			[S1, 0, -C1, L1*S1],
			[0, 1, 0, 0],
			[0, 0, 0, 1]
	])


T12 = Matrix([
			[C2, -S2, 0, L2*C2],
			[S2, C2, 0, L2*S2],
			[0, 0, 1, 0],
			[0, 0, 0, 1]
	])

T02 = T01.multiply(T12)

temp = diff(d22,X2)
temp1 = diff(d21,X1)

#####################################################################################


h122 = temp@I2@d21.T

h211 = temp1@I2@d22.T

h221 = temp1@I2@d22.T

h121 = temp1@I2@d21.T

print( "\n h122 = \n\n", trigsimp(trace(h122)) )
print( "\n h211 = \n\n", trigsimp(trace(h211)) )
print( "\n h221 = \n\n", trigsimp(trace(h221)) )
print( "\n h121 = \n\n", trigsimp(trace(h121)) )

######################################################################################
