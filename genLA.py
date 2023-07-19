def genLAs(k):
    potentialColors = ["blue", "red", "green", "yellow", "purple"]
    currentLAs = [["blue", "red"]]
    for _ in range(1, k-1):
        longerLAs = []
        for LA in currentLAs:
            # repeat an already used color
            usedColors = set()
            usedColors.update(LA)
            for col in usedColors:
                if col != LA[-1]:
                 longerLAs.append(LA + [col])
            # or add a new color
            newCol = list(c for c in potentialColors if c not in LA)[0]
            longerLAs.append(LA + [newCol])
        currentLAs = longerLAs
    return currentLAs

def nicePrint(lst):
    for l in lst:
        colors = set()
        colors.update(l)
        if len(colors) == 2:
            pl = str(l) + " <- only two colors"
        elif len(colors) > 3:
            pl = str(l) + " <- ≥3 colors"
        else:
            pl = str(l)
        print(pl)

if __name__ == "__main__":
    fourVert = genLAs(4)
    fiveVert = genLAs(5)

    print(f"For four vertices, there are {len(fourVert)} quasi-discriminating labelings, where the unfixed side of N_(4) are labeled with:")
    nicePrint(fourVert)
    print("from top to bottom, respectively.\n")

    print(f"For five vertices, there are {len(fiveVert)} quasi-discriminating labelings, where the unfixed side of N_(5) are labeled with:")
    nicePrint(fiveVert)
    print("from top to bottom, respectively.\n")