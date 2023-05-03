---
title: The p-Lagrangian relaxation for separable nonconvex MIQCQP problems
# If group member, use folder name in /content/authors
authors:
  - Tiago Andrade
  - g_nikita-belyak
  - Andrew Eberhard
  - Silvio Hamacher
  - g_fabricio-oliveira
date: 2022-02-22
doi: 10.1007/s10898-022-01138-y

# Schedule page publish date (NOT publication's date).
publishDate: 2017-01-01

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# Publication name and optional abbreviated publication name. Notice * * on title
publication: '*Journal of Global Optimization*'
publication_short: ''

abstract: This paper presents a novel technique to compute Lagrangian bounds for nonconvex mixed-integer quadratically constrained quadratic programming problems presenting a separable structure (i.e., a separable problems) such as those arising in deterministic equivalent representations of two-stage stochastic programming problems. In general, the nonconvex nature of these models still poses a challenge to the available solvers, which do not consistently perform well for larger-scale instances. Therefore, we propose an appealing alternative algorithm that allows for overcoming computational performance issues. Our novel technique, named the p-Lagrangian decomposition, is a decomposition method that combines Lagrangian decomposition with mixed-integer programming-based relaxations. These relaxations are obtained using the reformulated normalised multiparametric disaggregation technique and can be made arbitrarily precise by means of a precision parameter p. We provide a technical analysis showing the convergent behaviour of the approach as the approximation is made increasingly precise. We observe that the proposed method presents significant reductions in computational time when compared with a previously proposed techniques in the literature and the direct employment of a commercial solver. Moreover, our computational experiments show that the employment of a simple heuristic can recover solutions with small duality gaps.

# Summary. An optional shortened abstract.
summary: ''

# Not in use. Could be used for keywords 
tags:
  
featured: false

# links:
url_pdf:
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Categories
#  These asociate the publications with the icons representing reearch topics and application areas
categories: [Efficient formulation and solution methods, Production and operations planning]

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
  
profile: false
share: false
---