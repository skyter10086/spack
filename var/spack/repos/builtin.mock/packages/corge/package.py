# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Corge(Package):
    """A toy package to test dependencies"""

    homepage = "https://www.example.com"
    url      = "https://github.com/gartung/corge/releases/download/v3.0.0/corge-3.0.0.tar.gz"

    version(
        '3.0.0', sha256='fdd4b03b38dcc6650366a6469898ba89714777647687ae28f0ae55480ae5b393',
        url="https://github.com/gartung/corge/releases/download/v3.0.0/corge-3.0.0.tar.gz")

    depends_on('quux')

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)
