#!/bin/bash
printf "%s\n" "Converting Markdown to PDF"
pandoc \
  --standalone \
  --template=eisvogel \
  --citeproc \
  --listings \
  keyinfo.yaml \
  report_template_week_2.md \
  -o James_Murray_13879046_week2.pdf

printf "%s\n" "Finished"
