from fpdf import FPDF
import datetime

class DRCGenerator(FPDF):
    def __init__(self):
        super().__init__()
        # כאן אנחנו טוענים את הפונט. וודא שהקובץ Assistant-Regular.ttf נמצא בתיקייה!
        self.add_font('Assistant', '', 'Assistant-Regular.ttf', uni=True)
        self.set_auto_page_break(auto=True, margin=15)

    def header(self):
        self.set_font('Assistant', '', 20)
        self.cell(0, 10, 'Digital Registry Center - DRC', ln=True, align='R')
        self.set_draw_color(0, 50, 100)
        self.line(10, 25, 200, 25)

    def footer(self):
        self.set_y(-15)
        self.set_font('Assistant', '', 8)
        self.cell(0, 10, f'מסמך מונפק אוטומטית - {datetime.datetime.now().strftime("%d/%m/%Y")}', align='C')

    def generate(self, name, doc_type, doc_id):
        self.add_page()
        self.set_font('Assistant', '', 14)
        
        # כותרת המסמך
        self.cell(0, 15, doc_type, ln=True, align='C')
        
        # גוף המסמך
        self.set_font('Assistant', '', 12)
        self.cell(0, 10, f"אסמכתא: {doc_id}", ln=True, align='R')
        self.cell(0, 10, f"שם המוטב: {name}", ln=True, align='R')
        self.ln(10)
        self.multi_cell(0, 10, "הנ\"ל מאושר בזאת על ידי המרכז לרישום דיגיטלי (DRC) כפעיל במערכותינו.")
        
        filename = f"Document_{doc_id}.pdf"
        self.output(filename)
        return filename

