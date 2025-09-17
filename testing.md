
# Testing Jupyter Book features

- [ghost forest](wiki:Ghost_forest) should resolve to
  https://en.wikipedia.org/wiki/Ghost_forest
- [This paper DOI 10.1029/91JB02346](doi:10.1029/91JB02346)  % not working
- This works: [DOI 10.1029/91JB02346](https://doi.org/10.1029/91JB02346)
- ~~testing stirkethrough~~
- Testing replacement: {{ WEBSITE }} is a url?
- Testing [website]({{ WEBSITE }})
- Testing <a href="{{ WEBSITE }}">website in raw html</a>
- Testing <a href="{{ CLAWDOCS }}/fgmax.html">website in raw html</a>

## Latex

$\int e^x \, dx$ or {math}`\int e^x \, dx`.  Display:

$$
\int e^x \, dx
$$


