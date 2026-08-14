"""
Builds a real, sourced instruction-tuning dataset for fine-tuning Qwen3 on
AI/ML research-assistant tasks — basics through advanced, including CV/VLM.

Sources:
- MMLU (cais/mmlu): real exam-style Q&A across ML, CS, and logic subjects
- arXiv abstracts (live API): recent CV/VLM/ML papers, reformatted as
  cited research-summary pairs matching AutoLab AI's report format

This is a genuinely sourced dataset (not hand-authored), documented as such
in the README — appropriate scale/scope for a portfolio QLoRA fine-tune.
"""
import json
import random
import arxiv
from datasets import load_dataset

random.seed(42)

MMLU_SUBJECTS = [
    "machine_learning",
    "college_computer_science",
    "high_school_computer_science",
    "computer_security",
    "formal_logic",
    "electrical_engineering",
    "college_mathematics",
]

ARXIV_QUERIES = [
    "vision language model",
    "computer vision deep learning",
    "convolutional neural network image classification",
    "transformer attention mechanism",
    "reinforcement learning",
    "large language model fine-tuning",
    "object detection",
    "image segmentation",
    "multimodal learning",
    "self-supervised learning",
]

ARXIV_PER_QUERY = 40  # 10 queries x 25 = ~250 arXiv-sourced examples


def build_mmlu_examples():
    examples = []
    for subject in MMLU_SUBJECTS:
        print(f"Loading MMLU subject: {subject}...")
        ds = load_dataset("cais/mmlu", subject, split="test")
        for row in ds:
            question = row["question"]
            choices = row["choices"]
            correct_idx = row["answer"]
            correct_answer = choices[correct_idx]

            instruction = f"Write a research report answering: {question}"
            output = (
                f"# Research Report: {question}\n\n"
                f"## Findings\n\n"
                f"The correct answer is: {correct_answer}. This reflects "
                f"established understanding in the subject area of "
                f"{subject.replace('_', ' ')}. [1]\n\n"
                f"## Sources\n\n"
                f"[1] MMLU benchmark — {subject.replace('_', ' ')} subject area"
            )
            examples.append({"instruction": instruction, "output": output})
    return examples


def build_arxiv_examples():
    examples = []
    client = arxiv.Client()

    for query in ARXIV_QUERIES:
        print(f"Fetching arXiv papers for: {query}...")
        search = arxiv.Search(
            query=query,
            max_results=ARXIV_PER_QUERY,
            sort_by=arxiv.SortCriterion.Relevance,
        )
        for result in client.results(search):
            title = result.title.strip().replace("\n", " ")
            abstract = result.summary.strip().replace("\n", " ")
            authors = ", ".join([a.name for a in result.authors[:3]])

            instruction = f"Write a research report summarizing recent work on: {title}"
            output = (
                f"# Research Report: {title}\n\n"
                f"## Findings\n\n{abstract} [1]\n\n"
                f"## Sources\n\n"
                f"[1] {title} — {authors} ({result.published.year}), arXiv:{result.get_short_id()}"
            )
            examples.append({"instruction": instruction, "output": output})

    return examples


def format_for_training(examples):
    return [
        {"text": f"<|user|>\n{ex['instruction']}\n<|assistant|>\n{ex['output']}"}
        for ex in examples
    ]


if __name__ == "__main__":
    print("=== Building MMLU examples ===")
    mmlu_examples = build_mmlu_examples()
    print(f"Collected {len(mmlu_examples)} MMLU examples")

    print("\n=== Building arXiv examples ===")
    arxiv_examples = build_arxiv_examples()
    print(f"Collected {len(arxiv_examples)} arXiv examples")

    all_examples = mmlu_examples + arxiv_examples
    random.shuffle(all_examples)

    print(f"\nTotal examples before split: {len(all_examples)}")

    formatted = format_for_training(all_examples)

    # 90/10 train/eval split
    split_idx = int(len(formatted) * 0.9)
    train_data = formatted[:split_idx]
    eval_data = formatted[split_idx:]

    with open("scripts/training_data.jsonl", "w", encoding="utf-8") as f:
        for item in train_data:
            f.write(json.dumps(item) + "\n")

    with open("scripts/eval_data.jsonl", "w", encoding="utf-8") as f:
        for item in eval_data:
            f.write(json.dumps(item) + "\n")

    print(f"\nSaved {len(train_data)} training examples -> scripts/training_data.jsonl")
    print(f"Saved {len(eval_data)} eval examples -> scripts/eval_data.jsonl")