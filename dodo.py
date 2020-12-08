DOIT_CONFIG = {"default_tasks": ["convert"]}

# map source file to dependencies
SOURCE = {
    "main": ["defs.h"],
    "kbd": ["defs.h", "command.h"],
    "command": ["defs.h", "command.h"],
}

from pathlib import Path
import tomlkit
import latticejson

base_dir = Path(__file__).parent
lattice_dir = Path("lattices")
info = tomlkit.parse((base_dir / "info.toml").read_text())


def task_convert():
    def convert_lattices(source, targets):
        lattice_file = latticejson.load(source)
        for target in targets:
            latticejson.save(lattice_file, target)

    for source in lattice_dir.rglob("*"):
        if source.is_dir():
            continue

        targets = [
            "_generated" / source.with_suffix(".lte").relative_to(lattice_dir),
            "_generated" / source.with_suffix(".madx").relative_to(lattice_dir),
            "_generated" / source.with_suffix(".json").relative_to(lattice_dir),
        ]
        targets[0].parent.mkdir(parents=True, exist_ok=True)

        yield {
            "name": source,
            "actions": [(convert_lattices, [source, targets])],
            "targets": targets,
            "file_dep": [source],
            "clean": True,
        }
