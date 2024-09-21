import PyPDF2
import os

def pdf_to_text(pdf_files, output_file):
    # Open a new text file for writing the combined content
    with open(output_file, 'w', encoding='utf-8') as txt_file:
        for pdf_file in pdf_files:
            # Open each PDF file in binary read mode
            with open(pdf_file, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                # Loop through all the pages in the PDF
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    # Extract text from the page and write it to the text file
                    txt_file.write(page.extract_text())
                    txt_file.write('\n')  # Add newline after each page

    print(f"All PDF files have been merged into {output_file}")

# Example usage
pdf_files = ['C:\\Users\\4a Freeboard\\Documents\\WEKLY REPORT 4.docx.pdf',
             'C:\\Users\\4a Freeboard\\Documents\\Scenarios - Sheet1.pdf', 
             'C:\\Users\\4a Freeboard\\Documents\\LeaveForm_TI-0131.pdf' ]
output_file = 'combined_output1.txt'

pdf_to_text(pdf_files, output_file)
