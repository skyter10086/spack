# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Quux(Package):
    """Toy package for testing dependencies"""

    homepage = "https://www.example.com"
    url      = "https://github.com/gartung/quux/releases/download/v3.0.0/quux-3.0.0.tar.gz"

    version('3.0.0', sha256='92910c1045fb2722fedbab6d679d3bcb52a1f6d5338ee61514f5e587c7eb5e57')

    depends_on('garply')

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)
