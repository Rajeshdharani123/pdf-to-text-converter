# PDF to Text Converter
This Python script converts the contents of multiple PDF files into a single text file. The script uses the PyPDF2 library to extract text from each page of the given PDF files and writes the combined text into one output file.

### Prerequisites
Before running the script, make sure you have the following installed:

    Python 3.x
    PyPDF2 library
    Install PyPDF2
You can install the PyPDF2 library using pip:

    pip install PyPDF2
### How to Use
Clone or download the script to your local machine.
Make sure you edit the list of PDF file paths in the script to include the full paths of the PDF files you want to merge.
Run the script using Python.
Example Usage
Place your PDF files in the appropriate location and update the pdf_files list with the full paths of your PDF files:

    pdf_files = [
    'C:\\Users\\4a Freeboard\\Documents\\WEKLY REPORT 4.docx.pdf',
    'C:\\Users\\4a Freeboard\\Documents\\Scenarios - Sheet1.pdf',
    'C:\\Users\\4a Freeboard\\Documents\\LeaveForm_TI-0131.pdf'
    ]
Then, specify the name of the output file:

    output_file = 'combined_output1.txt'
To run the script, use the following command:

    python pdf_converter.py
The output file will contain the combined text from all the specified PDF files.

### Example Output
The text from all the provided PDF files will be extracted and saved into *** combined_output1.txt ***.

### Troubleshooting
If the output file is empty or contains no data, check whether the PDF files are scanned documents. If they are, you may need to use an OCR library (e.g., pytesseract).
Ensure that the file paths are correct and that the PDF files exist at the specified locations.
Limitations
This script only works with text-based PDFs. If your PDFs are scanned images or contain complex formatting, the text extraction may not work as expected.
If you need to process scanned PDFs, you may want to look into using OCR tools such as pytesseract.
