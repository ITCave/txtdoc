#txtdoc
General purpose library for creating and formating of plain text documents

##Basic usage 

````
import TxtDoc from txtdoc.document

doc = TxtDoc(width=50)
doc.add_run("This is a paragraph", align='center')
doc.br()  # Line break
doc.hr()  # Draws a line
doc.hr("Line with optional text")

# To string
to_sting = doc.render()
# To file
doc.save(".\file.txt")

````

##Output