#!/bin/bash
printf "%s\n" "Converting Markdown to PDF"
pandoc \
  --standalone \
  --template=eisvogel \
  --citeproc \
  --listings \
  keyinfo.yaml \
  report_template_week_1.md \
  -o James_Murray_13879046_week1.pdf

printf "%s\n" "Finished"
