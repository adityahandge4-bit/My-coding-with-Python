def sum(*args):
    print(args)   # This will always returns the tuple
    total=0
    for items in args:
        total+=items
    return total
print(sum(12,345,6789,68790))