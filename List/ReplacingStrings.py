filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for files in range(len(filenames)):
    if "hpp" in filenames[files][:-3]:
        newfilenames.append(filenames[files][:-2])
    else:
        newfilenames.append(filenames[files])

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
