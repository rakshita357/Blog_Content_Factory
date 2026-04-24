import json
import re


def extract_json(text: str) -> dict:
    """
    Extract JSON from LLM response safely
    """

    # try direct json
    try:
        return json.loads(text)
    except:
        pass

    # try markdown ```json blocks
    pattern = r"```(?:json)?\s*([\s\S]*?)```"
    match = re.search(pattern, text)

    if match:
        try:
            return json.loads(match.group(1))
        except:
            pass

    # try first { ... }
    pattern = r"\{[\s\S]*\}"
    match = re.search(pattern, text)

    if match:
        try:
            return json.loads(match.group())
        except:
            pass

    raise ValueError("No valid JSON found in response")


def count_words(text: str) -> int:
    """
    Count words in text
    """
    return len(text.split())


def format_sources(sources: list) -> str:
    """
    Format sources for display
    """
    if not sources:
        return ""

    lines = ["\n\n---\n### Sources:\n"]

    for i, s in enumerate(sources, 1):
        title = s.get("title", "Source")
        url = s.get("url", "#")

        lines.append(f"{i}. [{title}]({url})")

    return "\n".join(lines)