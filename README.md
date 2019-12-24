# 📋 Notion Page Sort

Sort notion subpage by title (or part of title's content). Very simple, bare-bone script, with only 40+ lines of code but a decent terminal UI.

![](https://i.loli.net/2019/12/24/LhSdiHU4EOAPBlV.gif)

## Config

Change configurations in line 6 to line 8 in `main.py`:

```python
# Regex match pattern
pattern = r"#(\d+)\ "

# Notion's Login Cookie
token = "{GET-TOKEN-FROM-LOGINED-NOTION's-COOKIE}"

# Notion's page to sort
url = "{NOTION-PAGE-URL}"
```

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

Q: Why so slow?

A:

---

**📋 Notion Page Sort** ©Spencer Woo. Released under the [MIT License](./LICENSE).

Authored and maintained by Spencer Woo.

[@Portfolio](https://spencerwoo.com) · [@GitHub](https://github.com/spencerwooo) · [@BIT](http://www.bit.edu.cn/)
