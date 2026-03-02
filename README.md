# Resume PDF Generator

This project contains a Python script that generates a one-page resume PDF using a two-column layout.

## What this script does

- Builds `Cristian_Ionel_Resume.pdf` from hardcoded resume content in `generate_resume.py`.
- Uses `reportlab` to render:
  - a dark left sidebar (photo, contact, skills, education, languages)
  - a main content area on the right (name, summary, work experience)
- Applies custom typography, spacing, and colors for a modern printable layout.

## How it works

The script is organized into three main parts:

1. **Configuration**
   - Output file name and photo file name are defined at the top of the script.
   - Color constants define the visual theme.

2. **Layout and styling**
   - `draw_background(canvas, doc)` paints the sidebar background on each page.
   - ReportLab `ParagraphStyle` objects define text styles for headers, body text, and bullets.
   - Two ReportLab `Frame`s create the left and right columns.

3. **Content generation**
   - `create_resume()` builds a `story` list of flowable elements (`Paragraph`, `Image`, `Spacer`, `FrameBreak`).
   - Helper functions add skill groups and job entries in a structured way.
   - `doc.build(story)` writes the final PDF.

## Requirements

- Python 3.10+
- Dependencies listed in `requirements.txt`

## Setup

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

## Usage

Run the script from the project directory:

```bash
.venv/bin/python generate_resume.py
```

On success, it prints:

```text
Resume generated: Cristian_Ionel_Resume.pdf
```

## Input and output files

- **Input image:** `cristian_portrait.jpg`
- **Script:** `generate_resume.py`
- **Output PDF:** `Cristian_Ionel_Resume.pdf`

## Customization

- Update content text directly in `generate_resume.py`.
- Change theme colors via the `COLOR_*` constants.
- Adjust layout widths/heights by modifying the two `Frame` definitions.
- Replace the portrait by swapping `cristian_portrait.jpg` (or changing `PHOTO_FILENAME`).

## Troubleshooting

- **`ModuleNotFoundError: No module named 'reportlab'`**
  - Make sure dependencies are installed in your virtual environment:
    - `.venv/bin/python -m pip install -r requirements.txt`
- **Image not shown in PDF**
  - Verify `cristian_portrait.jpg` exists in the same directory as the script.
