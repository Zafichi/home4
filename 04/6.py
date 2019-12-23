from collections import Counter

fil = open('1112.txt')
st = fil.read()
lst = st.split()
print(Counter(lst).most_common(10))
