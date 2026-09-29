---
title: 'Input convex neural networks as surrogates in mathematical optimisation'
# If group member, use folder name in /content/authors
authors:
  - g_yu-liu
  - Jan Kronqvist
  - g_fabricio-oliveira
date: 2026-08-11
doi: 10.48550/arXiv.2608.09707

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

abstract: 'Embedding trained neural networks as surrogates within optimisation problems is an established practice in operations research. The prevailing approach uses feedforward neural networks (FNNs) with ReLU activations, whose piecewise-linear structure admits an exact but computationally intensive mixed-integer programming (MIP) reformulation as the networks grow. We advocate input convex neural networks (ICNNs) as structurally superior surrogates when the underlying response is approximately convex or concave. The convex architecture offers two computational advantages. First, the ICNN-MIP formulation tends to yield a tighter linear programming (LP) relaxation than its FNN-MIP counterpart, with no integrality gap in favourable instances. Second, ICNNs uniquely admit an LP-based reformulation via epigraph representations of ReLU activations, though this embedding is not always exact. When it is not, we exploit the properties of ICNNs to construct the strongest continuous relaxation over box domains, namely, the convex hull of the ICNN''s graph, bounded below by the epigraph and above by the concave envelope; this construction is tractable under input convexity but hard for general ReLU networks. On this basis, we develop a branch-and-bound algorithm that builds this relaxation at each node, branches directly on input variables rather than intermediate variables as in MIP reformulations, and terminates at the root node whenever the epigraph embedding is valid. Case studies on humanitarian food aid, oil well routing, and wine blending show that ICNN surrogates match FNN accuracy and deliver gains in solve time and scalability, supporting ICNN as the default surrogate when the underlying function is convex, concave, or well-approximated as such.'

# Summary. An optional shortened abstract.
summary:  

# Not in use. Could be used for keywords 
tags:
  
featured: false

# links:
url_pdf: 'https://doi.org/10.48550/arXiv.2608.09707'
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