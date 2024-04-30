a=input().split()
b = {}
k= int(input())
# a = ["watermelon", "girl", "boy", "color"]
for element in a:
    b[len(element)] = element
print(b)
sorted_dict=dict(sorted(b.items(),key=lambda a:a[1],reverse=True))
print(sorted_dict)
for i in range(k):
    print(sorted)

# k= int(input())
# b=sorted(a[n],key= lambda a:a[i], reverse=True)
# print(b)
# for i in range(k):
#     print(b[i])
#
# print(a)