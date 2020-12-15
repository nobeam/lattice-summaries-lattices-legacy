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

The generated lattices are stored in the generated folder. Generate the lattices in the different formats by running (requires Python >3.8 and poetry):

```
poetry install
poetry run doit
```
## Naming Scheme

Information like the energy, periodicity, number of bends per cell and other details (e.g. longitudinal gradients bend) which characterize a lattice will be included in the `info.toml` file, so it is not necessary that they are present in the filename. As we want to distribute the lattices over the web we have restrict us to the [unreserved URL characters `A-Za-z0-9.~-_`](https://en.wikipedia.org/wiki/Percent-encoding#Percent-encoding_in_a_URI).

### Schema

 The schema of a lattice name is given by:

<pre><code><b>&ltnamespace&gt</b>/<b>&ltmachine&gt</b>_<b>&ltfamiliy&gt</b>_v_<b>&ltversion&gt</b></pre></code>

A name is built up out of different `<identifiers>` which are separated by a `_`. Allowed characters within an `<identifier>` are therefore `A-Za-z0-9.~-`. 

> :warning: Notice that `_` is not allowed!

### Explanation of different `<identifiers>`

- **`<namespace>`** This is necessary to make sure different people don't come up with the same name. All contributors of lattice-summaries repo will have their own namespace and have to make sure that all **`<family>`** names are unique within their namespace. Notice that the **`<namespace>`** must not correspond to the author(s) of a lattice. The actual authors of a lattice are listed in `info.toml` file and also as comment at the top of automatically generated lattice files. I decided it this way, because we may want to include lattices from other facilities. If Paul would upload the SLS2 lattice, the name would be something like `sls2_goslawski_design_v_std-user` even though Paul is not the author of the SLS2 lattice. The same would be true for a LOCO-measured BESSY II lattice file. In case a lattice **`<family>`** is maintained by multiple people an acronym like `gaa` for `Goslawski`, `Abo-Bakr` and `Andreas` would also be fine.
- **`<machine>`** Name of the machine (e.g. `b2`,`b3`, `mls`, `mls2`)
- **`<familiy>`** The goal of a **`<family>`** identifier is to make different versions of a lattice easier to compare on the lattice-summaries website. The name of the lattice *family* must be unique within *YOUR* **`<namespace>`**. Lattices within a family should belong logically together. For example Paul created several MLS2 lattices based on a scaled down version of BESSY II. In this case the family name should be something like `scaled-bessy2`. As during the B3 development presumably many lattices will be called `5ba-20p`, you could also choose a more memorable name like `jupiter`, `bravo` or `falcon`, which will make it easy to refer to a specific lattice during discussions.
- **`<version>`** The version name uniquely identifies a lattice within a **`<family>`**. It can be a simple number like `1` or a more descriptive name like `std-user`, `low-alpha` or `reference`. To please Paul it is also possible to use something like `1200mev-8p-2ba-new-wp-x909125-y909125`.

### Recommendations

Even there are no technical limitation, I would recommend to stick with lowercase characters and avoid using the `~` and `.` characters. This will make it easier on the command line and also provides some consistency. So I would only use the `a-z0-9-`.

### Examples

* `b3_kuske_5ba-20p_v_reference`
* `b3_kuske_5ba-20p_v_long-bend-tgrb`
* `b3_abo-bakr_jupiter_v_2`
* `mls3_goslawski_scaled-bessy2_v_100m-1200mev-8p-2ba-new-wp-x909125-y909125`
* `b2_mertens_loco_v_std-user-2020-08-10`
* `b2_andreas_q5t2-off_v_4`
