import time
import re
from yaspin import yaspin
from notion.client import NotionClient

pattern = r"#(\d+)\ "
token = "{GET-TOKEN-FROM-LOGINED-NOTION'S-COOKIE}"
url = "{NOTION-PAGE-URL}"


def getBlockIndex(block):
    try:
        index = re.findall(pattern, block)[0]
        return index
    except IndexError as e:
        print('Index Error occurred')


def getBlockIndex(block):
  index = re.findall(pattern, block)[0]
  return index


if __name__ == "__main__":
  with yaspin(text="Fetching Notion page...", color="blue") as spinner:
    page = initNotionPage()
    if page:
      spinner.ok("✔")
    else:
      spinner.fail("✗")

  with yaspin(text="Analyzing blocks...", color="yellow") as spinner:
    blockCount = 0
    for child in page.children:
      spinner.write("> Block " + getBlockIndex(child.title) + " analyzed")
      blockCount += 1

  with yaspin(text="Sorting blocks in ascending order...", color="magenta") as spinner:
    for i in range(blockCount):
      for j in range(0, blockCount - i - 1):
        preIndex = int(getBlockIndex(page.children[j].title))
        postIndex = int(getBlockIndex(page.children[j + 1].title))
        if (preIndex >= postIndex):
          page.children[j].move_to(page.children[j + 1], "after")

    spinner.ok("✔")

  print("Done sorting.")
