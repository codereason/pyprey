# import sys
# while True:
#     inStr = sys.stdin.readline()
#     if not inStr:
#         break
#     a = inStr.split('\n')[0].split(' ')
#     # ans = list()
#     # l = len(a)
#     # for k in range(l):
#     #     ans.append(a[l-k-1])
#     # s = ' '.join(ans)
#     print(' '.join(a[::-1]))
#
# except:
#     pass
# ans = 0
# a,b = letter[1],letter[2]
# len1,len2=len(a),len(b)
# for i in range(0,len1-1):
#   for j in range(1,len2):
#     if(a[i]==b[j] and a[i+1]==b[j-1]):
#       ans+=1
# print(2**ans)
#
#
# N = int(input())
# for i in range(N):
#     a1 = input().strip()
#     a2 = input().strip()
#     ans=0
#     len1=len(a1)
#     for i in range(1,len1):
#       for j in range(1,len1):
#         if(a1[i]==a2[j-1] and a1[i-1]==a2[j]):
#           ans+=1
#     print(2**ans)
