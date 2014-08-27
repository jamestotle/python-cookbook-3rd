def dedupe1(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print (list(dedupe(a, key=lambda d: (d['x'],d['y']))))

with open(somefile,'r') as f:
    for line in dedupe(f):
        print (line,end='')