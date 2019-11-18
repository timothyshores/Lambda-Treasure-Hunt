with open('api.txt', 'r') as reader:
    # Read and print the entire file line by line
    # for line in reader:
    #     print(line, end='')
    key = reader.read().strip()

print(key)
