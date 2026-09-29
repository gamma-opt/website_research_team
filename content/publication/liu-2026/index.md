---
title: 'ICNN-enhanced 2SP: Leveraging input convex neural networks for solving two-stage stochastic programming'
# If group member, use folder name in /content/authors
authors:
  - g_yu-liu
  - g_fabricio-oliveira
  - Jan Kronqvist
date: 2026-09-01
doi: 10.1016/j.ejco.2026.100141

# Schedule page publish date (NOT publication's date).
publishDate: 2017-01-01

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# Publication name and optional abbreviated publication name. Notice * * on title. # Publication name and optional abbreviated publication name. Quote marks needed for Markdown typesetting
publication: '*EURO Journal on Computational Optimization*'
publication_short: ''

abstract: 'Two-stage stochastic programming (2SP) offers a basic framework for modelling decision-making under uncertainty, yet scalability remains a challenge due to the computational complexity of recourse function evaluation. Existing learning-based methods like Neural Two-Stage Stochastic Programming (Neur2SP) employ neural networks (NNs) as recourse function surrogates but rely on computationally intensive mixed-integer programming (MIP) formulations. We propose ICNN-enhanced 2SP, a method that leverages Input Convex Neural Networks (ICNNs) to exploit linear programming (LP) representability in convex 2SP problems. By architecturally enforcing convexity and enabling exact inference through LP, our approach eliminates the need for integer variables inherent to the conventional MIP-based formulation while retaining an exact embedding of the ICNN surrogate within the 2SP framework. This results in a more computationally efficient alternative, and we show that good solution quality can be maintained. Comprehensive experiments reveal that ICNNs incur only marginally longer training times while achieving validation accuracy on par with their standard NN counterparts. Across benchmark problems, ICNN-enhanced 2SP often exhibits considerably faster solution times than the MIP-based formulations while preserving solution quality, with these advantages becoming significantly more pronounced as problem scale increases. For the most challenging instances, the method achieves speedups of up to 100 and solution quality superior to MIP-based formulations.'

# Summary. An optional shortened abstract.
summary:  

# Not in use. Could be used for keywords 
tags:
  
featured: false

# links:
url_pdf: 'https://doi.org/10.1016/j.ejco.2026.100141'
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