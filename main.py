"""Write the entry image to the make.fun output directory.

The entry is a single 1024x1024 PNG, ``entry.png``, stored next to this
script. Running this program copies that file, byte for byte, to
``$MAKEFUN_OUTPUT_DIR/entry.png`` (or to ``output/entry.png`` under the
current directory when the variable is unset).

Before copying, the first eight bytes of the source are compared against
the PNG file signature; a file that is not a PNG is refused with an error
on stderr and a non-zero exit code. The copy goes through a temporary
file in the destination directory, which is then renamed into place, so
a failed run never leaves a half-written ``entry.png`` behind and two
successful runs produce identical bytes.
"""

import os
import sys

ENTRY_FILE = "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message):
    print("error: " + message, file=sys.stderr)
    return 1


def run():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, ENTRY_FILE)

    try:
        with open(source, "rb") as handle:
            image = handle.read()
    except OSError as exc:
        return fail("cannot read {}: {}".format(source, exc))

    if image[:8] != PNG_MAGIC:
        return fail("{} is not a PNG file".format(source))

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = os.path.join(os.getcwd(), "output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        return fail("cannot create {}: {}".format(out_dir, exc))

    target = os.path.join(out_dir, ENTRY_FILE)
    staging = target + ".tmp"
    try:
        with open(staging, "wb") as handle:
            handle.write(image)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(staging, target)
    except OSError as exc:
        try:
            os.unlink(staging)
        except OSError:
            pass
        return fail("cannot write {}: {}".format(target, exc))

    return 0


if __name__ == "__main__":
    sys.exit(run())
