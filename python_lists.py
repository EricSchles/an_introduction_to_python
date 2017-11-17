if __name__ == '__main__':
    listing = []    
    N = int(input())
    for i in range(N):
        operation = input()
        if "insert" in operation:
            _, i, e = operation.split()
            e = int(e)
            i = int(i)
            listing.insert(i, e)
        if "remove" in operation:
            _, e = operation.split()
            e = int(e)
            listing.remove(e)
        if "append" in operation:
            _, e = operation.split()
            e = int(e)
            listing.append(e)
        if "print" in operation:
            print(listing)
        if "sort" in operation:
            listing.sort()
        if "pop" in operation:
            listing.pop()
        if "reverse" in operation:
            listing.reverse()
