---
title: 'A novel exact formulation for parallel machine scheduling problems'
# If group member, use folder name in /content/authors
authors:
  - p_luana-carrilho
  - g_fabricio-oliveira
  - Silvio Hamacher

date: 2024-05-01
doi: 10.1016/j.compchemeng.2024.108649

# Schedule page publish date (NOT publication's date).
publishDate: 2017-01-01

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# Publication name and optional abbreviated publication name. Notice * * on title. # Publication name and optional abbreviated publication name. Quote marks needed for Markdown typesetting
publication: '*Computers and Chemical Engineering*'
publication_short: 'CACE'

abstract: Machine scheduling is one of the most studied problems due to its technical challenges and prevalence in real life. In the literature, continuous- and discrete-time formulations are the two most known formulations for scheduling problems. However, continuous-time formulations often suffer from weak linear relaxations, while discrete-time formulations struggle with large numbers of variables. In contrast, the bucket-indexed formulation is an alternative that mitigates both issues by working with partial time discretization. We propose a mixed-integer linear programming model based on a bucket-indexed formulation to solve a nonpreemptive scheduling problem of identical parallel machines considering release dates, deadlines, precedence, eligibility, and machine availability constraints. We evaluate the proposed formulation against real-world instances comprising more than 400 jobs and 100 machines, comparing its performance against equivalent continuous- and discrete-time formulations. Remarkably, our formulation can be solved to optimality for all instances, outperforming both continuous- and discrete-time formulations.

# Summary. An optional shortened abstract.
summary:  

# Not in use. Could be used for keywords 
tags:
  
featured: false

# links:
url_pdf: 'https://doi.org/10.1016/j.compchemeng.2024.108649'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Categories
#  These asociate the publications with the icons representing reearch topics and application areas
categories: [Production and operations planning]

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false
  
# remove social media icons 
share: false
---