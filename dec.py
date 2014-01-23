import venusian

found = []

def dec(wrapped):
    def callback(scanner, name, obj):
        found.append(wrapped)
    venusian.attach(wrapped, callback)
    return wrapped
