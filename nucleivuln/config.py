#! /usr/bin/env python

"""This module is responsible for loading the configuration variables.
"""

import importlib.util
import os


def load_config(path):
    spec = importlib.util.spec_from_file_location("config", path)
    if spec:
        config = importlib.util.module_from_spec(spec)
        if spec.loader:
            spec.loader.exec_module(config)
    return config


conf = None
try:
    conf = load_config(
        os.environ.get("NUCLEIVULN_CONFIG", "./nucleivuln/conf_sample.py")
    )
except Exception as exc:
    raise Exception("No configuration file provided.") from exc
finally:
    if not conf:
        raise Exception("No configuration file provided.")


vulnerability_lookup_base_url = conf.vulnerability_lookup_base_url
vulnerability_auth_token = conf.vulnerability_auth_token

nuclei_git_repository = conf.nuclei_git_repository