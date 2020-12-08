from pathlib import Path
from operator import itemgetter
import tomlkit
import latticejson

base_dir = Path(__file__).parent
lattice_dir = Path("originals")
generated_dir = base_dir / "generated"
info = tomlkit.parse((base_dir / "info.toml").read_text())


def task_convert():
    def convert_lattices(source, targets):
        lattice_file = latticejson.load(source)
        for target in targets:
            latticejson.save(lattice_file, target)

    for lattice in info["lattices"]:
        namespace, name = itemgetter("namespace", "name")(lattice)
        source_base = lattice_dir / namespace / name
        source = next(source_base.parent.glob(str(source_base.stem) + ".*"))
        target_base = generated_dir / namespace / name
        targets = [
            target_base.with_suffix(".json"),
            target_base.with_suffix(".lte"),
            target_base.with_suffix(".madx"),
        ]
        targets[0].parent.mkdir(parents=True, exist_ok=True)

        yield {
            "name": source,
            "actions": [(convert_lattices, [source, targets])],
            "targets": targets,
            "file_dep": [source],
            "clean": True,
        }
