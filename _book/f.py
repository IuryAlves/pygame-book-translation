# coding: utf-8

with open("indice.md", "r") as file:
	with open("SUMMARY.md", "w") as out:
		for line in file.readlines():
			if "+" in line:
				line = line.replace("+", "* [")
				line = line.strip('\n')
				line += "]" + '\n'
			out.write(line)
