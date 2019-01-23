def get_file_contents(filename):
    with open(filename) as w:
        return w.read().strip().split()
