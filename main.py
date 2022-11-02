

def SumarPares (str="" , pos=0, sum=0):
  if (pos == len(str)):
    print (sum)
    return 0
    
  if (int(str[pos])%2==0):
      sum = sum + int(str[pos])
      #print(sum,pos)
  return SumarPares(str, pos+1, sum)

#print("andy"[0])
SumarPares("16582234",0)