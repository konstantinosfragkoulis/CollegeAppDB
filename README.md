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

- <LINK_TEXT> @ <LINK> @ <IMAGE_NAME.EXTENSION>
- <LINK_TEXT> @ <LINK> @ <IMAGE_NAME.EXTENSION>
- <LINK_TEXT> @ <LINK> @ <IMAGE_NAME.EXTENSION>
- <LINK_TEXT> @ <LINK> @ <IMAGE_NAME.EXTENSION>
- <LINK_TEXT> @ <LINK> @ <IMAGE_NAME.EXTENSION>
```
New images must be placed in `res/images`.

### `res`, `res/css`, AND `res/images` MUST BE PRESENT!

### Run `python3 src/main.py` from the `CollegeAppDB` directory. DO NOT RUN `main.py` FROM INSIDE THE `src` DIRECTORY!
