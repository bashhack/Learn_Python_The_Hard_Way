from sys import argv

script, from_file, to_file = argv

open(to_file, "w").write(open(from_file).read())
print "File copied from %s to %s" % (from_file, to_file)
