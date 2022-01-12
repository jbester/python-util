import contextlib
import os
import sys
import traceback
from pathlib import Path
import shutil
from typing import Union, AnyStr, List


def die(*msg, file=sys.stderr, error_code=1):
    """Perl-like Die

    prints message to stderr with line number and filename if possible
    then exits with error code.
    :param file: output file (defualt stderr)
    :param error_code: error code
    """
    suffix = ''
    frame = traceback.extract_stack(limit=1)
    if frame:
        (filename, lineno, _, _) = frame[0]
        suffix = f"at {filename} {lineno}"
    print(*msg, suffix, file=file)
    sys.exit(error_code)


def warn(*msg, file=sys.stderr):
    """Perl-like warn

    prints message to stderr with line number and filename if possible
    """
    suffix = ''
    frame = traceback.extract_stack(limit=1)
    if frame:
        (filename, lineno, _, _) = frame[0]
        suffix = f"at {filename} {lineno}"
    print(*msg, suffix, file=file)



def fatal_assert(condition, *msg):
    """Assert using die instead of an exception"""
    if not condition:
        die(*msg)


@contextlib.contextmanager
def in_directory(path: os.PathLike):
    """With support for something like a pushd/popd pair.  Change to a directory for a block and then change back.
Raises NotADirectoryError if path does not exist

    :param path: path to use within the block
    """
    current_directory = os.path.abspath(os.getcwd())
    if not os.path.exists(path) or not os.path.isdir(path):
        raise NotADirectoryError(f"{path} is not a directory")
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(current_directory)


@contextlib.contextmanager
def directory_removed_after(path: os.PathLike, ignore_errors: bool = False):
    """With support that removes the specified path after the block

    :param path: directory path
    :param ignore_errors: flag to ignore errors on removal
    """
    try:
        yield
    finally:
        if os.path.exists(path):
            shutil.rmtree(path, ignore_errors=ignore_errors)


@contextlib.contextmanager
def file_removed_after(path: os.PathLike):
    """With support that removes the specified path after the block

    :param path: directory path
    """
    try:
        yield
    finally:
        if os.path.exists(path):
            os.unlink(path)


@contextlib.contextmanager
def files_removed_after(paths: List[os.PathLike]):
    """With support that removes the specified path after the block

    :param paths: list of directory paths
    """
    try:
        yield
    finally:
        for path in paths:
            if os.path.exists(path):
                os.unlink(path)


def chomp(s: AnyStr) -> AnyStr:
    """Perl-Like Chomp; strips line endings and returns just the string

    >>> chomp( "test\r\n" )
    'test'

    @param s: string to chomp
    @return: string without ending newline
    """
    if s.endswith('\r\n'):
        return s[:-2]
    if s[-1] == '\r' or s[-1] == '\n':
        return s[:-1]
    return s