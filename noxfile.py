# autoflake: skip_file
import nox
python_versions = ['3.10']
import sys
from pathlib import Path

src_path = Path('src').resolve()
sys.path.append(str(src_path))


@nox.session(python=python_versions, tags=['lint-fix', 'lint'], reuse_venv=True)
@nox.parametrize("sources", ["src", "app.py","config_files"])
def lint_files(session,sources):
    session.run('autoflake', '--in-place', '--remove-all-unused-imports', '--expand-star-imports', '--recursive', sources,
                external=True)
    session.run('isort', sources, external=True)
    session.run('black', sources, external=True)