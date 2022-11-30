import sys
from setuptools import setup, find_packages

setup(name="cubao_meshcat",
    version="0.3.3",
    description="WebGL-based visualizer for 3D geometries and scenes",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cubao/meshcat-python",
    author="tzx",
    author_email="dvorak4tzx@gmail.com",
    license="MIT",
    packages=find_packages("src"),
    package_dir={"": "src"},
    test_suite="meshcat",
    entry_points={
        "console_scripts": [
            "cubao-meshcat-server=cubao_meshcat.servers.zmqserver:main"
        ]
    },
    install_requires=[
      "ipython >= 5",
      "u-msgpack-python >= 2.4.1",
      "numpy >= 1.14.0",
      "tornado >= 4.0.0",
      "pyzmq >= 17.0.0",
      "pyngrok >= 4.1.6",
      "pillow >= 7.0.0"
    ],
    zip_safe=False,
    include_package_data=True
)
