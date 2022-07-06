#1등 코드 : 스택 없이 푸는게 훨 간편한데 왜 이걸 스택으로 풀어보라하셨을까...ㅠ
a=input() #ex) <open>gat<close>
b=a.replace('>','<').split('<') #>를 <로 바꾸고 <을 기준으로 나누기 #ex) ['', 'open', 'gat', 'close', '']
s=""
for i in range(len(b)):
  if i%2: #ex) ['', 'open', 'gat', 'close', '']에서 짝수번째 인덱스에 있는 것들이 <>안에 있던 것. 그러니까 그냥 붙여줌
      s+='<'+b[i]+'>'
  else: #홀수 번째 인덱스에 있는 것들은 단어이므로 단어 뒤집어줌!
    c=b[i].split()
    s+=' '.join([d[::-1] for d in c]) #만약에 <ab>abc def<cd>일 경우 abc def가 c이고 abc, def에 대해 각각 뒤집고 띄어쓰기해야되므로!
print(s)
"""내가 푼 스택 이용 풀이 : 스택 이용해서 풀라길래 이렇게 풀었는데 그냥
import sys
s = list(sys.stdin.readline().rstrip())

def popall(a,b):
  for _ in range(len(a)):
    b.append(a.pop())

tag = False
rev = []
stack = []

for w in s:
  if w=='<':
    popall(stack, rev)
    rev.append('<')
    tag=True
  elif w=='>':
    rev.append('>')
    tag=False
  elif tag:
    rev.append(w)
  else:
    if w != ' ':
      stack.append(w)
    else:
      popall(stack, rev)
      rev.append(w)
popall(stack, rev)

print(''.join(rev))
"""