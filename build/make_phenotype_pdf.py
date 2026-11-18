from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, PageBreak
from PIL import Image as PILImage

S=getSampleStyleSheet()
TITLE=ParagraphStyle('T',parent=S['Title'],fontSize=14,spaceAfter=2)
SUB=ParagraphStyle('S',parent=S['Normal'],fontSize=9.5,textColor=colors.HexColor('#444444'),spaceAfter=12)
CAP=ParagraphStyle('C',parent=S['Normal'],fontSize=9,leading=12,spaceBefore=4,spaceAfter=14)

D="/tmp/claude-0/-home-user-Task11/6125c45e-3071-50fa-9cb2-fcf0093300e6/scratchpad/figs2_out"
PANELS=[
 ("tumour_growth_screen.png",
  "Tumour volume over time following subcutaneous implantation of the library-containing populations, "
  "for the backgrounds and treatment arms indicated."),
 ("lectin_signal.png",
  "Relative lectin signal measured by flow cytometry in two cell lines, for cells carrying a non-targeting "
  "sgRNA or an MGAT1-targeting sgRNA. Left: PHA-L. Right: GNA."),
 ("coculture_viability.png",
  "Relative viability of tumour cells carrying the indicated sgRNAs after co-culture with antigen-matched "
  "CD8<sup>+</sup> T cells, at the effector-to-target ratios shown."),
 ("tumour_growth_adoptive.png",
  "Tumour volume over time following adoptive transfer of the indicated numbers of CD8<sup>+</sup> T cells."),
 ("rescue_lectin_and_viability.png",
  "Surface lectin signal and relative viability across the cDNA construct panel, in the two sgRNA backgrounds "
  "indicated. Viability was measured with no T cells and with T cells from two donors."),
 ("rescue_blot_and_histograms.png",
  "Immunoblot and flow cytometry histograms for the engineered construct panel."),
 ("rescue_tumour_growth.png",
  "Tumour volume over time for tumours carrying the cDNA constructs indicated."),
 ("supp_tumour_growth.png",
  "Tumour volume over time, additional cohorts."),
 ("supp_target_expression_and_killing_1.png",
  "Target antigen expression across cell lines."),
 ("supp_target_expression_and_killing_2.png",
  "Viability after co-culture with CD8<sup>+</sup> T cells, with and without the antigen-specific receptor."),
 ("supp_rescue_validation.png",
  "Immunoblot for the engineered lines, and a schematic of the engineering steps."),
]
AW=(297-2*18)*mm; AH=(210-2*16)*mm-34*mm
F=[Paragraph("Antera Therapeutics",TITLE),
   Paragraph("MGAT1 programme &mdash; cellular and in vivo phenotype records.",SUB)]
for i,(fn,cap) in enumerate(PANELS):
    p=f"{D}/{fn}"; w,h=PILImage.open(p).size
    s=min(AW/w,AH/h)
    F.append(Image(p,width=w*s,height=h*s)); F.append(Paragraph(cap,CAP))
    if i<len(PANELS)-1: F.append(PageBreak())
SimpleDocTemplate("/home/user/Task11/room/phenotype_figures.pdf",pagesize=landscape(A4),
   leftMargin=18*mm,rightMargin=18*mm,topMargin=16*mm,bottomMargin=16*mm,
   title="Cellular and in vivo phenotype records",author="").build(F)
print("built")
