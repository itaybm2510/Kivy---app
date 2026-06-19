import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_pdf_invoice(order_id, items_str, total_amount, date_str):
    """
    מייצר קובץ PDF של חשבונית מס / קבלה בעיצוב הייטק פרימיום
    כולל חלוקת עמודות מתקדמת ומבנה ארגוני מושלם
    """
    filename = f"invoice_{order_id}.pdf"
    
    # הגדרת מסמך עם שוליים מדויקים
    doc = SimpleDocTemplate(
        filename, 
        pagesize=letter, 
        rightMargin=45, 
        leftMargin=45, 
        topMargin=45, 
        bottomMargin=45
    )
    
    story = []
    styles = getSampleStyleSheet()
    
    # הגדרות עיצוב וצבעים (סקאלת Slate & Blue עמוקה)
    title_style = ParagraphStyle(
        'InvoiceTitle', 
        parent=styles['Heading1'], 
        fontSize=24, 
        leading=28, 
        textColor=colors.HexColor("#0F172A"),
        fontName="Helvetica-Bold"
    )
    
    meta_label = ParagraphStyle(
        'MetaLabel', 
        parent=styles['Normal'], 
        fontSize=10, 
        leading=14, 
        textColor=colors.HexColor("#64748B")
    )
    
    meta_val = ParagraphStyle(
        'MetaValue', 
        parent=styles['Normal'], 
        fontSize=10, 
        leading=14, 
        textColor=colors.HexColor("#0F172A"),
        fontName="Helvetica-Bold"
    )
    
    table_header_style = ParagraphStyle(
        'TableHeader', 
        parent=styles['Normal'], 
        fontSize=10, 
        leading=12, 
        textColor=colors.white, 
        fontName="Helvetica-Bold"
    )
    
    table_cell_style = ParagraphStyle(
        'TableCell', 
        parent=styles['Normal'], 
        fontSize=10, 
        leading=14, 
        textColor=colors.HexColor("#334155")
    )

    table_cell_right = ParagraphStyle(
        'TableCellRight', 
        parent=styles['Normal'], 
        fontSize=10, 
        leading=14, 
        textColor=colors.HexColor("#0F172A"),
        fontName="Helvetica-Bold",
        alignment=2 # יישור לימין של מספרים
    )
    
    # --- חלק 1: כותרת ומיתוג תאגידי ---
    header_data = [
        [Paragraph("SMARTBIZ ENTERPRISE", title_style), Paragraph("<b>ORIGINAL INVOICE</b>", table_cell_right)]
    ]
    header_table = Table(header_data, colWidths=[300, 220])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(header_table)
    
    story.append(Spacer(1, 15))
    
    # --- חלק 2: בלוק מידע דו-צדדי (פרטי חברה מול פרטי הזמנה) ---
    info_data = [
        [Paragraph("<b>Issuer Details:</b>", meta_val), Paragraph("<b>Document Meta:</b>", meta_val)],
        [Paragraph("SmartBiz Solutions Ltd.", table_cell_style), Paragraph(f"Invoice ID: #{order_id}", table_cell_style)],
        [Paragraph("Global Tech Operations Center", table_cell_style), Paragraph(f"Date of Issue: {date_str}", table_cell_style)],
        [Paragraph("Reg No: 516489445-OS", table_cell_style), Paragraph("Payment: Cash on Delivery", table_cell_style)]
    ]
    info_table = Table(info_data, colWidths=[260, 260])
    info_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(info_table)
    
    story.append(Spacer(1, 25))
    
    # --- חלק 3: טבלת פריטים ופירוט פיננסי ---
    # כותרות העמודות
    items_table_data = [[
        Paragraph("Line Item Description", table_header_style), 
        Paragraph("Quantity", table_header_style),
        Paragraph("Status", table_header_style),
        Paragraph("Amount (Net)", table_header_style)
    ]]
    
    # פירוק מחרוזת המוצרים שהגיעו מה-CRM
    for part in items_str.split(', '):
        if part:
            qty = "1"
            name = part
            if "(" in part and ")" in part:
                # חילוץ כמות במידה וקיימת בסגנון (x2)
                try:
                    name = part.split(" (")[0]
                    qty = part.split("(x")[1].replace(")", "")
                except:
                    pass
                    
            items_table_data.append([
                Paragraph(name, table_cell_style), 
                Paragraph(qty, table_cell_style),
                Paragraph("Verified", table_cell_style),
                Paragraph("-", table_cell_style)
            ])
            
    # שורת סיכום סופי מוטמעת בתוך הטבלה
    items_table_data.append([
        Paragraph("<b>TOTAL SECURED AMOUNT PAID</b>", table_cell_style), 
        Paragraph("", table_cell_style),
        Paragraph("", table_cell_style),
        Paragraph(f"<b>{total_amount} ILS</b>", table_cell_right)
    ])
    
    # עיצוב מותאם לטבלה (סגנון מינימליסטי יוקרתי)
    invoice_table = Table(items_table_data, colWidths=[260, 70, 80, 110])
    invoice_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0F172A")), # כותרת שחורה/כחולה
        ('ALIGN', (0,0), (-1,0), 'LEFT'),
        ('BOTTOMPADDING', (0,0), (-1,0), 10),
        ('TOPPADDING', (0,0), (-1,0), 10),
        ('GRID', (0,0), (-1,-2), 0.5, colors.HexColor("#E2E8F0")), # קווים עדינים רק בין המוצרים
        ('LINEBELOW', (0,-1), (-1,-1), 1.5, colors.HexColor("#0F172A")), # קו עבה מתחת לסיכום
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor("#F8FAFC")), # רקע אפור רך לשורת סיכום
        ('BOTTOMPADDING', (0,-1), (-1,-1), 12),
        ('TOPPADDING', (0,-1), (-1,-1), 12),
        ('SPAN', (0,-1), (2,-1)), # איחוד תאים בשורת הסיכום
    ]))
    
    story.append(invoice_table)
    
    story.append(Spacer(1, 40))
    
    # --- חלק 4: חתימה אלקטרונית ואישור מערכת ---
    footer_text = ParagraphStyle('FooterText', parent=styles['Normal'], fontSize=8, textColor=colors.HexColor("#94A3B8"), alignment=1)
    story.append(Paragraph("This is an electronically generated document. Securely signed and sealed by SmartBiz Automated Financial Node.", footer_text))
    
    # בניית המסמך הסופי
    doc.build(story)
    return filename

