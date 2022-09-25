from docx2pdf import convert

def Word2PDF(filename):
    filename = filename + ".docx"
    return convert(filename)

Word2PDF("lab")