#!/usr/bin/env python3
import tomllib
import collections


def main():
    with open("web.toml", "rb") as web:
        data = tomllib.load(web)

        tags = {}
        for site in data:
            for tag in data[site]["tags"]:
                if tag not in tags:
                    tags[tag] = []
                tags[tag].append(site)

    sorted_tags = collections.OrderedDict(sorted(tags.items()))

    with open("header.md", "rt") as header:
        print(header.read())

    print("## Table of Contents")
    for tag in sorted_tags:
        print(f"""- [{tag.title()}](#{tag.replace(" ", "-")})""")

    print()

    for tag, sites in sorted_tags.items():
        print(f"## {tag.title()}")
        for site in sorted(sites):
            print(f"""<details><summary><a href="https://{site}">{site}</a></summary>""")
            print(data[site]["description"].rstrip())
            print("</details>")
        print()


if __name__ == "__main__":
    main()
