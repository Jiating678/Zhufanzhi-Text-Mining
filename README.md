# Zhufanzhi-Text-Mining
**Project Overview**

This project focuses on analyzing the place names mentioned in the Zhufanzhi (诸蕃志), an important historical text from the Song Dynasty (960-1279 CE) that documents foreign lands and interactions with neighboring countries. The goal is to understand how the relationships between China and other regions were shaped during the medieval period. The analysis of place names forms a foundational step toward understanding Sino-foreign relations through the lens of historical geography and spatial history.
Research Iterations

**Iteration 1: Initial Setup and Research Planning (Aug 27 - Sep 9)**

In the first iteration, the focus was on defining the scope of the research and identifying the methodology for analyzing Zhufanzhi. 
Key decisions included:
1) Learning primary source.
2) Utilizing OpenCC for chracters conversion.

**Iteration 2: Basic Textual Analysis (Sep 10 - Oct 18)**

In this iteration, the primary task was to basic text analysis.
Key decisions included:
1) Word segmentation and High-frequency analysis.
2) Realizing necessity of constructing Stop-word list and topic dictionaries.

**Iteration 3: Tokenization and Preliminary Social Network Analysis (Oct 21 - Nov 18)**

In this iteration, the focus was on tokenization and preliminary place name co-occurrence and social network analysis.
Key decisions included:
1) Utilizing the MARKUS platform to assist with automatic tagging of place names, followed by manual corrections.
2) Creating a historical place name dictionary based on the tokenized results.
3) Encountering challenges related to the subjectivity of tokenization and inconsistencies in the automatic tool’s results.
4) Performing second high-frequency analysis to identify the most commonly mentioned places.
5) Begining exploring social network analysis with Gephi to map the relationships between different places mentioned in the *Zhufanzhi*.

**Iteration 4: Public-Facing Presentation and Further Insights (Nov 18 - Dec 9)**

In the fourth iteration, the focus shifted towards making the project more accessible and refining the research outputs:
Key decisions included:
1) Developing a public-facing presentation of the high-frequency results and social network centrality analysis.
2) Focusing on the 15 most frequently mentioned places in the text and providing English translations and contemporary equivalents.
3) Conducting social network analysis using Gephi, focusing on centrality measures such as degree centrality, betweenness centrality, and closeness centrality.

**Tools and Platforms Used**

MARKUS: A platform developed for text annotation and tokenization, particularly useful for historical texts. It allowed for both manual and automatic tagging of place names, helping to create a historical place name dictionary.
Website: [MARKUS Platform](https://dh.chinese-empires.eu/markus/)

Gephi: A social network analysis tool used to analyze relationships between different places mentioned in the *Zhufanzhi*. Centrality measures were used to explore the significance of particular places in the text.
Website: [Gephi](https://gephi.org/)

Python and VS Code: Used for data processing, including high-frequency analysis and tokenization. Python scripts were written to automate various steps in the analysis.
Packages: OpenCC: https://github.com/BYVoid/OpenCC; Jiayan: https://github.com/jiaeyan/Jiayan; Panda: https://blog.csdn.net/GCTTTTTT/article/details/121870643.

Web Resources for Translation: A website was used to translate place names into English.
Website: Story Maps: Translation of Zhufanzhi Place Names, https://storymaps.arcgis.com/stories/39bce63e4e0642d3abce6c24db470760

**Conclusion**

This project has been an iterative process of refining research methods, analyzing historical materials, and making the findings accessible to a broader audience. The combination of manual and automated text analysis tools, coupled with social network analysis, has provided valuable insights into the spatial networks of the Song Dynasty, particularly its relations with Southeast Asia and beyond. As the project progresses, the integration of more secondary sources and further refinement of the analysis will continue to deepen our understanding of the historical dynamics at play.

**Author Bio**
Jiating is a history PhD student at the University of Pittsburgh, focusing on Sino-Southeast Asian relations during the Song Dynasty. Her research interests include exploring the complex networks of maritime trade, political interactions, and cultural exchanges between China and Southeast Asia through spatial history and digital methods. Her work aims to enhance understanding of medieval global connections and contribute to the broader field of world history.
