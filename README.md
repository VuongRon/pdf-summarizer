# pdf-summarizer

WIP PDF summarizer intended to summarize research papers. It has not been tested on review papers.

Upon executing the python script, the user is prompted to select a pdf file to summarize. The script uses tika to get the plaintext from the pdf file, then uses some basic regex to remove lines that contain common non-sentence keywords that would be found in the headers/footers of a page, the references, or the document information. Subsequently, blank lines are removed and a reduced file 'output.txt' is written to the folder containing the python script. Then the script uses the LSASummarizer included in sumy to summarize the reduced file and writes a file 'final.txt' to the folder containing the python script.

'final.txt' contains the output from the LSASummarizer and gives a 15 sentence summary of the reduced file.

To Do:
- Reduce the initial text file further to avoid figure headings, authorship, chart data, etc.
- Separate paper into sections (Methods, Results, Discussion) and create separate files for each, to obtain summaries of each heading instead of the entire paper
