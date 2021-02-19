from fpdf import FPDF
from pdfrw import PdfReader, PdfWriter
pdf = FPDF()
starting_line1 = "                        This certificate of completion serves as a recognition that the recipient"
starting_line2 = "                                    has a strong understanding of the key elements of"
subject_line = "                          Advanced C++ for CPP Developers"
next_to_sub_line = "                                      and how they can be applied to business."
concluding_line1 = "                           Having Fulfilled all the requirements necessary to complete the"
concluding_line2 = "                                XYZ Certification Program, this certificate is awarded to:"
employee_name = "                                          ABCDEF         "
date_of_certification = "                                                          Dec-2020"
def initialise():
    global pdf
    pdf = FPDF('L', 'cm', 'A4')
    pdf.set_auto_page_break(0)
    pdf.set_draw_color(255, 127, 80)   #change colorcode
    pdf.set_fill_color(255, 255, 255)
    pdf.set_line_width(0.7)
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    #border
    pdf.cell(0, 17, '', 1, 1, '')

def header():
    """Defined Header"""
    pdf.set_xy(4, 2)
    pdf.image("Virat World.jpg", x=2, y=2, w=3, h=2)
    pdf.set_xy(17, 1.5)
    pdf.set_font('Arial', 'B', 18)
    pdf.set_text_color(0, 126, 175)
    pdf.set_xy(5.5, 5)
    pdf.cell(0, 1, '                           XYZ CERTIFICATION PROGRAM')

def actual_text(subject, empname):
    """Defined actual function"""
#    pass
    pdf.set_xy(6, 6.5)
    pdf.set_font('Arial', '', 12)
    pdf.set_text_color(0, 126, 175)
    pdf.cell(0, 0, starting_line1)
    pdf.set_xy(6, 7.28)
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 0, starting_line2)
    pdf.set_xy(7, 8.25)
    pdf.set_font('Arial', 'B', 15)
    pdf.cell(0, 0, subject)
    pdf.set_xy(7, 9.25)
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 0, next_to_sub_line)
    pdf.set_xy(6, 10)
    pdf.cell(0, 0, concluding_line1)
    pdf.set_xy(6, 10.75)
    pdf.cell(0, 0, concluding_line2)
    pdf.set_xy(8, 12)
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 0, empname)
    pdf.set_xy(7, 13)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 0, date_of_certification)
def footer():
    """Defined Footer of document"""
    pdf.set_xy(4, 14)
    pdf.image("download.png", w=3, h=2)
    pdf.set_font('Arial', 'B', 9)
    pdf.set_xy(4, 16.5)
    pdf.cell(0, 0, 'Virat Gupta')
    pdf.set_xy(4, 17)
    pdf.set_font('Arial', '', 8)
    pdf.cell(0, 0, 'Chief Engineering Officer')
    pdf.set_xy(23, 14)
    pdf.image("download.png", w=3, h=2)
    pdf.set_font('Arial', 'B', 9)
    pdf.set_xy(23.5, 16.5)
    pdf.cell(0, 0, 'Virat Gupta')
    pdf.set_xy(23.5, 17)
    pdf.set_font('Arial', '', 8)
    pdf.cell(0, 0, 'Vice President - HR')
    pdf.output('sample.pdf', 'F')

def main():
    """Main Function"""
    initialise()
    header()
    actual_text(subject_line, employee_name)
    footer()
if __name__ == "__main__":
    main()