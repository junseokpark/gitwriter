from setuptools import setup, find_packages

setup(
    name='gitwriter',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'openai',
    ],
    entry_points={
        'console_scripts': [
            'gitwriter = gitwriter.cli:main',
        ],
    },
    author='Junseok Park',
    author_email='junseokpark.kr@gmail.com',
    description='A tool that generates git commit messages using LLM API or llama.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/junseokpark/gitwriter',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
