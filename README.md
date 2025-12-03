# Conceptual alternatives. Competition in language and beyond

## What is it?

This repository is a fork of [Brian Buccola, Manuel Križ and Emmanuel Chemla's experiment](https://github.com/brianbuccola/conceptual-alternatives-experiment) about conceptual alternatives. The [original article](https://semanticsarchive.net/Archive/WE2NzVlY/buccola-kriz-chemla-conceptual-alternatives.html) analyzes the pairs `all vs. some but not all`, `no vs. some but not all` , `at least vs. at most`.

We adopt the same experimental approach in the new study for a research seminar "Sematics-Syntax Interface" (HSE University, 2025). With our experiment we analyze the primitiveness of `and, or, xor`. The experiment uses the [Ibex](http://spellout.net/ibexfarm/) platform for running psycholinguistic
experiments. The questionnaire is avalaible [here](https://farm.pcibex.net/p/MwltjO/).

## Project Structure

This repository contains experimental materials.

```
├── README.md
├── analysis
├── chunk_includes
├── css_includes
├── data_includes
├── generating_items
├── js_includes
└── results
```

The questionnaire and other html's are available in `chunk_includes/`. They were created by the script from `generating_items` directory. The results of the experiment are located in `results/` folder and their analysis on Python is available in `analysis/`. 

The other directories are adopted from the [Ibex repository](https://github.com/addrummond/ibex). See it for further instructions, documentation and licence.
