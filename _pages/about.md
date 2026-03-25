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

Hi, there! I'm Hanrong Zhang (张涵容), a CS PhD Student advised by Prof. [Philip S. Yu](https://cs.uic.edu/profiles/philip-yu/) (IEEE Fellow/ACM Fellow), also an incoming Google Student Researcher in 2026 summer. I received my Master degree from Zhejiang University, where I was honored as an Outstanding Graduate in Zhejiang Province and at Zhejiang University, and received the National Scholarship twice. I was also a research intern at Alibaba Group.

My research interests lie in:
- **LLM Agent**: Agent Training; Tool Learning; Data Synthethis; Agentic RL; Agent Safety and Security;
- **Large Language Model**: LLM Reasoning; LLM Post-training;
<!--- **Machine Learning and Data Mining**: ML for Industrial Fault Diagnosis, Self-supervised Learning-->
<!-- - **Machine Learning and Data Mining**: ML for Industrial Fault Diagnosis, Anomaly/Out-of-Distribution Detection; ML for Healthcare;-->

<!-- If you are interested in academic collaboration or discussion, please feel free to contact me zhanghr0709 [AT]  gmail.com. -->

<!-- 📢  **I am actively looking for research internships for Summer 2026. Feel free to reach out if you think I am a good fit!** -->

# 🔥 News
- *2026.03*: &nbsp;🎉🎉 Invited as a reviewer for NeurIPS 2026.
- *2026.02*: &nbsp;🎉🎉 I will join Google as a Student Researcher in 2026 summer.
- *2026.01*: &nbsp;🎉🎉 Invited as a reviewer for [TPAMI](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=34), ECCV 2026, ICML 2026, KDD 2026.
- *2025.11*: &nbsp;🎉🎉 Invited as a reviewer for [TMLR](https://jmlr.org/tmlr/).
- *2025.10*: &nbsp;🎉🎉 Invited as a reviewer for ICLR 2026, CVPR 2026, [TNNLS](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=5962385).
- *2025.04*: &nbsp;🎉🎉 Give a talk at [Xtra Computing Group](https://www.xtra.science/2025/04/invited-speakers/) of Prof. [Bingsheng He](https://www.comp.nus.edu.sg/~hebs/) at School of Computing, NUS.
- *2025.03*: &nbsp;🎉🎉 I've been awarded the Outstanding Graduate in Zhejiang Province and Outstanding Graduate at Zhejiang University.
- *2025.02*: &nbsp;🎉🎉 [Invisible Backdoor Attack in Self-supervised Learning](https://arxiv.org/abs/2405.14672) (First author) is accepted by CVPR 2025.
- *2025.01*: &nbsp;🎉🎉 [Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents](https://arxiv.org/abs/2410.02644) (First author) is accepted by ICLR 2025.
- *2025.01*: &nbsp;🎉🎉 [Class Incremental Fault Diagnosis under Limited Fault Data via Supervised Contrastive Knowledge Distillation](https://arxiv.org/pdf/2501.09525) (First author) is accepted by IEEE Transactions on Industrial Informatics.
- *2024.11*: &nbsp;🎉🎉 I've been awarded the National Scholarship for Graduate Students at Zhejiang University.
- *2023.11*: &nbsp;🎉🎉 I've been awarded the National Scholarship for Graduate Students at Zhejiang University.


# 📖 Educations
- **University of Illinois Chicago** | Aug. 2025 -- Present <br>
  Ph.D. in Computer Science, USA<br>
  Supervisor: Prof. [Philip S. Yu](https://cs.uic.edu/profiles/philip-yu/)

- **Zhejiang University** | Sep. 2022 -- Mar. 2025 <br>
  Master of Engineering in Computer Engineering, China<br>
  **Ranking: 1/82**; Supervisor: Prof. [Hongwei Wang](https://person.zju.edu.cn/en/hwang)

- **University of Leeds** (QS 75) | Sep. 2018 -- Jun. 2022<br>
  Bachelor of Science in Computer Science - **Honors First Class Degree**, United Kingdom

- **Southwest Jiaotong University** | Sep. 2018 -- Jun. 2022<br>
  Bachelor of Engineering in Computer Science and Technology, China<br>
  **Ranking: 1/75**; Supervisor: Prof. [Tianrui Li](https://scholar.google.com/citations?user=CQ1HneMAAAAJ)

# 💻 Internships
- Student Researcher, **Google**, 2026.05 - 2026.08 (incoming)
- Research Intern, **Alibaba Group**, 2025.05 - 2025.08
    - Research on RL for Human-Agent Multi-turn Interaction

# 🛠️ Open Source Projects

<div class="opensource-grid">
  <div class="opensource-card">
    <div class="opensource-card-header">
      <svg class="opensource-icon" viewBox="0 0 16 16" width="18" height="18" fill="currentColor"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg>
      <a href="https://github.com/OpenLAIR/dr-claw" class="opensource-repo-name">OpenLAIR / <strong>dr-claw</strong></a>
    </div>
    <p class="opensource-desc">A Super AI Lab with massive AI Doctors as Assistants. Best IDE for Research via AI Power</p>
    <div class="opensource-meta">
      <a href="https://github.com/OpenLAIR/dr-claw/stargazers"><img src="https://img.shields.io/github/stars/OpenLAIR/dr-claw?style=social" alt="GitHub stars"></a>
      <a href="https://github.com/OpenLAIR/dr-claw/network/members"><img src="https://img.shields.io/github/forks/OpenLAIR/dr-claw?style=social" alt="GitHub forks"></a>
    </div>
  </div>
  <div class="opensource-card">
    <div class="opensource-card-header">
      <svg class="opensource-icon" viewBox="0 0 16 16" width="18" height="18" fill="currentColor"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg>
      <a href="https://github.com/agiresearch/ASB" class="opensource-repo-name">agiresearch / <strong>ASB</strong></a>
    </div>
    <p class="opensource-desc">Benchmarking attacks &amp; defenses in LLM-based agents</p>
    <div class="opensource-meta">
      <a href="https://github.com/agiresearch/ASB/stargazers"><img src="https://img.shields.io/github/stars/agiresearch/ASB?style=social" alt="GitHub stars"></a>
      <a href="https://github.com/agiresearch/ASB/network/members"><img src="https://img.shields.io/github/forks/agiresearch/ASB?style=social" alt="GitHub forks"></a>
      <span class="opensource-venue">ICLR 2025</span>
    </div>
  </div>
  <div class="opensource-card">
    <div class="opensource-card-header">
      <svg class="opensource-icon" viewBox="0 0 16 16" width="18" height="18" fill="currentColor"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg>
      <a href="https://github.com/Zhang-Henry/INACTIVE" class="opensource-repo-name">Zhang-Henry / <strong>INACTIVE</strong></a>
    </div>
    <p class="opensource-desc">Invisible Backdoor Attack against Self-supervised Learning</p>
    <div class="opensource-meta">
      <a href="https://github.com/Zhang-Henry/INACTIVE/stargazers"><img src="https://img.shields.io/github/stars/Zhang-Henry/INACTIVE?style=social" alt="GitHub stars"></a>
      <a href="https://github.com/Zhang-Henry/INACTIVE/network/members"><img src="https://img.shields.io/github/forks/Zhang-Henry/INACTIVE?style=social" alt="GitHub forks"></a>
      <span class="opensource-venue">CVPR 2025</span>
    </div>
  </div>
  <div class="opensource-card">
    <div class="opensource-card-header">
      <svg class="opensource-icon" viewBox="0 0 16 16" width="18" height="18" fill="currentColor"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg>
      <a href="https://github.com/HenryPengZou/Awesome-Human-Agent-Collaboration-Interaction-Systems" class="opensource-repo-name">HenryPengZou / <strong>Awesome-Human-Agent-Collaboration-Interaction-Systems</strong></a>
    </div>
    <p class="opensource-desc">LLM-Based Human-Agent Collaboration and Interaction Systems: A Survey</p>
    <div class="opensource-meta">
      <a href="https://github.com/HenryPengZou/Awesome-Human-Agent-Collaboration-Interaction-Systems/stargazers"><img src="https://img.shields.io/github/stars/HenryPengZou/Awesome-Human-Agent-Collaboration-Interaction-Systems?style=social" alt="GitHub stars"></a>
      <a href="https://github.com/HenryPengZou/Awesome-Human-Agent-Collaboration-Interaction-Systems/network/members"><img src="https://img.shields.io/github/forks/HenryPengZou/Awesome-Human-Agent-Collaboration-Interaction-Systems?style=social" alt="GitHub forks"></a>
    </div>
  </div>
</div>

# 📝 Selected Publications and Preprints

\* denotes Equal Contribution. <a class='scholar_url' href='https://scholar.google.com/citations?user=qG5_O40AAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations" alt="Google Scholar Citations"></a>

<!-- <div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2016</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Deep Residual Learning for Image Recognition](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf)

**Kaiming He**, Xiangyu Zhang, Shaoqing Ren, Jian Sun

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span>
- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.
</div>
</div> -->

<!-- - [Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet](https://github.com), A, B, C, **CVPR 2020** -->
## LLM Agents:
1. [Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents](https://arxiv.org/abs/2410.02644)<br>
**Hanrong Zhang**, Jingyuan Huang, Kai Mei, Yifei Yao, Zhenting Wang, Chenlu Zhan, Hongwei Wang, Yongfeng Zhang <br>
**ICLR 2025**
\[[website](https://luckfort.github.io/ASBench/)\] [![GitHub stars](https://img.shields.io/github/stars/agiresearch/ASB?style=social)](https://github.com/agiresearch/ASB) <span class='show_paper_citations' data='qG5_O40AAAAJ:hqOjcs7Dif8C'></span>

1. [GAM: Hierarchical Graph Memory for LLM-based Agents](#)<br>
Zhaofen Wu\*, **Hanrong Zhang**\*, Fulin Lin, Wujiang Xu, Xinran Xu, Yankai Chen, Henry Peng Zou, Shaowen Chen, Weizhi Zhang, Xue Liu, Philip S. Yu, Hongwei Wang<br>
**ICLR 2026 Workshop MemAgents**

1. [Rethinking Memory Mechanisms of Foundation Agents in the Second Half: A Survey](https://www.arxiv.org/pdf/2602.06052)<br>
Worked as a core contributor <span class='show_paper_citations' data='qG5_O40AAAAJ:aqlVkmm33-oC'></span>


## Machine Learning and Data Mining:
1. [Invisible Backdoor Attack in Self-supervised Learning](https://arxiv.org/abs/2405.14672)<br>
**Hanrong Zhang**\*, Zhenting Wang\*, Tingxu Han, Mingyu Jin, Chenlu Zhan, Mengnan Du, Hongwei Wang, Shiqing Ma <br>
**CVPR 2025**
[![GitHub stars](https://img.shields.io/github/stars/Zhang-Henry/INACTIVE?style=social)](https://github.com/Zhang-Henry/INACTIVE) <span class='show_paper_citations' data='qG5_O40AAAAJ:UebtZRa9Y70C'></span>

1. [Class Incremental Fault Diagnosis under Limited Fault Data via Supervised Contrastive Knowledge Distillation](https://arxiv.org/pdf/2501.09525)<br>
**Hanrong Zhang**, Yifei Yao, Zixuan Wang, Jiayuan Su, Mengxuan Li, Peng Peng, Hongwei Wang<br>
**IEEE Transactions on Industrial Informatics** (**IF=12.3**, SCI Q1 Top) <span class='show_paper_citations' data='qG5_O40AAAAJ:4DMP91E08xMC'></span>

1. [Generalized Out-of-distribution Fault Diagnosis (GOOFD) via Internal Contrastive Learning](https://ieeexplore.ieee.org/abstract/document/10510599)<br>
Xingyue Wang\*, **Hanrong Zhang**\*, Xinlong Qiao, Ke Ma, Shuting Tao, Peng Peng, Hongwei Wang<br>
**IEEE Transactions on Industrial Informatics** (**IF=12.3**, SCI Q1 Top) <span class='show_paper_citations' data='qG5_O40AAAAJ:4TOpqqG69KYC'></span>

1. [Imbalanced Chemical Process Fault Diagnosis Using Balancing GAN With Active Sample Selection](https://ieeexplore.ieee.org/abstract/document/10114639)<br>
Peng Peng\*, **Hanrong Zhang**\*, Xinyue Wang, Wanqiu Huang, Hongwei Wang<br>
**IEEE Sensors Journal** (IF=4.3, SCI Q1) <span class='show_paper_citations' data='qG5_O40AAAAJ:ULOm3_A8WrAC'></span>


1. [SAKA: an intelligent platform for semi-automated knowledge graph construction and application](https://link.springer.com/article/10.1007/s11761-023-00371-x)<br>
**Hanrong Zhang**, Xinyue Wang, Jiabao Pan, Hongwei Wang<br>
**Service Oriented Computing and Applications** <span class='show_paper_citations' data='qG5_O40AAAAJ:d1gkVwhDpl0C'></span>

1. [An Intelligent System for Semantic Information Extraction and Knowledge Graph Construction from Multi-Type Data Sources](https://ieeexplore.ieee.org/abstract/document/10035077)<br>
**Hanrong Zhang**, Xinyue Wang, Bo Qin, Hongwei Wang<br>
**IEEE ICEBE 2022** <span class='show_paper_citations' data='qG5_O40AAAAJ:u5HHmVD_uO8C'></span>


1. [Multi-gate Mixture-of-Expert Combined with Synthetic Minority Over-sampling Technique for Multimode Imbalanced Fault Diagnosis](https://ieeexplore.ieee.org/abstract/document/10152774)<br>
Wanqiu Huang, **Hanrong Zhang**, Peng Peng, Hongwei Wang<br>
**IEEE CSCWD 2023**, **Best Paper Award Finalist** <span class='show_paper_citations' data='qG5_O40AAAAJ:2osOgNQ5qMEC'></span>

1. [From Uncertainty to Clarity: Uncertainty-Guided Class-Incremental Learning for Limited Biomedical Samples via Semantic Expansion](https://arxiv.org/abs/2409.07757)<br>
Yifei Yao\*, **Hanrong Zhang**\*, Xiaoxiao Li, Hongwei Wang, Ying Chi (preprint, Journal of Biomedical and Health Informatics Under Review) <span class='show_paper_citations' data='qG5_O40AAAAJ:Y0pCki6q_DkC'></span>

<!-- 1. [Debiasing Medical Visual Question Answering via Counterfactual Training](https://link.springer.com/chapter/10.1007/978-3-031-43895-0_36)<br>
Chenlu Zhan\*, Peng Peng\*, **Hanrong Zhang**, Haiyue Sun, Chunnan Shang, Tao Chen, Hongsen Wang, Gaoang Wang, Hongwei Wang<br>
MICCAI 2023 <span class='show_paper_citations' data='qG5_O40AAAAJ:TFP_iSt0sucC'></span>

1. [Industrial Data Synthesis Framework for Fault Diagnosis Using Diffusion and Flow-Based Models](https://ieeexplore.ieee.org/abstract/document/11033333/)<br>
Shuting Tao, Xiangming Meng, **Hanrong Zhang**, Hongwei Wang<br>
IEEE CSCWD 2025 <span class='show_paper_citations' data='qG5_O40AAAAJ:M3ejUd6NZC8C'></span> -->



# 🎖 Honors and Awards

## Scholarships
- **National Scholarship for Graduate Students (Top 0.2%)**, ZJU, 2023 - 2024
- **National Scholarship for Graduate Students (Top 0.2%)**, ZJU, 2022 - 2023
- **First-class full-ride Scholarship (1/75, ￥62000)**, UoL, 2020 - 2021
- **National Scholarship for Undergraduate Students (Top 0.2%)**, SWJTU, 2019 - 2020
<!-- - Second-class Scholarship (3/75, ￥25000), UoL, 2018 - 2019 -->

## Academic Awards
- **Outstanding Graduate in Zhejiang Province and at Zhejiang University**, ZJU, 2025
<!-- - Award of Honor for Graduate, ZJU, 2022 - 2023, 2023 - 2024-->
<!-- - Graduate with Merit A Performance, ZJU, 2022 - 2023 -->
- **Provincial Outstanding Graduate**, SWJTU, 2022
- **Best Student in Computer Science (1/75)**, UoL, 2020 - 2021
- **Best Student Overall (1/300, 4 majors)**, UoL, 2018 - 2019
<!-- - Pacemaker to Merit Student (Top 1%), SWJTU, 2018 - 2019 & 2019 - 2020 & 2020 - 2021 -->

## Competition Awards
- Mathematical Modeling Contest for College Students, *National Second Prize*, Sep. 2020
- Students Service Outsourcing Innovation and Entrepreneurship Competition, *National Second Prize*, Aug. 2020
- MathorCup College Mathematical Modeling Competition,  *First Prize*, May 2020
- May Day Mathematical Modeling Competition, *First Prize*, May 2020
- Asia-Pacific Mathematical Modeling Contest, *First Prize*, Nov. 2019
- Mathematical Modeling Competition in Southwest Jiaotong University, *First Prize*, Nov. 2019
<!--- American College Student Mathematical Modeling Contest, *Honorable Mention (Top 10%)*, Jan. 2020-->


# 📝 Academic Service
## Conference Program Committee/Reviewer
- ICLR 2026
- NeurIPS 2026
- ICML 2026
- CVPR 2026
- ECCV 2026
- KDD 2026
- MICCAI 2026

## Journal Reviewer
- [IEEE Transactions on Pattern Analysis and Machine Intelligence](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=34) (TPAMI)
- [IEEE Transactions on Neural Networks and Learning Systems](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=5962385) (TNNLS)
- [Pattern Recognition](https://www.sciencedirect.com/journal/pattern-recognition)
- [Transactions on Machine Learning Research](https://jmlr.org/tmlr/) (TMLR)
- [IEEE Transactions on Industrial Informatics](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=9424)
- [IEEE Transactions on Reliability](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=24)
- [IEEE Transactions on Computational Biology and Bioinformatics]()
- [IEEE Transactions on Industrial Cyber-Physical Systems]()

<!-- ## Volunteer
- ICLR 2025 -->




<!-- # 💻 Teachings
- Teaching Assistant, *ECE 448: Artificial Intelligence*, Zhejiang University and University of Illinois Urbana-Champaign (with Prof. [Mark Hasegawa-Johnson](https://ece.illinois.edu/about/directory/faculty/jhasegaw)), Spring 2023 and Spring 2024 (for undergrad)
- Teaching Assistant, *ECE 2013: Artificial Intelligence*, Zhejiang University, Fall 2023 (for grad) -->


<script type='text/javascript' id='clustrmaps' src='//cdn.clustrmaps.com/map_v2.js?cl=ffffff&w=794&t=tt&d=AMZ-k4oe-eM7qEBL1st--OzUlbxHV1mLbULIhu5_dXQ'></script>
