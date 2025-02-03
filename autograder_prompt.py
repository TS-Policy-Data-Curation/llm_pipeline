rubric_prompt = """Evaluation Rubric for Economic Policy Explanations
1. Accuracy and Specificity of Policy References
Excellent (4 points):
Clearly identifies multiple real, historically or currently implemented policies relevant to the economic context.
Provides detailed descriptions, including policy names, enactment dates, and jurisdictions.
Demonstrates deep understanding of the policies' mechanics and historical impact.
Good (3 points):
Identifies at least one or two relevant real-world policies.
Provides some context (e.g., brief descriptions or historical notes) but may lack complete details.
Adequate (2 points):
Mentions policies, but some may be too generic or loosely tied to actual historical policies.
Lacks depth in explaining the specifics or context of these policies.
Needs Improvement (1 point):
Provides vague, ambiguous, or inaccurate policy references.
Fails to clearly connect the policy with a real-world counterpart.

2. Integration and Consideration of Multiple Factors
Excellent (4 points):
Thoroughly considers a wide range of factors (e.g., fiscal, monetary, regulatory) that could influence the time series data.
Provides a nuanced analysis of how these factors interact and affect the economic outcomes.
Clearly links each factor to specific observed trends in the time series.
Good (3 points):
Considers several key factors relevant to the data.
Offers a logical explanation of factor interactions, though some links may be less developed.
Adequate (2 points):
Mentions multiple factors but with limited discussion or clear connection to the data.
Analysis appears superficial or does not fully capture the complexity of the interactions.
Needs Improvement (1 point):
Considers only one or two factors without acknowledging the broader context.
Lacks clear connections between the factors and the observed time series.

3. Use of Evidence from Time Series Data
Excellent (4 points):
Provides explicit references to key data points, trends, or anomalies in the time series.
Uses data effectively to support and justify the selection of specific policies.
Incorporates graphical or statistical evidence when appropriate, ensuring clarity in the link between evidence and policy.
Good (3 points):
References relevant evidence from the time series, though the connection to policies could be more explicitly drawn.
Data usage is sound but might lack depth or detail.
Adequate (2 points):
Mentions evidence in general terms without linking it directly to policy recommendations.
Analysis of the data is minimal or lacks clarity.
Needs Improvement (1 point):
Provides little to no reference to actual data from the time series.
Fails to substantiate policy recommendations with empirical evidence.

4. Feasibility and Economic Plausibility
Excellent (4 points):
Clearly explains how and why the proposed policies are feasible given current economic conditions and institutional constraints.
Demonstrates deep understanding of economic theory and practical challenges.
Addresses potential trade-offs and provides contingency considerations.
Good (3 points):
Provides a convincing argument for the feasibility of the policies.
Recognizes some practical constraints but may not fully address potential challenges.
Adequate (2 points):
Offers policies that are conceptually sound but lacks discussion of real-world feasibility.
Overlooks significant practical or institutional challenges.
Needs Improvement (1 point):
Proposes policies that are unrealistic or impractical.
Fails to acknowledge known economic constraints or potential unintended consequences.
5. Depth, Clarity, and Coherence of Analysis
Excellent (4 points):
Presents a well-organized, logically coherent argument that connects policies, factors, and data seamlessly.
Uses clear, concise language with appropriate economic terminology.
Shows rigorous analytical depth, with each section building upon the previous.
Good (3 points):
Analysis is generally clear and logically organized.
Some minor gaps in the narrative, but overall argumentation is solid.
Adequate (2 points):
The explanation is somewhat disjointed or contains gaps in logic.
Clarity may suffer from underdeveloped sections or unclear language.
Needs Improvement (1 point):
Lacks coherence or clear organization.
Arguments are poorly structured, making it difficult to understand the rationale behind policy recommendations.

6. Methodological Rigor and Analytical Framework
Excellent (4 points):
Employs a robust economic framework or model to link policies with time series trends.
Demonstrates analytical rigor through clear methodological steps and sound reasoning.
Appropriately references economic theories and empirical methodologies.
Good (3 points):
Uses an appropriate framework or model with generally sound reasoning.
Some methodological details may be underdeveloped or assumed.
Adequate (2 points):
Methodology is present but not fully fleshed out or is somewhat generic.
Lacks depth in applying economic theory or empirical techniques.
Needs Improvement (1 point):
Demonstrates little to no methodological rigor.
Fails to apply a coherent framework, resulting in weak analytical justification.

7. Presentation and Professionalism
Excellent (4 points):
The response is professionally formatted, free of errors, and uses proper citations where necessary.
Visual aids (tables, graphs, charts) are used effectively to support the argument.
The overall presentation enhances clarity and comprehension.
Good (3 points):
Well-organized and clear, with only minor formatting or stylistic issues.
Visual aids and citations are used appropriately.
Adequate (2 points):
Some formatting issues are present, and the presentation may distract from the overall argument.
Use of visual aids or citations is minimal or inconsistent.
Needs Improvement (1 point):
Poorly formatted and difficult to follow.
Lacks professional presentation and appropriate citation of sources.

Using the Rubric
Total Possible Points: 28 (each of the 7 criteria is worth up to 4 points)
Scoring Guide:
Excellent Overall Response: 25-28 points
Good Overall Response: 19-24 points
Adequate Overall Response: 13-18 points
Needs Improvement: 7-12 points
This rubric ensures that responses are evaluated comprehensively—assessing not only the factual correctness of the policy references but also the analytical rigor, evidence integration, feasibility, and overall clarity of the response. Feel free to adapt or expand the rubric as needed for your specific context or evaluation goals."""
autograder_prompt = """

---

## Rubric Overview

| Criterion | Definition / What to Look For |
| --- | --- |
| **1. Clarity & Comprehensibility** | Are the policy's goals and mechanisms clearly stated, coherent, and understandable? |
| **2. Use of Time Series Insights** | How well does the policy incorporate and accurately interpret time series data and trends? |
| **3. Feasibility & Practicality** | How realistically can the policy be implemented given real-world constraints (e.g., budgets, resources)? |
| **4. Depth of Explanation** | How thoroughly are the underlying causal factors and assumptions behind time series patterns explained? |
| **5. Stakeholder Engagement** | Does the policy address the needs and perspectives of different stakeholders (public, experts, etc.)? |
| **6. Ethical & Equity Considerations** | Does the policy safeguard against biases, ensure fair treatment, and consider vulnerable groups? |
| **7. Evidence & Justification** | Is the policy supported by relevant research, data, or authoritative sources? |
| **8. Measurable Outcomes** | Does the policy propose clear metrics and methods to evaluate success over time? |
| **9. Communication & Transparency** | How well does the policy foster transparency and open communication regarding the time series analyses? |
| **10. Overall Impact** | Does the policy demonstrate potential for significant positive impact or innovation in its domain? |

---

## Performance Levels

Each criterion can be assessed on a scale (e.g., 1 to 4), with **4 = Excellent**, **3 = Good**, **2 = Needs Improvement**, **1 = Poor**. You can add half-points or different numerical scales if desired.

### Level Descriptions

- **4 (Excellent)**
    - The policy proposal fully meets or exceeds the criterion’s requirements.
    - Demonstrates outstanding coherence, creativity, or rigor.
- **3 (Good)**
    - The policy proposal addresses most aspects of the criterion effectively.
    - Minor gaps or weaknesses may be present, but do not undermine the overall quality.
- **2 (Needs Improvement)**
    - The policy proposal partially meets the criterion’s requirements.
    - Noticeable weaknesses or inconsistencies that limit its overall effectiveness.
- **1 (Poor)**
    - The policy proposal fails to meet the criterion’s requirements.
    - Major flaws, lack of clarity, or fundamental misunderstandings.

---

## Detailed Rubric

### 1. Clarity & Comprehensibility

- **Excellent (4):**
The policy is stated with precise language and a coherent structure. Readers can easily identify the main goals, scope, and steps.
- **Good (3):**
The policy is mostly clear, with only minor ambiguities or jargon that might confuse some readers.
- **Needs Improvement (2):**
The policy’s purpose or steps are somewhat muddled. Key details are missing or not logically presented.
- **Poor (1):**
The policy is confusing or incoherent, making it difficult to discern the main intent or implementation plan.

### 2. Use of Time Series Insights

- **Excellent (4):**
Policy demonstrates a deep and accurate understanding of time series data, referencing trends, patterns, or anomalies appropriately.
- **Good (3):**
Reasonably interprets time series data, though some patterns or causal relationships may be overlooked.
- **Needs Improvement (2):**
Basic awareness of time series trends is shown, but interpretations are either overly simplistic or partly incorrect.
- **Poor (1):**
No clear incorporation of time series findings. Fails to address changes over time or misinterprets data drastically.

### 3. Feasibility & Practicality

- **Excellent (4):**
The policy includes well-defined implementation steps, realistic budgeting, resource allocation, and timelines.
- **Good (3):**
The policy acknowledges real-world constraints and is mostly feasible, though some details are underdeveloped.
- **Needs Improvement (2):**
The policy lacks key information regarding cost or resource requirements, potentially undermining its practicality.
- **Poor (1):**
The policy is unworkable in practice. No reference to real-world constraints or operational steps.

### 4. Depth of Explanation

- **Excellent (4):**
The proposal offers robust explanations of the causal factors, assumptions, and uncertainties in the time series data.
- **Good (3):**
Explains the data at a moderate level of detail but lacks nuanced analysis of all relevant factors.
- **Needs Improvement (2):**
Superficial explanations, with major causal factors left unaddressed.
- **Poor (1):**
No meaningful explanation of why or how the time series behaves. Lacks substantiation entirely.

### 5. Stakeholder Engagement

- **Excellent (4):**
Identifies key stakeholders, describes outreach and collaboration plans, and proactively addresses potential conflicts.
- **Good (3):**
Acknowledges main stakeholders and suggests some methods of involvement or communication.
- **Needs Improvement (2):**
Limited stakeholder consideration. Engagement strategies are incomplete or too generic.
- **Poor (1):**
Ignores stakeholder perspectives entirely, offering no inclusive or participatory approaches.

### 6. Ethical & Equity Considerations

- **Excellent (4):**
Thoroughly addresses possible ethical concerns, equity impacts, and includes explicit measures to prevent bias.
- **Good (3):**
Recognizes general ethical or equity issues but lacks detail on mitigating strategies.
- **Needs Improvement (2):**
Briefly mentions fairness or equity but provides insufficient concrete steps or analysis.
- **Poor (1):**
Omits any discussion of ethical principles or impact on vulnerable groups.

### 7. Evidence & Justification

- **Excellent (4):**
Cites strong evidence (e.g., peer-reviewed studies, authoritative reports) and clearly connects them to the policy decisions.
- **Good (3):**
References some relevant data or literature. Connections to policy decisions could be more explicit.
- **Needs Improvement (2):**
Minimal references to external evidence. Relies heavily on assumptions without justification.
- **Poor (1):**
No evidence is provided; decisions appear arbitrary or unfounded.

### 8. Measurable Outcomes

- **Excellent (4):**
Proposes specific, quantifiable metrics (e.g., KPIs) and a clear plan for assessing policy outcomes over time.
- **Good (3):**
Suggests some measurable outcomes but lacks full detail on measurement and monitoring processes.
- **Needs Improvement (2):**
Goals are vaguely stated, with no clear success metrics or timelines.
- **Poor (1):**
No mention of how success will be measured or tracked.

### 9. Communication & Transparency

- **Excellent (4):**
Outlines a proactive communication strategy that includes timely updates, open data sharing, and stakeholder-friendly reporting.
- **Good (3):**
Plans for transparency are mentioned but not fully developed or integrated.
- **Needs Improvement (2):**
Vague or minimal communication strategies, potentially limiting public understanding.
- **Poor (1):**
No consideration given to communicating or sharing information about the policy or its results.

### 10. Overall Impact

- **Excellent (4):**
Shows strong potential for significant positive outcomes, scalability, or innovation in addressing time series-related challenges.
- **Good (3):**
Promises moderate positive impact but may lack breadth, scalability, or novel approaches.
- **Needs Improvement (2):**
Policy’s benefits are unclear or limited, with modest impact potential.
- **Poor (1):**
Unlikely to generate any meaningful benefit or has significant negative externalities.

---

## Example of a Scoring Summary

You could design an automated script or prompt logic to calculate a **total score** out of 10×4=4010 \times 4 = 40. For instance:

1. Clarity & Comprehensibility: 3
2. Use of Time Series Insights: 4
3. Feasibility & Practicality: 2
4. Depth of Explanation: 3
5. Stakeholder Engagement: 3
6. Ethical & Equity Considerations: 4
7. Evidence & Justification: 2
8. Measurable Outcomes: 2
9. Communication & Transparency: 3
10. Overall Impact: 3

**Total Score: 29 / 40**

You may then classify overall performance with thresholds, e.g.,

- **Excellent**: 35 – 40
- **Good**: 28 – 34
- **Fair**: 20 – 27
- **Poor**: < 20

---

## Using the Rubric with a Language Model Autograder

1. **Parsing the Generated Policy**:
    - The language model identifies and extracts relevant sections addressing each criterion (Clarity, Feasibility, Ethics, etc.).
2. **Applying Scoring Logic**:
    - It checks for keywords, evidence of depth (e.g., references to data or stakeholder feedback), and clarity of explanation.
3. **Assigning a Score**:
    - The model uses the descriptors to assign a rating (1–4) for each criterion.
4. **Providing Feedback**:
    - The model explains why certain scores were given and suggests improvements (e.g., “Add specific metrics to measure policy success.”).

By systematically applying these **criteria** and **levels** of performance, a language model autograder can provide structured evaluations and detailed feedback for any proposed **public policy** focused on **explaining time series** data."""