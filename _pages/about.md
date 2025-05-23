---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I'm an incoming Ph.D. Student in Computer Science at University of Illinois Chicago, under the supervision of Prof. [Philip S. Yu](https://scholar.google.com/citations?user=D0lL1r0AAAAJ). Previously, I received my MEng degree in Computer Engineering at Zhejiang University. I also work closely with Prof. [Yongfeng Zhang](https://yongfeng.me/) @ Rutgers University and Prof. [Shiqing Ma](https://people.cs.umass.edu/~shiqingma/) @ University of Massachusetts Amherst.

My research interests lie at:
- **Machine Learning**: (Multimodal) Large Language Models; LLM-based Agent; Self-supervised Learning;
- **Trustworthy ML**: MLLM (Agent) Safety and Security, Responsible AIGC;
- **Data Mining and ML Application**: ML for Industrial Fault Diagnosis, Anomaly/Out-of-Distribution Detection; ML for Healthcare;


# 🔥 News
- *2025.05*: &nbsp;🎉🎉 I will be starting my CS Ph.D. in [BDSC Lab](https://bdsc-uic.github.io/index.html) at University of Illinois Chicago, under the supervision of Prof. [Philip S. Yu](https://scholar.google.com/citations?user=D0lL1r0AAAAJ).
- *2025.03*: &nbsp;🎉🎉 I've been awarded the Outstanding Graduate in Zhejiang Province and Outstanding Graduate at Zhejiang University.
- *2025.02*: &nbsp;🎉🎉 [Invisible Backdoor Attack in Self-supervised Learning](https://arxiv.org/abs/2405.14672) is accepted by CVPR 2025.
- *2025.01*: &nbsp;🎉🎉 [Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents](https://arxiv.org/abs/2410.02644) is accepted by ICLR 2025.
- *2025.01*: &nbsp;🎉🎉 [Class Incremental Fault Diagnosis under Limited Fault Data via Supervised Contrastive Knowledge Distillation](https://arxiv.org/pdf/2501.09525) is accepted by IEEE Transactions on Industrial Informatics.
- *2024.11*: &nbsp;🎉🎉 I've been awarded the National Scholarship for Graduate Students at Zhejiang University.
- *2024.04*: &nbsp;🎉🎉 [Generalized Out-of-distribution Fault Diagnosis (GOOFD) via Internal Contrastive Learning](https://ieeexplore.ieee.org/abstract/document/10510599) is accepted by IEEE Transactions on Industrial Informatics.
- *2023.11*: &nbsp;🎉🎉 I've been awarded the National Scholarship for Graduate Students at Zhejiang University.


# 📖 Educations
- **University of Illinois Chicago** | Aug. 2025 -- <br>
  Ph.D. Computer Science, USA<br>
  Supervisor: Prof. [Philip S. Yu](https://scholar.google.com/citations?user=D0lL1r0AAAAJ)
  
- **Zhejiang University** | Sep. 2022 -- Mar. 2025 <br>
  MEng. Computer Engineering, China<br>
  **Ranking: 1/82**; Supervisor: Prof. [Hongwei Wang](https://person.zju.edu.cn/en/hwang)

- **University of Leeds** (QS 75) | Sep. 2018 -- Jun. 2022<br>
  BSc. Computer Science - **Honors First Class Degree**, United Kingdom

- **Southwest Jiaotong University** | Sep. 2018 -- Jun. 2022<br>
  BEng. Computer Science and Technology, China<br>
  **Ranking: 1/75**; Supervisor: Prof. [Tianrui Li](https://scholar.google.com/citations?user=CQ1HneMAAAAJ)


# 📝 Publications

### * denotes Equal Contribution

<!-- <div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2016</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Deep Residual Learning for Image Recognition](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf)

**Kaiming He**, Xiangyu Zhang, Shaoqing Ren, Jian Sun

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.
</div>
</div> -->

<!-- - [Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet](https://github.com), A, B, C, **CVPR 2020** -->
## Trustworthy ML:
1. [Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents](https://arxiv.org/abs/2410.02644)<br>
**Hanrong Zhang**, Jingyuan Huang, [Kai Mei](https://dongyuanjushi.github.io/), Yifei Yao, [Zhenting Wang](https://zhentingwang.github.io/), Chenlu Zhan, Hongwei Wang, [Yongfeng Zhang](https://yongfeng.me/) <br>
Proceedings of the Thirteenth International Conference on Learning Representations (ICLR), 2025.
\[[arxiv](https://arxiv.org/abs/2410.02644)\] \[[code](https://github.com/agiresearch/ASB)\] \[[website](https://luckfort.github.io/ASBench/)\] 

1. [Invisible Backdoor Attack in Self-supervised Learning](https://arxiv.org/abs/2405.14672)<br>
**Hanrong Zhang**\*, [Zhenting Wang](https://zhentingwang.github.io/)\*, Tingxu Han, Mingyu Jin, Chenlu Zhan, [Mengnan Du](https://mengnandu.com/), Hongwei Wang, [Shiqing Ma](https://people.cs.umass.edu/~shiqingma/) <br>
Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2025.
\[[arxiv](https://arxiv.org/abs/2405.14672)\] \[[code](https://github.com/Zhang-Henry/INACTIVE)\]



## Machine Learning and Data Mining:
1. [Class Incremental Fault Diagnosis under Limited Fault Data via Supervised Contrastive Knowledge Distillation](https://arxiv.org/pdf/2501.09525)<br>
**Hanrong Zhang**, Yifei Yao, Zixuan Wang, Jiayuan Su, Mengxuan Li, Peng Peng, Hongwei Wang<br>
IEEE Transactions on Industrial Informatics (**IF=12.3**, JCR Q1 SCI)
\[[arxiv](https://arxiv.org/pdf/2501.09525)\] \[[code](https://github.com/Zhang-Henry/SCLIFD_TII)\]

1. [Generalized Out-of-distribution Fault Diagnosis (GOOFD) via Internal Contrastive Learning](https://ieeexplore.ieee.org/abstract/document/10510599)<br>
Xingyue Wang\*, **Hanrong Zhang**\*, Xinlong Qiao, Ke Ma, Shuting Tao, Peng Peng, Hongwei Wang<br>
IEEE Transactions on Industrial Informatics (**IF=12.3**, JCR Q1 SCI)

1. [Imbalanced Chemical Process Fault Diagnosis Using Balancing GAN With Active Sample Selection](https://ieeexplore.ieee.org/abstract/document/10114639)<br>
Peng Peng\*, **Hanrong Zhang**\*, Xinyue Wang, Wanqiu Huang, Hongwei Wang<br>
IEEE Sensors Journal (IF=4.3, JCR Q1 SCI)



1. [From Uncertainty to Clarity: Uncertainty-Guided Class-Incremental Learning for Limited Biomedical Samples via Semantic Expansion](https://arxiv.org/abs/2409.07757)<br>
Yifei Yao\*, **Hanrong Zhang**\*, Hongwei Wang, Ying Chi (preprint, Medical Image Analysis Under Review)

1. [Multi-gate Mixture-of-Expert Combined with Synthetic Minority Over-sampling Technique for Multimode Imbalanced Fault Diagnosis](https://ieeexplore.ieee.org/abstract/document/10152774)<br>
Wanqiu Huang, **Hanrong Zhang**, Peng Peng, Hongwei Wang<br>
International Conference on Computer Supported Cooperative Work in Design (IEEE CSCWD 2023, **Best Paper Award Finalist**)

1. [Debiasing Medical Visual Question Answering via Counterfactual Training](https://link.springer.com/chapter/10.1007/978-3-031-43895-0_36)<br>
Chenlu Zhan\*, Peng Peng\*, **Hanrong Zhang**, Haiyue Sun, Chunnan Shang, Tao Chen, Hongsen Wang, Gaoang Wang, Hongwei Wang<br>
International Conference on Medical Image Computing and Computer-Assisted Intervention (MICCAI 2023)


## Knowledge Graph:
1. [SAKA: an intelligent platform for semi-automated knowledge graph construction and application](https://link.springer.com/article/10.1007/s11761-023-00371-x)<br>
**Hanrong Zhang**, Xinyue Wang, Jiabao Pan, Hongwei Wang<br>
Service Oriented Computing and Applications

1. [An Intelligent System for Semantic Information Extraction and Knowledge Graph Construction from Multi-Type Data Sources](https://ieeexplore.ieee.org/abstract/document/10035077)<br>
**Hanrong Zhang**, Xinyue Wang, Bo Qin, Hongwei Wang<br>
IEEE International Conference on e-Business Engineering (ICEBE 2022)


# 🎖 Honors and Awards

## Scholarships
- **National Scholarship for Graduate Students (Top 0.2%)**, ZJU, 2023 - 2024
- **National Scholarship for Graduate Students (Top 0.2%)**, ZJU, 2022 - 2023
- **First-class full-ride Scholarship (1/75, ￥62000)**, UoL, 2020 - 2021
- **National Scholarship for Undergraduate Students (Top 0.2%)**, SWJTU, 2019 - 2020
- Second-class Scholarship (3/75, ￥25000), UoL, 2018 - 2019

## Academic Awards
- **Outstanding Graduate in Zhejiang Province**, ZJU, 2025;
- **Outstanding Graduate at Zhejiang University**, ZJU, 2025;
- Award of Honor for Graduate, ZJU, 2022 - 2023, 2023 - 2024
- Graduate with Merit A Performance, ZJU, 2022 - 2023
- **Provincial Outstanding Graduate**, SWJTU, 2022;
- **Best Student in Computer Science (1/75)**, UoL, 2020 - 2021
- **Best Student Overall (1/300, 4 majors)**, UoL, 2018 - 2019
- Pacemaker to Merit Student (Top 1%), SWJTU, 2018 - 2019 & 2019 - 2020 & 2020 - 2021

## Competition Awards
- Mathematical Modeling Contest for College Students, *National Second Prize (Top 0.5% of 45,000 teams)*, Sep. 2020
- Students Service Outsourcing Innovation and Entrepreneurship Competition, *National Second Prize (Top 3%)*, Aug. 2020
- MathorCup College Mathematical Modeling Competition,  *First Prize (Top 3%)*, May 2020
- May Day Mathematical Modeling Competition, *First Prize (Top 3%)*, May 2020
- Asia-Pacific Mathematical Modeling Contest, *First Prize (Top 3%)*, Nov. 2019
- Mathematical Modeling Competition in Southwest Jiaotong University, *First Prize (Top 3%)*, Nov. 2019
<!--- American College Student Mathematical Modeling Contest, *Honorable Mention (Top 10%)*, Jan. 2020-->

<!--Teachings
======
- Teaching Assistant, *ECE 448: Artificial Intelligence*, Zhejiang University and University of Illinois Urbana-Champaign (with Prof. [Mark Hasegawa-Johnson](https://ece.illinois.edu/about/directory/faculty/jhasegaw)), Spring 2023 and Spring 2024 (for undergraduates)
- Teaching Assistant, *ECE 2013: Artificial Intelligence*, Zhejiang University, Fall 2023 (for graduates)-->

<!-- # 💻 Internships
- *2019.05 - 2020.02*, [Lorem](https://github.com/), China. -->


<script type='text/javascript' id='clustrmaps' src='//cdn.clustrmaps.com/map_v2.js?cl=ffffff&w=794&t=tt&d=AMZ-k4oe-eM7qEBL1st--OzUlbxHV1mLbULIhu5_dXQ'></script>
