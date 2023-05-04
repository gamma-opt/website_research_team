---
title: A decomposition strategy for decision problems with endogenous uncertainty using mixed-integer programming
# If group member, use folder name in /content/authors
authors:
  - g_olli_herrala
  - Tommi Ekholm
  - g_fabricio_oliveira

date: 2023-04-01
doi: 10.48550/arXiv.2304.02338

# Schedule page publish date (NOT publication's date).
publishDate: 2017-01-01

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name. Notice * * on title. # Publication name and optional abbreviated publication name. Quote marks needed for Markdown typesetting
publication: '*ArXiv*'
publication_short: ''

abstract: Despite methodological advances for modeling decision problems under uncertainty, faithfully representing endogenous uncertainty still proves challenging, both in terms of modeling capabilities and computational requirements. A novel framework called Decision Programming provides an approach for solving such decision problems using off-the-shelf mathematical optimization solvers. This is made possible by using influence diagrams to represent a given decision problem, which is then formulated as a mixed-integer linear programming problem.
In this paper, we focus on the type of endogenous uncertainty that received less attention in the introduction of Decision Programming: conditionally observed information. Multi-stage stochastic programming (MSSP) models use conditional non-anticipativity constraints (C-NACs) to represent such uncertainties, and we show how such constraints can be incorporated into Decision Programming models. This allows us to consider the two main types of endogenous uncertainty simultaneously, namely decision-dependent information structure and decision-dependent probability distribution. Additionally, we present a decomposition approach that provides significant computational savings and also enables considering continuous decision variables in certain parts of the problem, whereas the original formulation was restricted to discrete variables only. The extended framework is illustrated with two example problems. The first considers an illustrative multiperiod game and the second is a large-scale cost-benefit problem regarding climate change mitigation. Neither of these example problems could be solved with existing frameworks.

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
categories: [Modelling decision-making and uncertainty, Efficient formulation and solution methods]

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: [2020-AF-Decision_programming]

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