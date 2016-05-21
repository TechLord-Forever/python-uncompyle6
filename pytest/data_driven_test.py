# std
import os
import fnmatch
import py_compile
# pytest
import pytest
# uncompyle
from uncompyle6.main import main


def get_srcdir():
    filename = os.path.normcase(os.path.dirname(__file__))
    return os.path.realpath(filename)


test_dir = os.path.join(get_srcdir(), '..', 'test')


def remove_dis_files(sub_test):

    remove_passed, remove_failed = True, False

    dis_path = sub_test + '_dis'
    if remove_passed and (os.path.exists(dis_path) or remove_failed):
        os.unlink(dis_path)


def data_driven_test(test_dir_pattern, *file_patterns):
    """
    Data driven test decorator factory. The decorator will run the data driven
    test, parameterizing the inputs to the funtions based on the search
    parameters.

    :param test_dir_pattern: fnmatch pattern to use to find the sub directory
                             containingtest files.

    :param *file_patterns: fnmatch patterns to use to find files which should
                           be run through uncompyle for verification.

    :return: Data driven test decorator.
    """

    tests = sorted(

        (tests_root, filename)

        for root, dirs, files in os.walk(test_dir)
        for tests_root in [root.replace(test_dir + '/', '')]
        for filename in files
        for file_pattern in file_patterns

        if fnmatch.fnmatch(filename, file_pattern)
        if fnmatch.fnmatch(tests_root, test_dir_pattern)
        if filename != '__init__.py'
    )

    def decorator(fn):
        """
        Decorate a function to produce a data driven test. Since the actual
        test function is also performed here, the only thing of importance
        from the decorated function is the name, which will be used to generate
        the test name for py.test

        :param fn: The function the decorate.

        :return: The decorated function.
        """

        @pytest.mark.parametrize('test, sub_test', tests)
        def run_test(test, sub_test):
            """
            Perform the data driven test, run the file specified by sub test
            through uncompyle and verify the output.

            :param test: The test directory.
            :param sub_test: The test file to uncompyle.
            """

            fullpath = os.path.join(test_dir, test)
            py_compile.compile(os.path.join(fullpath, sub_test))

            result = main(fullpath, '.', [sub_test], [], do_verify=True)
            _, _, failed_files, failed_verify = result

            failed_fmt = 'failed to {action} {test}-{sub_test}'
            if failed_files != 0:
                action = 'uncompyle'
                msg = failed_fmt.format(**locals())
                raise Exception(msg)
            elif failed_verify != 0:
                action = 'verify'
                msg = failed_fmt.format(**locals())
                raise Exception(msg)

            remove_dis_files(sub_test)

        return run_test

    return decorator
