import setuptools


desc ="A PyTorch model zoo consisting of robust (adversarially trained) image classifiers and otherwise equivalent normal models for research purposes."


setuptools.setup(
    name="robustvsnormalzoo",
    version="1.0.1",
    author="Paul Gavrikov",
    author_email="paul.gavrikov@hs-offenburg.de",
    description=desc,
    long_description=desc,
    long_description_content_type="text/markdown",
    url="https://github.com/GeJulia/robust_confidences_evaluation",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "torch",
        "pandas",
        "robustbench @ git+https://github.com/RobustBench/robustbench.git@5e3b8bd56a9b6ee52554a63e8a9ea255289a8a12",
        "geotorch==0.3.0",
        "torchdiffeq==0.2.3",
        "timm==0.5.4",
    ],
    python_requires=">=3.6",
)