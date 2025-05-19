def _get_version() -> str:
    from pathlib import Path

    import versioningit

    import qhabortools

    qhabortools_path = Path(qhabortools.__file__).parent
    return versioningit.get_version(project_dir=qhabortools_path.parent)


__version__ = _get_version()
