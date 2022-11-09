##############################
######### PDF MERGER #########
##############################
########### itsba2 ###########
##############################


##############################
# Before running the script
# install the package
##############################
# pip install PyPDF2
##############################

# import the merge function
from PyPDF2 import PdfMerger

# assign the merge function to a constant
merger = PdfMerger()

# list of pdf files
# should be in the working directory
# or provide full paths
pdfs = ['1.pdf', '2.pdf']

# loop over pdfs list
for pdf in pdfs:
    # append each pdf end-to-end
    merger.append(pdf)

# write merged pdfs to a final file
merger.write('merged.pdf')

# finalize merging
merger.close()