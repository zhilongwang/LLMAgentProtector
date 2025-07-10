from setuptools import setup, find_packages

setup(
    name="llmagentprotector",
    version="0.1.0",
    description="Polymorphic Prompt Assembler to protect LLM agents from prompt injection and prompt leak",
    author="Zhilong Wang",
    packages=find_packages(),  # Automatically finds 'llmagentprotector'
    include_package_data=True,
    install_requires=[
        # list your dependencies here
    ],
)
