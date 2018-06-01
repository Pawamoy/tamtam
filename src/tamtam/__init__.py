import itertools
import pytoml
from copy import deepcopy


def load_configuration(file_path):
    with open(file_path) as stream:
        configuration = pytoml.load(stream)
    if "tool" in configuration:
        return configuration["tool"].get("tamtam", {})
    return configuration


def expand_job(job):
    return list(
        itertools.product(
            [("python", python) for python in job["pythons"]],
            *[
                [
                    (dependency, version_specifier)
                    for version_specifier in version_specifiers
                ]
                for dependency, version_specifiers in job["dependencies"].items()
            ]
        )
    )
