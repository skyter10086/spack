from spack import *


class Garply(Package):
    """Toy package for testing dependencies"""

    homepage = "https://www.example.com"
    url      = "https://github.com/gartung/garply/releases/download/v3.0.0/garply-3.0.0.tar.gz"

    version(
        '3.0.0', sha256='ac289d2f5baac6ae85308d66d7e8e5a27d6c716ec13f2d4514d634a3ef5799c8')

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)
