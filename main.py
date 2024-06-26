# -*- coding: utf-8 -*-

import itertools
import os
import re
import sys

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, "lib"))

from flowlauncher import FlowLauncher

class KillerSudokuCalc(FlowLauncher):

    def query(self, query):
        values = [int(part) for part in re.split(r"\s+", query) if part.isdigit()]

        numbers = list(range(1, 10))
        total = values[0] if len(values) > 0 else 0
        cells = values[1] if len(values) > 1 else 0
        exclude = [num for num in values[2:] if num < 10]

        if exclude:
            numbers = [num for num in numbers if num not in exclude]

        results = []

        if len(values) == 1:
            results = [{
                "Title": f"Looking for a total of {total} in how many cells?",
                "Subtitle": "Type in the total value, the number of cells and optionally the numbers to exclude, all separated by spaces",
                "IcoPath": "icon-search.png",
            }]
        elif len(values) > 1:
            subtitle = f"summing up to a cage total of {total} in {cells} cells"
            if exclude:
                subtitle += f", excluding {','.join(map(str, exclude))}"

            possibleCombinations = itertools.combinations(numbers, cells)
            validCombinations = [combination for combination in possibleCombinations if sum(combination) == total]

            for c in validCombinations:
                results.append({
                    "Title": f"{' - '.join(map(str,c))}",
                    "Subtitle": subtitle,
                    "IcoPath": "icon-valid.png",
                })

            if len(validCombinations) < 1:
                results = [{
                    "Title": "There are no valid combinations",
                    "Subtitle": subtitle,
                    "IcoPath": "icon-invalid.png",
                }]

        return results


if __name__ == "__main__":
    KillerSudokuCalc()