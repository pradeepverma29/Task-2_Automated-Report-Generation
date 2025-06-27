import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# Load and analyze the data
df = pd.read_excel("data.csv.xlsx")



# Basic analysis
total_revenue = df["Revenue"].sum()
total_units = df["Units Sold"].sum()
category_stats = df.groupby("Category").agg({
    "Units Sold": "sum",
    "Revenue": "sum"
})

# Create PDF report
report_file = "sales_report.pdf"
c = canvas.Canvas(report_file, pagesize=A4)
width, height = A4

# Title
c.setFont("Helvetica-Bold", 16)
c.drawString(1 * inch, height - 1 * inch, "Sales Summary Report")

# Summary stats
c.setFont("Helvetica", 12)
c.drawString(1 * inch, height - 1.5 * inch, f"Total Revenue: ₹{total_revenue}")
c.drawString(1 * inch, height - 1.8 * inch, f"Total Units Sold: {total_units}")

# Category-wise stats
c.drawString(1 * inch, height - 2.2 * inch, "Category-wise Breakdown:")
y = height - 2.5 * inch
for idx, row in category_stats.iterrows():
    c.drawString(1.2 * inch, y, f"{idx}: {row['Units Sold']} units, ₹{row['Revenue']}")
    y -= 0.3 * inch

# Footer
c.setFont("Helvetica-Oblique", 10)
c.drawString(1 * inch, 0.75 * inch, "Report generated using Python and ReportLab.")

# Save
c.save()

print(f"PDF report '{report_file}' has been generated.")
