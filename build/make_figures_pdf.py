from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from PIL import Image as PILImage

S = getSampleStyleSheet()
TITLE = ParagraphStyle('T', parent=S['Title'], fontSize=14, spaceAfter=2)
SUB   = ParagraphStyle('S', parent=S['Normal'], fontSize=9.5,
                       textColor=colors.HexColor('#444444'), spaceAfter=12)
CAP   = ParagraphStyle('C', parent=S['Normal'], fontSize=9, leading=12, spaceBefore=4, spaceAfter=14)

D = "/tmp/claude-0/-home-user-Task11/6125c45e-3071-50fa-9cb2-fcf0093300e6/scratchpad/figs_out"
PANELS = [
 ("doseresponse_series.png",
  "Enzyme inhibition dose&ndash;response for the screening hit and the synthesised series, measured in the "
  "UDP-Glo format described in the experimental records. Points are plotted with error bars as recorded."),
 ("doseresponse_acquired.png",
  "Enzyme inhibition dose&ndash;response and surface plasmon resonance for the two acquired compounds and for UDP. "
  "For each row: chemical structure, UDP-Glo dose&ndash;response, SPR sensorgrams, and SPR steady-state response "
  "against analyte concentration."),
 ("spr_ANT3744.png",
  "Surface plasmon resonance for ANT-3744. Upper row: sensorgrams and steady-state response against analyte "
  "concentration. Lower row: the same measurement performed with UDP present at 5000 &micro;M."),
 ("dsf_melt_curves.png",
  "Differential scanning fluorimetry melting curves and their first derivatives, for protein alone in 5% DMSO "
  "and in the presence of the ligands at the concentrations indicated."),
 ("ic50_vs_kd.png",
  "Enzyme inhibition potency plotted against surface plasmon resonance dissociation constant for compounds "
  "derived from the screening hit. The identity line is shown for reference."),
]

AVAIL_W = (297-2*18)*mm
AVAIL_H = (210-2*16)*mm - 34*mm

F = [Paragraph("Antera Therapeutics", TITLE),
     Paragraph("MGAT1 programme &mdash; biochemical and biophysical assay records.", SUB)]
for i,(fn,cap) in enumerate(PANELS):
    p = f"{D}/{fn}"
    w,h = PILImage.open(p).size
    scale = min(AVAIL_W/w, AVAIL_H/h)
    F.append(Image(p, width=w*scale, height=h*scale))
    F.append(Paragraph(cap, CAP))
    if i < len(PANELS)-1:
        F.append(PageBreak())

doc = SimpleDocTemplate("/home/user/Task11/room/assay_figures.pdf", pagesize=landscape(A4),
                        leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=16*mm,
                        title="Biochemical and biophysical assay records", author="")
doc.build(F)
print("built")
