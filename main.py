import os
import re

INDEX_TEMPLATE_TOP = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>College DB</title>
    <link rel="stylesheet" href="css/styles.css">
    <link rel="stylesheet" href="css/index.css">
</head>
<body>

    <header class="head">
        <nav class="title">
            <a href="index.html"><h1>College DB</h1></a>
        </nav>
    </header>
    
    <div class="container">    

        <div class="body">

            <main>
"""

INDEX_TEMPLATE_BOTTOM = """
            </main>

        </div>
        
    </div>
</body>
</html>"""

INDEX_TEMPLATE_EMOJI = """
                <a href="$filename$.html"><div class="box">
                    <h2 class="emoji">$emoji$</h1>
                    <h3>$name$</h3>
                </div></a>
"""

INDEX_TEMPLATE_IMAGE = """
                <a href="$filename$.html"><div class="box">
                    <img class="logo" src="images/$imgname$">
                    <h3>$name$</h3>
                </div></a>
"""

PAGE_TEMPLATE_TOP = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$name$</title>
    <link rel="stylesheet" href="css/styles.css">
    <link rel="stylesheet" href="css/pages.css">
</head>
<body>
    
    <header class="head">
        <nav class="title">
            <a href="index.html"><h1>College DB</h1></a>
        </nav>
    </header>

    <div class="container">

        <div class="body">

            <h2 class="heading">$heading$</h2>

            <main>
"""

PAGES_TEMPLATE_LINK = """
                <a href="$link$" target="_blank"><div class="box">
                    <img class="logo" src="images/$boxImgName$">
                    <h3>$newsletterName$</h3>
                </div></a>
"""


def convertToName(filename):
    filename = re.sub("([a-z])([A-Z])","\g<1> \g<2>", filename)
    return filename[0].capitalize() + filename[1:]

def main():
    inputPath = "./input"
    outputPath = "./res"

    inputFiles = os.listdir(inputPath)

    # The way this works is that it opens each .md file and generates the html for it.
    # At the same time it adds a link to generated page in the index.html

    # Begin with the index.html
    indexContent = INDEX_TEMPLATE_TOP

    # For each input file
    for filename in inputFiles:
        # Check if it is a .md file
        if filename.endswith(".md"):
            filePath = os.path.join(inputPath, filename)

            filename = os.path.splitext(filename)[0]

            # Begin generating the page for the specific .md file
            pageContent = PAGE_TEMPLATE_TOP
            pageContent = pageContent.replace("$filename$", filename)


            link = []
            # Open the file
            with open(filePath, 'r') as myFile:
                print(f"Opened {filePath}")
                # For each line
                for line in myFile:
                    # Extract info
                    line = line.replace('\n', '').strip()
                    # Emoji
                    if line.startswith("$emoji:"):
                        emoji = line.split(":", 1)[1].strip()
                        if emoji == "-":
                            emoji = None
                    # Image
                    elif line.startswith("$imgname:"):
                        imgname = line.split(":", 1)[1].strip()
                        if imgname == "-":
                            imgname = None
                    # Heading
                    elif line.startswith("#"):
                        heading = line.lstrip("#").strip()
                    # Link (Text, link, image)
                    elif line.startswith("-"):
                        line = line.lstrip("-").strip()
                        link = line.split("@")

                        for i in range(0, len(link)):
                            link[i] = link[i].strip()

                        # If the line in the .md file contains a link
                        # Add a template of how the link should look in the page and replace placeholders
                        pageContent += PAGES_TEMPLATE_LINK
                        pageContent = pageContent.replace("$newsletterName$", link[0])
                        pageContent = pageContent.replace("$link$", link[1])
                        pageContent = pageContent.replace("$boxImgName$", link[2].strip())
            
                        if link != []:
                            print(f"Link: {link}\n")

            
            print(f"Filename: {filename}")
            print(f"Emoji: {emoji}")
            print(f"Image Name: {imgname}")
            print(f"Heading: {heading}")

            # Add the emoji OR image to the entry in index.html for the specific .md file
            if emoji != None:
                tmpVar = INDEX_TEMPLATE_EMOJI
                tmpVar = tmpVar.replace("$emoji$", emoji)
            elif imgname != None:
                tmpVar = INDEX_TEMPLATE_IMAGE
                tmpVar = tmpVar.replace("$imgname$", imgname)
            
            # Add the text to the entry in index.html for the specific .md file
            tmpVar = tmpVar.replace("$filename$", filename)
            tmpVar = tmpVar.replace("$name$", convertToName(filename))
            indexContent += tmpVar

            # Add the heading to the page for the specific .md file
            pageContent = pageContent.replace("$heading$", heading)
            pageContent = pageContent.replace("$name$", convertToName(filename))

            # We have read the entire .md file
            # Add the bottom part of the page to the generated html file
            pageContent += INDEX_TEMPLATE_BOTTOM


            # Write the generated html file to the output folder
            outputFilePath = os.path.join(outputPath, filename + ".html")
            with open(outputFilePath, 'w') as outputFile:
                outputFile.write(pageContent)
            print(f"New Page {convertToName(filename)}\n")
            print(pageContent)
            print(f"Written to {filename+'.html'}\n\n")
    
    # We have read all the .md files
    # Add the bottom part of the index.html
    # Write the generated index.html to the output folder
    indexContent += INDEX_TEMPLATE_BOTTOM
    outputFilePath = os.path.join(outputPath, "index.html")
    with open(outputFilePath, 'w') as outputFile:
        outputFile.write(indexContent)
    print(indexContent)
    print("Written to index.html")


if __name__ == "__main__":
    main()