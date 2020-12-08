# B3 Prototype Lattices

The lattices are listed in the `info.toml` file. If you add an lattice to this repo please add an entry to this file:

```toml
[[lattices]]
title = "Human readable name of the lattice"
file = "file_friendly_name_of_the_lattice"
author = "Max Mustermann"
description = """
A description of the lattice.
"""
```

## Generated Lattices

The generated lattices are stored in the generated folder. Generate the lattices in the different formats by running:

```
doit
```

