# Implement following string functions: replace(), count(), capitalize(), and join().

import string
s = "pnigma"
print(s)
s = s.replace("p","ee")
print(s)
print(s.count("e"))
print(s.capitalize())
seprator = "-"
seprator = seprator.join(s)
print(seprator)