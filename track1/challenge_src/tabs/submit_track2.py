"""Submit tab for Track 2."""

from __future__ import annotations

import io
import json
import os
from datetime import datetime, timezone
from pathlib import Path

import gradio as gr

from config import LEADERBOARD_DATASET, TRACK2_SUBMISSIONS_FOLDER
from utils import _LOCAL_DEV_DIR, _sanitize, get_hf_username, hf_username_to_display_slug

INTRO_MD = """
Upload your Track 2 proposal here for review by our independent expert judging panel. Unlike Track 1,
this track uses qualitative evaluation rather than automated scoring.

Only <u>one submission</u> is accepted for this track.

**Team Participation:** Please designate a single team member to submit on the team's behalf. Additional
or duplicate submissions from other team members will not be reviewed.
"""

INSTRUCTIONS_MD = """
### 1. Write your report.

Prepare a written report (PDF or Markdown) proposing repositioned drug candidates supported by your
analysis. Include a characterization of the variant's mechanism (loss-of-function / gain-of-function,
pathway disrupted, downstream biological consequence) as the basis for your repurposing rationale.

Not sure what details to include? Please use the provided methods description template to organize your
analysis and supporting materials, then export your report as a PDF or Markdown file for submission.

When saving your report, please include your username (or team name) in the filename. For example, if your
HF username is `jane-doe`, you might name your report file:

* `jane-doe_track2_report.pdf` (`.md` also accepted)

### 2. Prepare other supporting materials.

* Push documented, reproducible code to a public GitHub repository.
* Record a 3-minute pitch video walking through your reasoning and proposed candidates and upload it to
  YouTube or Vimeo.

### 3. After submission:

The independent panel will review all entries over a ~2-3 month window. Results will be announced at a
later date.
"""

def _save_track2_submission(entry: dict, report_path: str) -> None:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S_%f")
    safe_user = _sanitize(entry.get("hf_username", "unknown"))
    subfolder = f"{TRACK2_SUBMISSIONS_FOLDER}{safe_user}/"
    filename = f"sub_{timestamp}.json"
    payload = json.dumps(entry, indent=2).encode()
    token = os.environ.get("HF_TOKEN")
    if token:
        from huggingface_hub import upload_file
        upload_file(
            path_or_fileobj=io.BytesIO(payload),
            path_in_repo=f"{subfolder}{filename}",
            repo_id=LEADERBOARD_DATASET,
            repo_type="dataset",
            token=token,
            commit_message=f"track2: {entry.get('display_name', entry.get('hf_username', '?'))}",
        )
        upload_file(
            path_or_fileobj=report_path,
            path_in_repo=f"{subfolder}{entry['report_filename']}",
            repo_id=LEADERBOARD_DATASET,
            repo_type="dataset",
            token=token,
            commit_message=f"track2 report: {entry.get('display_name', entry.get('hf_username', '?'))}",
        )
    else:
        local_dir = _LOCAL_DEV_DIR / "track2_submissions" / safe_user
        local_dir.mkdir(parents=True, exist_ok=True)
        (local_dir / filename).write_bytes(payload)
        import shutil
        shutil.copy(report_path, local_dir / entry['report_filename'])

def _track2_submissions_by_user(hf_username: str) -> int:
    """Count Track 2 submissions for a given HF user."""
    safe_user = _sanitize(hf_username)
    token = os.environ.get("HF_TOKEN")
    if token:
        from huggingface_hub import HfApi
        api = HfApi()
        try:
            return sum(
                1 for f in api.list_repo_files(
                    LEADERBOARD_DATASET, repo_type="dataset", token=token
                )
                if f.startswith(f"{TRACK2_SUBMISSIONS_FOLDER}{safe_user}/sub_") and f.endswith(".json")
            )
        except Exception:
            return 0
    # Local dev fallback
    local_dir = _LOCAL_DEV_DIR / "track2_submissions" / safe_user
    if not local_dir.exists():
        return 0
    return sum(1 for _ in local_dir.glob("sub_*.json"))


def _submission_status(request: gr.Request, oauth_profile: gr.OAuthProfile | None = None) -> str:
    hf_username = get_hf_username(request, oauth_profile)
    if not hf_username:
        return ""
    count = _track2_submissions_by_user(hf_username)
    if count >= 1:
        return '<div class="info-card quota-card">✅ <strong>Track 2 submission received.</strong> Only one submission per team is accepted.</div>'
    return '<div class="info-card quota-card"><strong>0 / 1</strong> submissions used &nbsp;·&nbsp; <strong>1</strong> remaining</div>'


def _handle_submit(
    display_name_input: str,
    github_url: str,
    video_url: str,
    report_file,
    notes: str,
    request: gr.Request,
    oauth_profile: gr.OAuthProfile | None = None,
) -> str:
    hf_username = get_hf_username(request, oauth_profile)
    if not hf_username:
        return "⚠️ Please sign in with your Hugging Face account to submit."

    display_name = (display_name_input or "").strip() or hf_username_to_display_slug(hf_username)

    count = _track2_submissions_by_user(hf_username)
    if count >= 1:
        return "⚠️ You have already submitted a Track 2 entry. Only one submission per participant is accepted."

    github_url = (github_url or "").strip()
    if not github_url.startswith("https://github.com/"):
        return "⚠️ GitHub URL must start with `https://github.com/`."
    video_url = (video_url or "").strip()
    if not video_url:
        return "⚠️ A pitch video URL is required. Please upload your 3-minute video to YouTube or Vimeo and paste the link."
    if report_file is None:
        return "⚠️ Please upload your report (PDF or Markdown)."

    report_path = report_file if isinstance(report_file, str) else report_file.name
    if Path(report_path).suffix.lower() not in {".pdf", ".md"}:
        return "⚠️ Report must be a PDF (.pdf) or Markdown (.md) file."

    report_name = Path(
        report_file if isinstance(report_file, str) else report_file.name
    ).name

    entry = {
        "hf_username": hf_username,
        "display_name": display_name,
        "github_url": github_url,
        "video_url": (video_url or "").strip(),
        "report_filename": report_name,
        "notes": (notes or "").strip(),
        "submitted_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    }
    _save_track2_submission(entry, report_path)

    video_line = f"[{entry['video_url']}]({entry['video_url']})" if entry["video_url"] else "_(not provided)_"

    return f"""
## Track 2 submission received ✓

**{display_name}** (`{hf_username}`)

Your submission has been logged and will be reviewed by the expert judging panel over the
~2-3 month judging window. Results will be announced after the judging period closes.

**What you submitted:**
- GitHub repository: [{github_url}]({github_url})
- Video: {video_line}
- Report file: `{report_name}`
""".strip()


def render() -> None:
    with gr.Tab("Submit - Track 2") as tab:
        gr.Markdown(INTRO_MD)
        status_md = gr.HTML()
        with gr.Accordion("📋 Submission Format & Instructions", open=True, elem_classes=["faq-accordion"]):
            gr.Markdown("**Templates:**")
            with gr.Row():
                gr.DownloadButton(
                    label="📄 Methods description template (Excel)",
                    value="static/templates/methods_description_form.xlsx",
                    size="sm",
                    elem_classes=["template-dl-btn"],
                )
            gr.Markdown(INSTRUCTIONS_MD)
        gr.Markdown("---")
        with gr.Row():
            with gr.Column():
                team_name_box = gr.Textbox(
                    label="Team / Display Name (optional)",
                    placeholder="e.g. helix-squad",
                    info="This will be used for the public announcement. Leave blank to use your "
                         "HF username if you are participating individually.",
                )
                github_box = gr.Textbox(
                    label="GitHub repo URL *",
                    placeholder="https://github.com/your-org/your-repo",
                )
                video_box = gr.Textbox(
                    label="Pitch video URL *",
                    placeholder="https://youtu.be/...",
                )
                notes_box = gr.Textbox(
                    label="Notes for judges (optional)",
                    lines=3,
                    placeholder="Anything you want judges to know before they open your submission…",
                )
            with gr.Column():
                report_file = gr.File(
                    label="Report file (PDF or Markdown) *",
                    file_types=[".pdf", ".md"],
                )
        submit_btn = gr.Button("Submit", variant="primary")
        result_md = gr.Markdown(label="Confirmation")
        submit_btn.click(
            fn=_handle_submit,
            inputs=[team_name_box, github_box, video_box, report_file, notes_box],
            outputs=result_md,
        )
        tab.select(fn=_submission_status, inputs=[], outputs=status_md)
    return status_md
