"""Leaderboard tab for Track 1."""

from __future__ import annotations

import gradio as gr

from config import LEADERBOARD_HEADERS, CHALLENGE_ACTIVE
from utils import leaderboard_df

LEADERBOARD_MD = """
## Track 1 Leaderboard

Rankings update automatically as valid Track 1 submissions are scored. Only your team's highest-scoring
submission is displayed.

**Metrics:** Rank Points & F-max (adapted from _Stenton et al., 2024_)
"""


def render() -> None:
    with gr.Tab("Leaderboard"):
        gr.Markdown(LEADERBOARD_MD)
        lb_table = gr.Dataframe(
            value=leaderboard_df,
            headers=LEADERBOARD_HEADERS,
            datatype=["str"] * 6,
            interactive=False,
            wrap=True,
            every=60 if CHALLENGE_ACTIVE else None,
        )
        refresh_btn = gr.Button("↻ Refresh leaderboard", variant="secondary", size="sm")
        refresh_btn.click(fn=leaderboard_df, inputs=[], outputs=lb_table)
