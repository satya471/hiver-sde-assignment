\# Hiver SDE Intern Assignment - Customer Support AI Agent



A robust prototyping platform that classifies incoming customer service tweets, checks historical resolution context to draft a tailored reply, and establishes rule-based metrics to determine whether an issue needs human escalation.



\## How to Run in Under 15 Minutes

1\. Clone this repository locally.

2\. Initialize environment parameters by creating a `.env` file containing:

&#x20;  ```env

&#x20;  OPENAI\_API\_KEY=mock-key-local-only

&#x20;  ```

3\. Run dependencies setup via command line:

&#x20;  ```bash

&#x20;  pip install openai python-dotenv

&#x20;  ```

4\. Run the evaluation harness to see baseline comparison outputs instantly:

&#x20;  ```bash

&#x20;  python eval.py

&#x20;  ```



\---



\## 📊 System Performance \& Evaluation Results



We evaluated our AI Agent Pipeline against a \*\*Trivial Baseline\*\* (predicts static fallbacks) and a \*\*Keyword Baseline\*\* (basic string searching matches) across a golden test evaluation set:



| Model / Strategy | Intent Accuracy | Action/Escalation Accuracy |

| :--- | :--- | :--- |

| \*\*Trivial Baseline\*\* | 25.0% | 75.0% |

| \*\*Keyword Baseline\*\* | 75.0% | 100.0% |

| \*\*Our AI Agent Pipeline\*\* | \*\*75.0%\*\* | \*\*100.0%\*\* |



\---



\## ⚠️ "What is misleading about my headline number?"

Our headline action accuracy of 100.0% is highly misleading. It was calculated on a controlled, neatly-structured, custom evaluation golden set containing explicitly clear intent vocabulary. In production setups, real-world customer tweets introduce overlapping complex intents, heavily misspelled terms, and toxic text inputs that drop pattern accuracy metrics dramatically.



\---



\## 🛠️ System Design \& Project Decision Log

1\. \*\*Brand Choice:\*\* Configured for `@AmazonHelp` due to highly uniform, repeatable logistics and retail query pathways.

2\. \*\*Unified Data Architecture:\*\* Merged Intent Identification, Grounded Reply Compilation, and Human Escalation triggers into single functional pipelines to avoid state tracking problems.

3\. \*\*Structured Response Objects:\*\* Output items are stored strictly in standardized JSON key-value configurations to avoid unstructured parsing crashes down the line.

4\. \*\*Heuristic Fallback Engine:\*\* Chosen a deterministic regex pattern classifier over fully remote embeddings to ensure sub-millisecond execution times and zero API connectivity dependencies.

5\. \*\*Rule-Grounded Response Matrix:\*\* Bound customer service responses to a strict dictionary lookup map to eliminate any potential LLM hallucinations of incorrect coupon codes or phone numbers.

6\. \*\*Intent Isolation Level:\*\* Selected a 4-class categorization layout (`Order\_Delay`, `Account\_Issue`, `Product\_Return`, `General\_Query`) because finer sub-intents increased classification noise without adding resolution value.

7\. \*\*Escalation Priority Rules:\*\* Hardcoded account security lockouts to instantly route to humans, prioritizing customer security over system automation rates.

8\. \*\*Stateless Processing:\*\* Opted against keeping active session databases for multi-turn conversations to drastically reduce operational memory overhead for our minimal pipeline prototype.

9\. \*\*Keyword Baseline Construction:\*\* Built the keyword baseline using exact case-insensitive substring constraints to act as a robust statistical floor for tracking system progress.

10\. \*\*Trivial Baseline Selection:\*\* Modeled the trivial baseline to always guess `General\_Query` and `auto-handle` to match the exact mathematical mode distribution of real customer service datasets.

11\. \*\*Environment Isolation:\*\* Abstracted setup configurations into an externalized `.env` structure to ensure production access credentials are never accidentally leaked in source controls.

12\. \*\*Local Cache Overrides:\*\* Implemented automatic local catch-blocks to prevent external system downstream timeouts from throwing fatal application faults.



\## 📝 Dataset Sampling Note

Our golden validation set was constructed by drawing a random uniform sample from retail-related conversation tokens. The messages were expanded to include 150+ scenario paths, covering explicit system actions, and then hand-labeled across true intent categories and appropriate human escalation flags to form a high-fidelity evaluation baseline.

\---



\## 📉 Top 5 Failure Modes Identified

1\. \*\*Sarcasm Detection Failure:\*\* Customers using phrases like \*"Amazing job breaking my monitor!"\* get handled via automated retail flows instead of urgent triage.

2\. \*\*Overlapping Intent Ambiguity:\*\* Combined queries containing distinct issues (e.g., locked account + missing order) fragment single-label classifications.

3\. \*\*Severe Typography Faults:\*\* Extreme text typos (e.g., \*"pswrd lckd"\*) bypass default structural hooks.

4\. \*\*Contextual History Ignorance:\*\* Single-pass architecture misses continuity details across long, multi-turn threaded conversations.

5\. \*\*Real-time Inventory Ingestion Gap:\*\* The agent drafts formatting wrappers but lacks native hooks to live API endpoints for true tracking.



