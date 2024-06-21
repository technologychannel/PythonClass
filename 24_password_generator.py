import random
alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
alphabet_upper = alphabet.upper()

numbers = '1,2,3,4,5,6,7,8,9,0'
symbols = '!,@,#,%,^,&,*,(),-'

all_combine = alphabet+ ','+  alphabet_upper+ ',' + numbers+ ','+ symbols

all_combine_to_list = all_combine.split(",")
print(all_combine_to_list)
random1= random.choice(all_combine_to_list)
random2 = random.choice(all_combine_to_list)
random3= random.choice(all_combine_to_list)
random4 = random.choice(all_combine_to_list)
random5 = random.choice(all_combine_to_list)
random6 = random.choice(all_combine_to_list)
random7= random.choice(all_combine_to_list)
random8 = random.choice(all_combine_to_list)
random9 = random.choice(all_combine_to_list)
random10 = random.choice(all_combine_to_list)

pasword = random1 + random2 + random3 + random4 + random5 + random6 + random7 + random8 + random9 + random10

print(f"Generated Password is : {pasword}")