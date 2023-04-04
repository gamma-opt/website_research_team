---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: The p-Lagrangian relaxation for separable nonconvex MIQCQP problems
subtitle: ''
summary: ''
authors:
- Tiago Andrade
- Nikita Belyak
- Andrew Eberhard
- Silvio Hamacher
- Fabricio Oliveira
tags: [Convexification techniques, Decomposition techniques]
categories: [Efficient formulations and solution methods]
keywords: '
- Lagrangian decomposition
- Reformulated normalised multiparametric disaggregation technique
- Nonconvex mixed integer quadratically constrained quadratic programs
- Decomposition methodsx'
date: '2022-02-22'
lastmod: 2022-02-22T16:01:38+03:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2022-02-22T13:01:38.690790Z'
# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']
abstract: This paper presents a novel technique to compute Lagrangian bounds for nonconvex mixed-integer quadratically constrained quadratic programming problems presenting a separable structure (i.e., a separable problems) such as those arising in deterministic equivalent representations of two-stage stochastic programming problems. In general, the nonconvex nature of these models still poses a challenge to the available solvers, which do not consistently perform well for larger-scale instances. Therefore, we propose an appealing alternative algorithm that allows for overcoming computational performance issues. Our novel technique, named the p-Lagrangian decomposition, is a decomposition method that combines Lagrangian decomposition with mixed-integer programming-based relaxations. These relaxations are obtained using the reformulated normalised multiparametric disaggregation technique and can be made arbitrarily precise by means of a precision parameter p. We provide a technical analysis showing the convergent behaviour of the approach as the approximation is made increasingly precise. We observe that the proposed method presents significant reductions in computational time when compared with a previously proposed techniques in the literature and the direct employment of a commercial solver. Moreover, our computational experiments show that the employment of a simple heuristic can recover solutions with small duality gaps.

publication: '*Journal of Global Optimization*'
url_pdf: https://link.springer.com/article/10.1007/s10898-022-01138-y
doi: 10.1007/s10898-022-01138-y
---
