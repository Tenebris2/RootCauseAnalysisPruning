from pprint import pprint

with open("static-data/collected_targets.md", "r") as file:
    contents = [x.strip().split(" - ") for x in file.readlines()]
with open("static-data/collected_targets.bib", "w") as bibfile:
    for c in contents:
        target = c[0].strip()
        cause = c[1]
        id = c[2]
        url_link = c[3]
        key = target + "".join(cause.split())
        title = target.capitalize() + " " + cause + f"({id})."

        bibtex_entry = f"""
        @misc{{{key},
          title = {{{title}}},
          howpublished = {{\\url{{{url_link}}}}},
        }}
        """

        bibfile.write(bibtex_entry)
