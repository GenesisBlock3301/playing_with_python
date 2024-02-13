from setuptools import setup

setup(
    name='cli-script',
    version='0.1.0',
    py_modules=['click_cli.py'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'click_cli = click_cli:cli',
        ],
    },
)
