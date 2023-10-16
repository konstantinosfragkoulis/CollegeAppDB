# CollegeAppDB
A website with links to the most valuable resources for high school students preparing for college.

# Usage
### Clone the repo
`git clone https://github.com/konfrag4/CollegeAppDB.git`

### Edit the files in the `input` directory
Create a new markdown file to create a new page on the website.
The files are made with this template:

```
$emoji: <EMOJI>
$imgname: <FRONT_PAGE_IMAGE_NAME.EXTENSION>

# <HEADING>

- <LINK_TEXT> @ <LINK> @ <IMAGE_NAME.EXTENSION> @ <IMAGE_DESCRIPTION>
- <LINK_TEXT> @ <LINK> @ <IMAGE_NAME.EXTENSION> @ <IMAGE_DESCRIPTION>
- <LINK_TEXT> @ <LINK> @ <IMAGE_NAME.EXTENSION> @ <IMAGE_DESCRIPTION>
- <LINK_TEXT> @ <LINK> @ <IMAGE_NAME.EXTENSION> @ <IMAGE_DESCRIPTION>
- <LINK_TEXT> @ <LINK> @ <IMAGE_NAME.EXTENSION> @ <IMAGE_DESCRIPTION>
```
New images must be placed in `res/images`.
While you can use any image format, it is recommended to use `.webp` images for the best performance.
`<IMAGE_DESCRIPTION>` is followed by "Logo". So if `<IMAGE_DESCRIPTION>` is "MIT", the alt text will be "MIT Logo".

### Generate the new HTML files
`res`, `res/css`, and `res/images` MUST BE PRESENT!

Run `python3 src/main.py`
