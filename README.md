# B3 Prototype Lattices

The orignal lattice files are stored in the `originals` folder.  The automattically converted lattices are stored in the `generated` folder and can be pushed to the `generated` branch.

## Convert Lattices

The lattices are converted using the [LatticeJSON cli](https://github.com/nobeam/latticejson). To convert all lattice files into the different formats run: (requires Python 3.8+ and [Poetry](https://python-poetry.org/))

```
poetry install
poetry run doit
```

## Add a new Lattice

The `originals` folder has several subfolders which are used as namespaces to prevent naming collisions. To add a new lattice:

1. Clone this repository
2. Create a new branch (e.g. `goslawski/add-mls2-lattice`)
3. Check if your lattice file meets all the requirements. [(see below)](#lattice-file-format) 
4. Add your lattice file to the `originals` folder.
5. Add an entry in the `info.toml` file.
6. Push the branch and create a pull request.
7. The pull request should be squash merged. The commit message should be "add goslawski/mls2_scaled-from-bessy2_v_1" for a newly added lattice or "update goslawski/mls2_scaled-from-bessy2_v_1" in case a lattice is updated.


The lattices are listed in the `info.toml` file. If you add an lattice to this repo please add an entry to this file:

```toml
[[lattices]]
namespace = "goslawski"
name = "mls2_scaled-from-bessy2_v_1"
machine = "mls2"
title = "mls2 based on bessy2"
authors = ["Goslawski", "Max Mustermann"]
energy = 1200
simulations = ["apace", "elegant", "madx"]
labels = []
description = """
A possible design lattice for the MLS2 based on a scaled down version of BESSY 2
"""
```

TODO @michael: add list of useful labels 


## Lattice file format
### Problem

To leverage multiple simulation tools we have to generate lattice files in different formats. These lattice file formats can have custom elements and attributes which makes a 1:1 mapping between them impossible.

### Solution

We agree on a restricted set of generic elements, which should be available in every simulation software and define a 1:1 mapping between these lattice file formats.

### Allowed lattice file formats


TODO @michael: 
    - add tables of allowed elements and attributes
    - i have added an examplary table for the Dipole element. we need a separate table for each element!

| Generic Element | MAD-X      | elegant |
| --------------- | ---------- | ------- |
| Drift           | DRIFT      | DRIF    |
| Dipole          | SBEND      | CSBEND  |
| Quadrupole      | QUADRUPOLE | KQUAD   |
| Sextupole       | SEXTUPOLE  | KSEXT   |
| Octupole        | Octupole   | KOCT    |

#### Dipole

| attribute | description                   |
| --------- | ----------------------------- |
| length    | length                        |
| angle     | deflection angle              |
| k1        | geometric quadrupole strength |
| e1        | entrance angle                |
| e2        | exit angle                    |

## Naming Scheme

Information like the energy, periodicity, number of bends per cell and other details (e.g. longitudinal gradients bend) which characterize a lattice will be included in the `info.toml` file, so it is not necessary that they are present in the filename. As we want to distribute the lattices over the web we have restrict us to the [unreserved URL characters `A-Za-z0-9.~-_`](https://en.wikipedia.org/wiki/Percent-encoding#Percent-encoding_in_a_URI).

### Schema

 The schema of a lattice name is given by:

<pre><code><b>&ltnamespace&gt</b>/<b>&ltmachine&gt</b>_<b>&ltfamiliy&gt</b>_v_<b>&ltversion&gt</b></pre></code>

A name is built up out of different `<identifiers>` which are separated by a `_`. Allowed characters within an `<identifier>` are therefore `A-Za-z0-9.~-`. 

> :warning: Notice that `_` is not allowed!

### Explanation of different `<identifiers>`

- **`<namespace>`** This is necessary to make sure different people don't come up with the same name. All contributors of lattice-summaries repo will have their own namespace and have to make sure that all **`<family>`** names are unique within their namespace. Notice that the **`<namespace>`** must not correspond to the author(s) of a lattice. The actual authors of a lattice are listed in `info.toml` file and also as comment at the top of automatically generated lattice files. I decided it this way, because we may want to include lattices from other facilities. If Paul would upload the SLS2 lattice, the name would be something like `goslawski/sls2_design_v_std-user` even though Paul is not the author of the SLS2 lattice. The same would be true for a LOCO-measured BESSY II lattice file. In case a lattice **`<family>`** is maintained by multiple people an acronym like `gaa` for `Goslawski`, `Abo-Bakr` and `Andreas` would also be fine.
- **`<machine>`** Name of the machine (e.g. `bessy2`, `bessy3`, `mls`, `mls2`)
- **`<familiy>`** The goal of a **`<family>`** identifier is to make different versions of a lattice easier to compare on the lattice-summaries website. The name of the lattice *family* must be unique within *YOUR* **`<namespace>`**. Lattices within a family should belong logically together. For example Paul created several MLS2 lattices based on a scaled down version of BESSY II. In this case the family name should be something like `scaled-bessy2`. As during the B3 development presumably many lattices will be called `5ba-20p`, you could also choose a more memorable name like `jupiter`, `bravo` or `falcon`, which will make it easy to refer to a specific lattice during discussions.
- **`<version>`** The version name uniquely identifies a lattice within a **`<family>`**. It can be a simple number like `1` or `2` or a more descriptive name like `std-user`, `low-alpha` or `reference`. To please Paul it is also possible to use something like `1200mev-8p-2ba-new-wp-x909125-y909125`.

### Recommendations

Even there are no technical limitation, I would recommend to stick with lowercase characters and avoid using the `~` and `.` characters. This will make it easier on the command line and also provides some consistency. There recommended character to use are therefore `a-z0-9-`.

### Examples

* `kuske/bessy3_5ba-20p_v_reference`
* `kuske/bessy3_5ba-20p_v_long-bend-tgrb`
* `abo-bakr/bessy3_jupiter_v_2`
* `goslawski/mls2_scaled-bessy2_v_100m-1200mev-8p-2ba-new-wp-x909125-y909125`
* `mertens/bessy2_loco_v_std-user-2020-08-10`
* `andreas/bessy2_q5t2-off_v_4`
