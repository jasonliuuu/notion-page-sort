# 📋 Notion Page Sort

Sort Notion's sub-page by title (or part of title's content). Very simple, bare-bone script, with only 40+ lines of code but a decent terminal UI.

![](https://i.loli.net/2019/12/24/LhSdiHU4EOAPBlV.gif)

## Config

Change configurations in line 6 to line 8 in `main.py`:

```python
# Regex match pattern
pattern = r"#(\d+)\ "

# Notion's Login Cookie
token = "{GET-TOKEN-FROM-LOGINED-NOTION's-COOKIE}"

# Notion's root page to sort
url = "{NOTION-PAGE-URL}"
```

In my case, the regex shown above is matching the pattern where a number comes after `#`, like `#20 ` in title `#20 macOS Menubar`. The script takes the `20` as key to sort through the titles.

The token used to log into Notion can be acquired from the developer's console in a already logged-in Notion web page.

## Build and run

1. Install dependencies

```bash
pipenv install
```

2. Run `main.py`

```bash
# Enter virtual environment
pipenv shell

# Run script
python main.py
```

## FAQ

**Q: Why is the sorting process so slow?**

**Because Notion's web API is slow to access.** I am using Notion's unofficial Python API wrapper to implement this script, and I am sorting the subpages with **Bubble sort**. 

**Bubble sort** is a sorting algorithm which is highly dependent on "swapping" components. In this case, each "swap" is sent out via HTTP requests, and considering how long it takes for us to access Notion, one can understand why exactly is the sorting process so slow.

If (or when) Notion releases their official API, I will try to implement this script using a single web request, so that the sorting can be done offline.

---

**📋 Notion Page Sort** ©Spencer Woo. Released under the [MIT License](./LICENSE).

Authored and maintained by Spencer Woo.

[@Portfolio](https://spencerwoo.com) · [@GitHub](https://github.com/spencerwooo) · [@BIT](http://www.bit.edu.cn/)
