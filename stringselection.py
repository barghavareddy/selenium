import re

name=input("enter string to be searched in sub string")

x=re.findall("[A-Z][A-Z][A-Z][^a-zA-Z0-9][0-9][0-9][0-9][0-9][0-9][A-Z][1-9]",name)
if x!=None:
    print(x)
if x==[] :
    print("not matched with your string,ZERO matchings")