---
title: 'An efficient mixed-integer linear programming formulation for solving influence diagrams'
# If group member, use folder name in /content/authors
authors:
  - g_topias-terho
  - g_fabricio-oliveira
  - Ahti Salo
  - Pedro Munari
date: 2026-01-14
doi: 10.48550/arXiv.2601.08460

# Schedule page publish date (NOT publication's date).
publishDate: 2017-01-01

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['3']

# Publication name and optional abbreviated publication name. Notice * * on title. # Publication name and optional abbreviated publication name. Quote marks needed for Markdown typesetting
publication: '*arXiv*'
publication_short: ''

abstract: 'Influence diagrams represent decision-making problems with interdependencies between random events, decisions, and consequences. Traditionally, they have been solved using algorithms that determine the expected utility-maximizing decision strategy. In contrast, state-of-the-art solution approaches convert influence diagrams into a mixed-integer linear programming (MILP) model, which can be solved with powerful off-the-shelf MILP solvers. From a computational standpoint, the existing MILP formulations can be efficiently solved when applied to influence diagrams that represent periodic (or sequential) decision processes, which can be cast as partially observable Markov Decision Processes. However, they are inefficient in problems that lack a periodic structure or if the nodes in the influence diagram have large state spaces, thus limiting their practical use. In this paper, we present an efficient MILP formulation that is specifically designed for influence diagrams that are challenging for the earlier MILP formulation-based methods. Additionally, we present how the proposed formulation can be adapted to maximize conditional value-at-risk and how chance and logical constraints can be incorporated into the formulation, thus retaining the modeling flexibility of the MILP-based methods. Finally, we perform computational experiments addressing problems from the literature and compare the computational efficiency of the proposed formulation against the available MILP formulations for the reported influence diagrams. We find that the MILP models based on the proposed formulations can be solved significantly more efficiently compared to the state-of-the-art when solving influence diagrams that cannot be cast as partially observable Markov decision processes.'

# Summary. An optional shortened abstract.
summary:  

# Not in use. Could be used for keywords 
tags:
  
featured: false

# links:
url_pdf: 'https://doi.org/10.48550/arXiv.2601.08460'
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