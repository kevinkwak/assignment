from operator import index
import sys

infile = open(sys.argv[1], "r")
outfile = open(sys.argv[2], "w")

lines = infile.read().splitlines()
for i in range(1, len(lines)):
    if "?" in lines[i]:
        print("Found ? (MUX)")
        value = lines[i][lines[i].index("=")+1:]
        value = value.replace(" ", "")
        sel = value[:value.index("?")]
        input1 = value[value.index("?")+1:value.index(":")]
        input2 = value[value.index(":")+1:value.index(";")]
        print("Select: ", sel)
        print("Input 1: ", input1)
        print("Input 2: ", input2)
        print("Original: ", lines[i])
        lines[i] = lines[i].replace(lines[i][lines[i].index("=")+2:], " (~(" + sel + ") & " + input2 + ") | (" + sel + " & " + input1 + ");")
        print("Modified: ", lines[i])
    if "|" in lines[i]:
        print("Found |")
        value = lines[i][lines[i].index("=")+1:]
        value = value.replace(" ", "")
        input1 = value[:value.index("|")]
        input2 = value[value.index("|")+1:value.index(";")]
        print("Input 1: ", input1)
        print("Input 2: ", input2)
        print("Original: ", lines[i])
        lines[i] = lines[i].replace(lines[i][lines[i].index("=")+2:], "~(~" + input1 + "&~" + input2 + ");")
        print("Modified: ", lines[i])

for i in range(1, len(lines)):
    outfile.write(lines[i] + "\n")
 


infile.close()
outfile.close()

