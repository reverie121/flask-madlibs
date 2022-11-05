"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text

# Here's a story to get you started

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a far-away {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    ["name",  "subject_pronoun_for_name", "object_pronoun_for_name",  "noun_1", "noun_2", "plural_noun", "adjective", "verb", "verb_ending_with_ing",  "period_of_time", "item_of_clothing"], 
    """{name} was a very {adjective} {noun_1}. Every {period_of_time}, when the {plural_noun} were aligned, {subject_pronoun_for_name} would put on {object_pronoun_for_name} {item_of_clothing} and go {verb_ending_with_ing} until the {noun_2} started to {verb} over the horizon.""")

stories = [story, story2]