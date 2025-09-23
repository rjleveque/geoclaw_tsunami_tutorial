---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Executable cells in markdown

This file adapted from
[this JupyterBook example](https://jupyterbook.org/en/stable/file-types/myst-notebooks.html#structure-of-myst-notebooks).

```{code-cell} ipython3
:tags: [mytag]

print("A python cell")
```

Try a simpler version:

```{code-cell}
print("A python cell")
```
## Try glue

See https://jupyterbook.org/en/stable/content/executable/output-insert.html

```{code-cell}
from myst_nb import glue
my_variable = "here is some text!"
glue("cool_text", my_variable)
```

Now we can try to use this: {glue:}`cool_text`

### Do it again, hiding the cell input and output:

```{code-cell}
:tags: [remove-cell]
from myst_nb import glue
my_text = 'Here is the text printed in a hidden cell!'
glue("my_text", my_text)
```

Now we can try to use this: {glue:}`my_text`

### Hide input with a button to show it

See https://jupyterbook.org/en/stable/interactive/hiding.html

```{code-cell}
:tags: [hide-input, remove-output]
bignumber = 2**32
glue('bignumber',bignumber)
```

What power of 2 is this big number: {glue:}`bignumber`?

```{code-cell}
:tags: [hide-input]
print(f'Hint, the 8th root of this number is {bignumber**(1/8):.0f}')
```
