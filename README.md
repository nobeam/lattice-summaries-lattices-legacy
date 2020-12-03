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

## Naming Scheme

TODO: @michael

## Open Questions

### Problem

To leverage multiple simulation tools we have to generate lattice files in different formats. These lattice file formats cam have custom elements and attributes which makes a 1:1 mapping between them impossible.

### Solution

Agree on a restricted form of lattice file format, which only uses a set of basic elements and parameters. This should make a 1:1 mapping possible. 

### Specification of restricted lattice file format

TODO: @michael

##### Dipole

 | Tables        | Are         |
 | ------------- | ----------- |
 | col 3 is      | right-align |
 | col 2 is      | centered    |
 | zebra stripes | are neat    |
