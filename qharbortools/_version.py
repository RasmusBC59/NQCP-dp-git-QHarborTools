def _get_version() -> str:
    from pathlib import Path

    import versioningit

    import qharbortools

    qharbortools_path = Path(qharbortools.__file__).parent
    return versioningit.get_version(project_dir=qharbortools_path.parent)


__version__ = _get_version()
