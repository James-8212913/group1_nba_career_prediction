#!/bin/bash
printf "%s\n" "Converting Markdown to PDF"
pandoc \
  --standalone \
  --template=eisvogel \
  --citeproc \
  --listings \
  keyinfo.yaml \
  report_template_final.md \
  -o James_Murray_13879046_final_report.pdf

printf "%s\n" "Finished"
