import os
from abc import ABC
from django.utils._os import safe_join
from django.utils.deconstruct import deconstructible

from storages.backends.dropbox import DropBoxStorage


class SuspiciousFileOperation(Exception):
    pass


@deconstructible
class DropBoxStorageFix(DropBoxStorage, ABC):
    def _full_path(self, name):
        if name == '/':
            name = ''

        # If the machine is windows do not append the drive letter to file path
        if os.name == 'nt':
            return safe_join_fix(self.root_path, name)
        else:
            return safe_join(self.root_path, name).replace('\\', '/')


def safe_join_fix(root_path, name):
    final_path = os.path.join(root_path, name).replace('\\', '/')

    # Separator on linux system
    sep = '//'
    base_path = root_path

    if (not os.path.normcase(final_path).startswith(os.path.normcase(base_path + sep)) and
            os.path.normcase(final_path) != os.path.normcase(base_path) and
            os.path.dirname(os.path.normcase(base_path)) != os.path.normcase(base_path)):
        raise SuspiciousFileOperation(
            'The joined path ({}) is located outside of the base path '
            'component ({})'.format(final_path, base_path))

    return final_path
