import os
import re

INDEX_TEMPLATE_TOP = """
<!DOCTYPE html>
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
</html>
"""

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

PAGE_TEMPLATE_TOP = """
<!DOCTYPE html>
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
    outputFiles = os.listdir(outputPath)

    indexContent = INDEX_TEMPLATE_TOP

    for filename in inputFiles: # Open each input file
        if filename.endswith(".md"):
            filePath = os.path.join(inputPath, filename)

            filename = os.path.splitext(filename)[0]

            pageContent = PAGE_TEMPLATE_TOP.strip()

            link = []

            with open(filePath, 'r') as myFile:
                print(f"Opened {filePath}")
                for line in myFile:
                    line = line.replace('\n', '').strip() # Remove newline
                    if line.startswith("$emoji:"):
                        emoji = line.split(":", 1)[1].strip()
                        if emoji == "-":
                            emoji = None
                    elif line.startswith("$imgname:"):
                        imgname = line.split(":", 1)[1].strip()
                        if imgname == "-":
                            imgname = None
                    elif line.startswith("#"):
                        heading = line.lstrip("#").strip()
                    elif line.startswith("-"):
                        line = line.lstrip("-").strip()
                        link = line.split("@")

                        if pageContent == PAGE_TEMPLATE_TOP.strip():
                            pageContent = pageContent.replace("$filename$", filename)
                            pageContent = pageContent.replace("$name$", convertToName(filename))
                            pageContent = pageContent.replace("$heading$", heading)

                        pageContent += PAGES_TEMPLATE_LINK
                        pageContent = pageContent.replace("$newsletterName$", link[0])
                        pageContent = pageContent.replace("$link$", link[1])
                        pageContent = pageContent.replace("$boxImgName$", link[2].strip())

            
            print(f"Filename: {filename}")
            print(f"Emoji: {emoji}")
            print(f"Image Name: {imgname}")
            print(f"Heading: {heading}")
            if link != []:
                print(f"Link: {link}\n")

            if emoji != None:
                tmpVar = INDEX_TEMPLATE_EMOJI
                tmpVar = tmpVar.replace("$emoji$", emoji)
            elif imgname != None:
                tmpVar = INDEX_TEMPLATE_IMAGE
                tmpVar = tmpVar.replace("$imgname$", imgname)
            
            tmpVar = tmpVar.replace("$filename$", filename)
            tmpVar = tmpVar.replace("$name$", convertToName(filename))
            indexContent += tmpVar

            pageContent = pageContent.replace("$heading$", heading)
            
            pageContent += INDEX_TEMPLATE_BOTTOM


            outputFilePath = os.path.join(outputPath, filename + ".html")
            with open(outputFilePath, 'w') as outputFile:
                outputFile.write(pageContent)
                print(f"New Page {convertToName(filename)}")
                print(f"Written to {filename+'.html'}\n\n")
    
    indexContent += INDEX_TEMPLATE_BOTTOM
    outputFilePath = os.path.join(outputPath, "index.html")
    with open(outputFilePath, 'w') as outputFile:
        outputFile.write(indexContent)
        print(indexContent)
        print("Written to index.html")


if __name__ == "__main__":
    main()
