def mablibs():
    start = 1
    while start == 1:
        story_template = (
            "It was a {adj1} and {adj2} morning when I woke up to the sound of a "
            "{noun1}. I immediately jumped out of bed and {verb1} across the room. "
            "Suddenly, a wild {noun2} appeared and started to {verb2} right on my desk!"
        )

        d = {"adj1": "", "adj2": "", "noun1":"", "verb1": "","noun2": "", "verb2": ""}
        q = list(d.keys())
        for i in q:
            ans = input(i + ":")
            d[i] = ans
        final = story_template.format(**d)
        print(final)

        start = int(input("If you want to play again, press 1, or press 0 to stop the game: "))

if __name__ == "__main__":
    mablibs()