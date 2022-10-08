from setuptools import setup, find_packages

VERSION = '0.5.2'

# this is what usually goes on requirements.txt
install_requires = [
    # more flexible torch version for easier installation on Colab
    'torch >= 1.10.1, < 2.0.0',
    'torch-scatter==2.0.9',
    'tqdm',
    'fairseq >= 0.10.2, < 1.13.0',
    'packaging',
    'requests',
    # for data (ELMO embeddings)
    'h5py',
    'python-dateutil',
    # for scoring
    'penman',
    # needs tools to be importable > 1.0.4
    'smatch',
    # skipping debugging deps for easier install
    # 'ipdb',
    # 'line_profiler',
    # 'pyinstrument'
]

setup(
    name='transition_amr_parser',
    version=VERSION,
    description="Trasition-based AMR parser",
    py_modules=['transition_amr_parser'],
    entry_points={
        'console_scripts': [
            'amr-parse = transition_amr_parser.parse:main',
            'amr-machine = transition_amr_parser.amr_machine:main',
        ]
    },
    packages=find_packages(),
    install_requires=install_requires,
)
