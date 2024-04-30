class tree:
    def __init__(self,left=None,right=None):
        self.right=right
        self.left=left
    def child(self):
        return(self.left,self.right)
def huffmancodetree(node,left=True,binstring=''):
    if type(node) is str:
        return{node:binstring}
    (l,r)=node.child()
    codes={}
    codes.update(huffmancodetree(l,True,binstring+'0'))
    codes.update(huffmancodetree(r,False,binstring+'1'))
    return codes


msg='BCCABBDDAECCBBAEDDCC'
d={}
char=[]
freq=[]
for i in msg:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
sdict=sorted(d.items(),key=lambda x:x[1])
for i,j in sdict:
    char.append(i)
    freq.append(j)
print(char)
print(freq)
temp=sdict
while len(temp)>1:
    (key1,c1)=temp[0]
    (key2,c2)=temp[1]
    temp=temp[2:]
    node=tree(key1,key2)
    temp.append((node,c1+c2))
    temp=sorted(temp,key=lambda x:x[1])
huffmancode=huffmancodetree(temp[0][0])
for (char,frequency) in sdict:
    print((char,huffmancode[char]))



