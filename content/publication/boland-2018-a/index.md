---
title: Combining Progressive Hedging with a Frank--Wolfe Method to Compute Lagrangian
  Dual Bounds in Stochastic Mixed-Integer Programming
# If group member, use folder name in /content/authors
authors:
  - Natashia Boland
  - Jeffrey Christiansen
  - Brian Dandurand
  - Andrew Eberhard
  - Jeff Linderoth
  - James Luedtke
  - g_fabricio-oliveira
date: 2020-08-27
doi: 10.1137/16M1076290

# Schedule page publish date (NOT publication's date).
publishDate: 2017-01-01

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# Publication name and optional abbreviated publication name. Notice * * on title. # Publication name and optional abbreviated publication name. Quote marks needed for Markdown typesetting
publication: '*SIAM Journal of Optimization*'
publication_short: ''

abstract: We present a new primal-dual algorithm for computing the value of the Lagrangian
  dual of a stochastic mixed-integer program (SMIP) formed by relaxing its nonanticipativity
  constraints. This dual is widely used in decomposition methods for the solution
  of SMIPs. The algorithm relies on the well-known progressive hedging method, but
  unlike previous progressive hedging approaches for SMIP, our algorithm can be shown
  to converge to the optimal Lagrangian dual value. The key improvement in the new
  algorithm is an inner loop of optimized linearization steps, similar to those taken
  in the classical Frank–Wolfe method. Numerical results demonstrate that our new
  algorithm empirically outperforms the standard implementation of progressive hedging
  for obtaining bounds in SMIP.

# Summary. An optional shortened abstract.
summary: 

# Not in use. Could be used for keywords 
tags:
  
featured: false

# links:
url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Categories
#  These asociate the publications with the icons representing reearch topics and application areas
categories: [Efficient formulation and solution methods]

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
  
 # forbid social media icons appearance
share: false
---