# name_matcher.py

from rapidfuzz import fuzz, process

def normalize_name(name: str) -> str:
    """Basic normalization: strip, lower‐case, remove extra spaces."""
    return " ".join(name.strip().lower().split())

def build_name_list(raw_list):
    """Normalize each name in the list and return unique list."""
    normalized = [normalize_name(n) for n in raw_list]
    # Remove duplicates while preserving order
    seen = set()
    uniq = []
    for n in normalized:
        if n not in seen:
            seen.add(n)
            uniq.append(n)
    return uniq

def find_best_match(input_name: str, name_list, top_n=5):
    """Given an input name and a list of candidate names, return the best match + a ranked list of top_n matches."""
    input_norm = normalize_name(input_name)
    # Use process.extract which gives you list of (candidate, score, index)
    results = process.extract(
        input_norm,
        name_list,
        scorer=fuzz.token_sort_ratio,
        limit=top_n
    )

    # Best match is first result
    best_match, best_score, best_idx = results[0]
    return best_match, best_score, results

def main():
    # Example dataset of names (at least ~30 names)
    raw_names = [
        "Geetha", "Gita", "Gitu", "Geeta", "Geetha Reddy",
        "Githa", "Geetha Smith", "Geetha Kumar", "Getha", "Geethaa",
        "Gita Rao", "Geeta Rao", "Gita K", "Githa Rao", "Geitha",
        "Geetha Devi", "Gita Devi", "Geetu", "Geethu", "Getha Reddy",
        "Geetha Reddy Rao", "Geethaa Reddy", "Gita Reddy", "Geeta Reddy",
        "Gita Reddy Kumar", "Geetha K", "Geitha K", "Geethu K", "Gitu K",
        "Githa Kumar", "Gita Kumar", "Geeta Kumar", "Geetha Kumar Rao"
    ]

    name_list = build_name_list(raw_names)

    print("Dataset of names:")
    for n in name_list:
        print("  ", n)
    print()

    while True:
        user_input = input("Enter a name (or ‘quit’ to exit): ").strip()
        if user_input.lower() == 'quit':
            break

        best_match, best_score, ranked_list = find_best_match(user_input, name_list, top_n=10)

        print(f"\nInput Name : {user_input}")
        print(f"Best Match : {best_match} (score {best_score}%)")
        print("Other Top Matches:")
        for cand, score, idx in ranked_list:
            print(f"  {cand} — {score}%")
        print()

if __name__ == "__main__":
    main()
