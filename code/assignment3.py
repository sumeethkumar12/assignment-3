#let a,b,c be insured scooty,car,truck drivers respectively
a=2000
b=4000
c=6000
d=a+b+c
#p_Aa is probability of scooty driver meeting accident and so on
p_a=a/d
p_b=b/d
p_c=c/d
p_Aa=1/100
p_Ab=3/100
p_Ac=15/100

#conditional probability that accident met guy was scooty driver
#lets use bayers theorm
#p_aA is p(a/A) theoritically 
 
p_aA= (p_a * p_Aa )/((p_a * p_Aa)+(p_b *p_Ab)+(p_c*p_Ac) )  

print (p_aA)
