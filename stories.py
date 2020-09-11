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

    def __init__(self, title, words, text):
        """Create story with words and template text."""
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

tales = [Story("Once Upon a time...",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. He loved to {verb} {plural_noun}."""
),

Story("Halloween Story",
["weather","name_town","costume","costume_2","character","greeting","adjective","place","candy","candy_2"],
"""On a {weather} Halloween in the town of {name_town}, I was going to go trick or treating. 
I decided to dress up as a {costume} but everyone thought I would scare people, 
so I decide to dress up as a {costume_2} instead. My {costume_2} costume was done to perfection 
and I looked great. The first door I knocked on turned out to be the home of {character}. 
opened the door and said, "{greeting}". I tried to utter the words, "trick or treat" but I was very {adjective}. 
{character} said, "come in". I said, no way and ran as fast as I could for the {place}. I didn't get any {candy} or 
{candy_2} for Halloween that year.
"""
),

Story('Gingerbread',
    ["plural_noun","person","adjective","noun","adjective_2","adjective_3","adjective_4","color","body_part","body_part_2","clothing"],
    """
    Gingerbread {plural_noun}, which are usually shaped like a {person} are a popular
    Christmas treat. Giner is {adjective} {noun} that gives gingerbread its 
    {adjective_2} flavor. Molasses is a {adjective_3} ingredient that gives the cookies 
    their traditional dark {adjective_4} color. After baking, decorate using {color},
    frosting to draw {body_part}, {body_part_2}, and {clothing} onto the gingerbread
    people.
    """
)
]