---
title: 'Decision tree enhancer (DTE): Improving decision trees with optimization'
# If group member, use folder name in /content/authors
authors:
  - p_flavio-limapo
  - g_fabricio-oliveira
  - Silvio Hamacher
date: 2026-04-01
doi: 10.1016/j.knosys.2026.115597

# Schedule page publish date (NOT publication's date).
publishDate: 2017-01-01

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# Publication name and optional abbreviated publication name. Notice * * on title. # Publication name and optional abbreviated publication name. Quote marks needed for Markdown typesetting
publication: '*Knowledge-Based Systems*'
publication_short: ''

abstract: 'Decision trees are off-the-shelf machine learning models widely used for classification and regression tasks in medical, logistics, financial, and other critical areas where interpretability is a key factor. They can efficiently handle numerical and categorical variables, making them a versatile choice for various applications. However, traditional decision-tree training methods are based on greedy heuristics, which cannot provide guarantees regarding whether further improvements could be achieved. We propose Decision Tree Enhancer (DTE), which employs optimization as a post-training step to improve previously trained decision trees. Moreover, the proposed method precludes the need for a pre-processing step for continuous features such as discretization or bucketization, and can be applied regardless of the model used to first train the decision tree. Lastly, DTE’s mathematical programming formulation enables, for example, the consideration of recall thresholds and class prioritization. Tested on 63 classification datasets from the UCI Machine Learning Repository, using tree depths from 1 to 5, four time limits (1, 5, 10, and 30 seconds), and 5 randomized train-test splits cross-validation, the proposed post-training step demonstrated superior performance over CART (Classification And Regression Tree), for both in- and out-of-sample data. With a 30-second time limit, DTE was able to improve the weighted recall in 83.2% of the datasets with an average improvement of 9.0% in training and 5.0% in testing.'

# Summary. An optional shortened abstract.
summary:  

# Not in use. Could be used for keywords 
tags:
  
featured: false

# links:
url_pdf: 'https://doi.org/10.1016/j.knosys.2026.115597'
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
  
# remove social media icons 
share: false
---