"""FAQ tab."""

from __future__ import annotations

import gradio as gr

from config import DATASET_URL, DISCUSSIONS_URL

FAQ_ITEMS = [
    (
        "Who can participate?",
        "Anyone with a Hugging Face account can participate - data scientists, ML engineers, clinicians, "
        "students, and citizen scientists alike. You must be at least 18 years old. See the **Official Rules** "
        "tab for details.",
    ),
    (
        "Can I participate in both tracks?",
        "Yes. Track 1 and Track 2 are scored independently. You can submit to one or both.",
    ),
    (
        "Can I participate as a team?",
        "Yes.\n\nEach team member must register individually with their own Hugging Face account. For Track 1, each "
        "team member may submit independently and your best score counts. For Track 2, designate one person to submit "
        "on the team's behalf - only one Track 2 submission per team is accepted, and additional submissions from "
        "other team members will be ignored.",
    ),
    (
        "How is Track 1 scored?",
        "Submissions are scored the way large-scale rare disease benchmarks (like Stenton et al., 2024) score solved "
        "cases applied to this single, clinically confirmed answer.\n\nTwo metrics are computed automatically: **rank points** "
        "(based on how high the true variant(s) land in your ranked list, with partial credit if you recover only one of "
        "two compound-heterozygous variants) and **F-max** (the best precision/recall balance across your submitted"
        "confidence thresholds).",
    ),
    (
        "Are secondary or incidental findings scored?",
        "They won't hurt your automated Track 1 score — include them as additional rows if you'd like. They're set aside "
        "for qualitative review by the judging panel rather than folded into the automated rank points/F-max calculation, "
        "since there's no fixed \"correct\" answer for secondary findings the way there is for the primary causal variant.\n\n"
        "Use the optional `notes` column to briefly explain why you're flagging it (e.g. \"well-established pathogenic "
        "variant, unrelated to primary phenotype, recommend clinical follow-up\")",

    ),
    (
        "How is Track 2 scored?",
        "Reports are reviewed by an independent panel, and will be judged on scientific rigor, potential impact, innovation, "
        "and scalability.",
    ),
    (
        "How many submissions can I make?",
        "Track 1 allows up to **6 submissions** per participant; only your highest-scoring submission appears on the "
        "leaderboard. Track 2 accepts **one final submission** per participant. No re-submissions allowed, so make "
        "them count.",
    ),
    (
        "What compute resources are available?",
        "This Space runs on CPU-basic hardware. You are welcome to use your own compute for training, as only "
        "the final submission files need to be uploaded here.",
    ),
    (
        "What is the data license?",
        "The underlying dataset is **gated** and subject to the terms of the Hackathon Rules and Data Transfer Agreement "
        "- access requires approval, redistribution is prohibited, and all data must be deleted upon conclusion of the "
        "Hackathon.\n\nParticipant submissions and results (predictions, code, reports) are released under **CC BY 4.0** and "
        "may be reused with attribution.",
    ),
    (
        "When will results be announced?",
        "Final rankings will be announced after the ~2-3 month judging window closes. The exact date will be posted in the "
        f"[Community tab]({DISCUSSIONS_URL}).",
    ),
    (
        "I have a question not answered here.",
        f"Post in the [Discussions tab]({DISCUSSIONS_URL}) and the community or organizers will respond!",
    ),
]


def render() -> None:
    with gr.Tab("FAQ"):
        gr.Markdown("## Frequently Asked Questions")
        for question, answer in FAQ_ITEMS:
            with gr.Accordion(question, open=False, elem_classes=["faq-accordion"]):
                gr.Markdown(answer)
        gr.HTML('<div class="back-to-top-row"><a class="back-to-top" href="javascript:void(0)" onclick="document.getElementById(\'page-top\').scrollIntoView({behavior:\'smooth\'})">↑ Back to top</a></div>')
