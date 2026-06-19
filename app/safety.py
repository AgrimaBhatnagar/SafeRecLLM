BLOCKED_TERMS = {
    "violence",
    "weapon",
    "hate",
    "extremism"
}

def filter_results(results):

    safe_rows = []

    for _, row in results.iterrows():

        text = (
            row["title"] +
            " " +
            row["description"]
        ).lower()

        if not any(
            term in text
            for term in BLOCKED_TERMS
        ):
            safe_rows.append(row)

    return safe_rows
