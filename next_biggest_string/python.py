def biggerIsGreater(w):
    n = len(w)
    if n<2:
        return 'no answer'
    for i in range(n-2, -1, -1):
        smallest = chr(123)
        index = n
        for j in range(i+1, n):
            if w[i] < w[j] and w[j] <= smallest:
                index = j
                print(w[i], w[j])
        if index < n:
            return w[0:i]+w[index]+''.join(sorted(w[i:index]+w[index+1:]))      
    return 'no answer'

input_file = open("input.txt", "r")
output_file = open("output.txt", "a")

for line in input_file:
    i = line.strip()
    output = biggerIsGreater(i)
    output_file.write(output+"\n")