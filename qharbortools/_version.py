def _get_version() -> str:
    # we use lazy imports to avoid importing modules that are not
    # used when the use of this function is patched out at build time
    from pathlib import Path  # noqa: PLC0415

    import versioningit  # noqa: PLC0415

    import qharbortools  # noqa: PLC0415

    qharbortools_path = Path(qharbortools.__file__).parent
    return versioningit.get_version(project_dir=qharbortools_path.parent)


__version__ = _get_version()
