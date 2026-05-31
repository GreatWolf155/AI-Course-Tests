input_story = (
    "The little fox saw the little bird and the little cat.",
    "The fox was happy because the little bird sang, and the little cat jumped.",
    "The little fox, the little bird, and the little cat became friends."
)

def most_common_word(story: tuple[str, ...]) -> tuple:
    full_story = ""
    clean_story = []
    story_dict = {}
    for sentence in story:
        full_story += " " + sentence.lower()
    full_story = full_story.strip().split()
    for word in full_story:
        word = "".join(char for char in word if char.isalpha())
        clean_story.append(word)
    common_word = max(set(clean_story), key=clean_story.count)
    return common_word, clean_story.count(common_word)

word, count = most_common_word(input_story)
print(f"{word}\n{count} times")
