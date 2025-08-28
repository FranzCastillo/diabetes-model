from setuptools import setup, find_packages

setup(
    name="diabetes-model",
    version="0.0.9",
    description="A pipeline for diabetes prediction using logistic regression.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "scikit-learn",
        "pandas",
        "joblib"
    ],
    python_requires=">=3.7",
)