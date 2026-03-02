from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import BaseDocTemplate, Frame, Paragraph, Spacer, Image, PageTemplate, FrameBreak
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_JUSTIFY, TA_CENTER

# --- CONFIGURATION ---
OUTPUT_FILENAME = "Cristian_Ionel_Resume.pdf"
PHOTO_FILENAME = "cristian_portrait.jpg"

# Modern Color Palette (Slate & Sky Theme)
COLOR_SIDEBAR_BG = colors.HexColor("#1e293b")   # Dark Slate (Slate 800)
COLOR_SIDEBAR_TEXT = colors.HexColor("#f1f5f9") # Off-white (Slate 100)
COLOR_SIDEBAR_HEADER = colors.HexColor("#38bdf8") # Light Sky Blue (Sky 400)
COLOR_MAIN_TEXT = colors.HexColor("#334155")    # Slate 700
COLOR_NAME = colors.HexColor("#0f172a")         # Darkest Slate (Slate 900)
COLOR_ACCENT = colors.HexColor("#0284c7")       # Sky 600
COLOR_JOB_META = colors.HexColor("#64748b")     # Slate 500

# --- CANVAS DRAWING (Backgrounds) ---
def draw_background(canvas, doc):
    """Draws the sidebar background on every page."""
    canvas.saveState()
    # Draw Left Sidebar Rectangle
    canvas.setFillColor(COLOR_SIDEBAR_BG)
    # Sidebar width: 2.3 inches (Reduced slightly)
    canvas.rect(0, 0, 2.3*inch, A4[1], fill=1, stroke=0)
    canvas.restoreState()

# --- STYLES ---
styles = getSampleStyleSheet()

# Sidebar Styles (Reduced sizes)
style_sb_header = ParagraphStyle('SB_Header', parent=styles['Normal'], fontSize=10, leading=12, 
                                 textColor=COLOR_SIDEBAR_HEADER, fontName='Helvetica-Bold', spaceBefore=10, spaceAfter=4, textTransform='uppercase')
style_sb_text = ParagraphStyle('SB_Text', parent=styles['Normal'], fontSize=8, leading=10, 
                               textColor=COLOR_SIDEBAR_TEXT, fontName='Helvetica')
style_sb_bold = ParagraphStyle('SB_Bold', parent=styles['Normal'], fontSize=8, leading=10, 
                               textColor=colors.white, fontName='Helvetica-Bold')

# Main Content Styles (Reduced sizes)
style_name = ParagraphStyle('Name', parent=styles['Normal'], fontSize=22, leading=26, 
                            textColor=COLOR_NAME, fontName='Helvetica-Bold', spaceAfter=4)
style_role = ParagraphStyle('Role', parent=styles['Normal'], fontSize=14, leading=14, 
                            textColor=COLOR_SIDEBAR_BG, fontName='Helvetica-Bold', spaceAfter=16)
style_section = ParagraphStyle('Section', parent=styles['Normal'], fontSize=10, leading=12, 
                               textColor=COLOR_ACCENT, fontName='Helvetica-Bold', spaceBefore=14, spaceAfter=4, textTransform='uppercase')

# Experience Styles
style_job_header = ParagraphStyle('JobHeader', parent=styles['Normal'], fontSize=9, leading=11, 
                                  textColor=colors.black, fontName='Helvetica-Bold', spaceBefore=8, spaceAfter=2)
style_job_sub = ParagraphStyle('JobSub', parent=styles['Normal'], fontSize=8.5, leading=11, 
                               textColor=COLOR_JOB_META, fontName='Helvetica-Oblique', spaceAfter=3)
style_body = ParagraphStyle('Body', parent=styles['Normal'], fontSize=8.5, leading=11, 
                            textColor=COLOR_MAIN_TEXT, fontName='Helvetica', alignment=TA_LEFT)
style_bullet = ParagraphStyle('Bullet', parent=style_body, leftIndent=0, firstLineIndent=0, spaceAfter=1)
style_sub_bullet = ParagraphStyle('SubBullet', parent=style_body, leftIndent=12, firstLineIndent=0, spaceAfter=1)

# --- CONTENT GENERATION ---
def create_resume():
    # Adjusted margins for single page fit
    doc = BaseDocTemplate(OUTPUT_FILENAME, pagesize=A4, rightMargin=0.4*inch, leftMargin=0, topMargin=0, bottomMargin=0)
    
    # Frames define the areas where text flows
    # Sidebar Frame (Left)
    frame_sidebar = Frame(x1=0.2*inch, y1=0.2*inch, width=1.9*inch, height=11.3*inch, id='col1', showBoundary=0)
    # Main Content Frame (Right) - Wider
    frame_main = Frame(x1=2.5*inch, y1=0.3*inch, width=5.4*inch, height=11.0*inch, id='col2', showBoundary=0)
    
    doc.addPageTemplates([PageTemplate(id='TwoCol', frames=[frame_sidebar, frame_main], onPage=draw_background)])

    story = []

    # === LEFT COLUMN (SIDEBAR) ===
    
    # 1. Photo
    try:
        im = Image(PHOTO_FILENAME, width=1.6*inch, height=1.6*inch)
        story.append(im)
    except:
        story.append(Spacer(1, 1.6*inch)) 
    
    story.append(Spacer(1, 0.3*inch))

    # 2. Contact
    story.append(Paragraph("CONTACT", style_sb_header))
    story.append(Paragraph("Brno, Czech Republic", style_sb_bold))
    story.append(Spacer(1, 4))
    
    contact_info = [
        "+420 608 326 387",
        "cristian.ionel@gmail.com",
        "linkedin.com/in/cristianionel",
        "github.com/waylay"
    ]
    for item in contact_info:
        story.append(Paragraph(item, style_sb_text))
        story.append(Spacer(1, 2))
    
    story.append(Spacer(1, 0.2*inch))

    # 3. Skills
    story.append(Paragraph("TECHNICAL SKILLS", style_sb_header))
    
    def add_skill_section(title, items):
        story.append(Paragraph(title, style_sb_bold))
        story.append(Paragraph(items, style_sb_text))
        story.append(Spacer(1, 6))

    add_skill_section("AI & Automation", "AI Agents, LLM APIs, MCP, Prompt Engineering, Vector Databases, Embeddings, RAG, Workflow Automation")
    add_skill_section("Backend", "PHP 8+, Laravel (Nova, Spark, Telescope, Livewire), Symfony, MySQL, Redis, RESTful APIs")
    add_skill_section("Frontend", "JavaScript (Vue.js, Alpine.js, TypeScript, jQuery), Tailwind CSS, Bootstrap, Sass")
    add_skill_section("DevOps & Tools", "AWS, Linux, Apache/Nginx, Docker, Git, CI/CD, Web Security, Performance Optimization")
    add_skill_section("CMS", "WordPress (Themes, Plugins, WooCommerce), Drupal (Modules, Themes)")

    story.append(Spacer(1, 0.2*inch))

    # 4. Education
    story.append(Paragraph("EDUCATION", style_sb_header))
    story.append(Paragraph("Bachelor's Degree", style_sb_bold))
    story.append(Paragraph("Computer Science", style_sb_text))
    story.append(Paragraph("Gheorghe Asachi Technical University of Iasi", style_sb_text))
    story.append(Paragraph("2005 – 2009", style_sb_text))

    story.append(Spacer(1, 0.2*inch))

    # 5. Languages
    story.append(Paragraph("LANGUAGES", style_sb_header))
    story.append(Paragraph("English: Proficient", style_sb_text))
    story.append(Paragraph("Romanian: Native", style_sb_text))

    # Jump to Next Frame (Right Column)
    story.append(FrameBreak())

    # === RIGHT COLUMN (MAIN) ===

    # 1. Name & Title
    story.append(Paragraph("CRISTIAN IONEL", style_name))
    story.append(Paragraph("Senior Full-Stack Web Developer", style_role))
    
    # 2. Summary
    story.append(Paragraph("PROFESSIONAL SUMMARY", style_section))
    summary_text = """
    <b>Senior Full-Stack Web Developer</b> with over 15 years of experience delivering web solutions. Expert in the Laravel ecosystem, specialized in building multi-tenant SaaS architectures, optimizing legacy codebases, and managing end-to-end DevOps pipelines on AWS. Proven track record of managing complex technical projects for enterprise clients, including <b>Ikea, Goodyear, Caterpillar,</b> and <b>Suzuki</b>, alongside core product development. Committed to code quality and AI-driven efficiency, with a comprehensive understanding of the full web development lifecycle—from concept to launch and sales.
    """
    story.append(Paragraph(summary_text, style_body))

    # 3. Experience
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", style_section))

    def add_job_entry(title, company, date, location, bullets):
        # Combined Title and Company
        header_text = f"{title} | {company}"
        story.append(Paragraph(header_text, style_job_header))
        
        # Location and Date on next line with different style
        sub_text = f"{location} | {date}"
        story.append(Paragraph(sub_text, style_job_sub))
        
        for b in bullets:
            if isinstance(b, list):
                for sub in b:
                    story.append(Paragraph(f"- {sub}", style_sub_bullet))
            else:
                story.append(Paragraph(f"• {b}", style_bullet))
        story.append(Spacer(1, 6)) # Reduced spacer between jobs

    # Monster
    add_job_entry("Senior Laravel Developer", "Monster", "01/2021 – 09/2025", "Brno, Czech Republic", [
        "<b>SaaS Architecture & Development:</b> Conceptualized, planned, and led the full-stack development of a <i>Career Website Builder</i>, a multi-tenant SaaS product allowing clients to generate personalized career sites.",
        ["<i>Tech Stack:</i> Built using <b>Laravel</b>, <b>Nova</b>, and <b>Vue.js</b>, hosted on <b>AWS</b> with <b>Redis</b> caching and tenant-separated databases.",
         "<i>Business Impact:</i> Pitched the Proof of Concept to executive management, secured approval, and launched to paying customers within 12 months."],
        "<b>Product Development:</b> Enhanced the technical stack (Laravel, Tailwind, JavaScript, PHP, MySQL, Redis, AWS, TDD, etc.) to improve performance and scalability.",
        "<b>Web Development:</b> Developed full-stack web applications for high-profile clients, including <i>Ikea, Goodyear, Caterpillar,</i> and <i>Suzuki</i>.",
        "<b>Team Leadership:</b> Mentored junior developers, created comprehensive documentation, and recorded training video libraries to standardize onboarding.",
        "<b>DevOps & Optimization:</b> Maintained core infrastructure, updated solutions, and focused heavily on performance optimization for existing commercial products."
    ])

    # Upwork
    add_job_entry("Full-Stack Developer", "Upwork", "09/2015 – 12/2020", "Brno, Czech Republic", [
        "<b>Custom Web Solutions:</b> Delivered specialized Laravel and WordPress solutions, ranging from brochure sites to full-scale CMS web applications like:",
        ["Inventory Management in Laravel for a truck parts supplier, eliminating manual data entry.",
        "Ski tournament system in Laravel for a Canadian ski club, allowing easy scoring and results.",
        "Kitchen parts supplier website in WordPress, allowing for easy product management.",
        "Snooker tournament management system in WordPress for a club in the UK."],
        "<b>Web Development:</b> Created Laravel and WordPress web applications for clients.",
        "<b>Security & Performance:</b> Specialized in hardening web security (HTTPS, CSRF, XSS, SQL injection, validation, etc.) and optimizing speed/SEO for high-traffic environments.",
        "<b>DevOps Management:</b> Planned, installed, and configured deployment systems using Linux, Apache, Nginx, and Git workflows."
    ])

    # Newbird
    add_job_entry("Senior Web Developer", "Newbird", "11/2013 – 08/2015", "Brno, Czech Republic", [
        "Developed full-stack web applications, ecommerce sites, and custom scripts for clients in the United States. Projects included: theme parks, nursing homes, advertising agencies, law firms, etc.",
    ])

    # Envato
    add_job_entry("Exclusive Author & Plugin Developer", "Envato (CodeCanyon)", "03/2013 – 06/2014", "Brno, Czech Republic", [
        "<b>Product Development:</b> Created the <i>Taxonomies Filter Widget</i>, a robust WordPress plugin for handling custom fields and taxonomy filtering.",
        "<b>Commercial Success:</b> Achieved 'Weekly Top Seller' status and generated over <b>2,000 verified sales</b>, handling all customer support and feature updates personally."
    ])

    # AT&T
    add_job_entry("Network Engineer", "AT&amp;T", "02/2012 – 12/2013", "Brno, Czech Republic", [
        "Implemented, maintained, and troubleshooted company's network and devices, ensuring security, reliability, and performance; configured routers, switches, firewalls, protocols, and VPNs."
    ])

    doc.build(story)
    print(f"Resume generated: {OUTPUT_FILENAME}")

if __name__ == "__main__":
    create_resume()
