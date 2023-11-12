from setuptools import setup, find_packages

setup(
    name='PypptRoadSign',
    packages=find_packages(),
    version='0.1.1',
    license='MIT',
    description=' QXWZ Power Point Road Sign Project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Haosong Liu',
    author_email='haosongliuofficial@gmail.com',
    url='https://github.com/liulhs/PypptRoadSign_Git',
    keywords=['Roadsign', 'PowerPoint', 'Genertor'],
    install_requires=[
        'python-pptx'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.6',
)
