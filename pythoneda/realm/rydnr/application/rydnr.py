"""
pythoneda/realm/rydnr/application/rydnr.py

This file can be used to run Rydnr's PythonEDA realm.

Copyright (C) 2023-today rydnr's pythoneda-realm-rydnr/application

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import asyncio
from pythoneda.application import PythonEDA

class Rydnr(PythonEDA):
    """
    Runs the Rydnr's PythonEDA realm.

    Class name: Rydnr

    Responsibilities:
        - Runs the Rydnr's PythonEDA realm.

    Collaborators:
        - Command-line handlers from pythoneda-realm-rydnr/infrastructure
    """
    def __init__(self, file=__file__):
        """
        Creates a new Rydnr instance.
        """
        super().__init__(__file__)

if __name__ == "__main__":

    asyncio.run(Rydnr.main())
