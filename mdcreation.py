def creation(fileName):
  file = open("{}.md".format(fileName),"x")
  file.close()

def textCreation(fileName, title, sectionArray):
  file = open("{}.md".format(fileName), "a")
  file.write("# {}\n".format(title))
  for section in sectionArray:
    file.write("## {}\n".format(section[0]))
    file.write("{}\n".format(section[1]))