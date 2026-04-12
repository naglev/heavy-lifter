def do_the_heavy_lifting(file_path, heavy_lifter_version):
    content = _read_file(file_path)


def _read_file(file_path) -> str:
    with open(file_path, encoding='utf-8') as f:
        return f.read()

