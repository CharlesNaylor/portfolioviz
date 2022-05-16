# PortfolioViz

Project primarily to teach myself where HoloViz, bokeh, DataShader, etc. have gotten to in the last few years.

Motivation will be to check a deep value portfolio from the start of the pandemic.

## Graphics to make

  - time series performance (vs benchmarks, by GICS, etc.)
  - sankey on composition (sectors, etc.)
  - clustering / network graphs

## Other goals

  - architecture to support event-based updating (I'm not putting this in the cloud, but want to receive a json update)
  - explore interactive graphs / JS output
  - automated reporting
  - refinitiv API

## Log

2022-05-16 - The first problem is that holoviz wants you to install a custom conda-based environment in order to use the packages. I have a "no conda" rule. Trying to install underlying packages only.
