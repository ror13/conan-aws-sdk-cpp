from conans import ConanFile, CMake, tools


class AwsConan(ConanFile):
    name = "aws-sdk-cpp"
    version = "1.8.82"
    license = "Apache-2.0 License"
    url = "https://github.com/aws/aws-sdk-cpp"
    description = "event bus"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    build_requires = "cmake/3.15.7"

    def source(self):
        self.run("curl -sSL https://github.com/aws/aws-sdk-cpp/archive/" + self.version + ".tar.gz > source.tar.gz")
        self.run("tar xf source.tar.gz")
        # self.run("rm source.tar.gz")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CONAN_CMAKE_CXX_STANDARD"] = "17"
        cmake.definitions["ENABLE_UNITY_BUILD"] = "ON"
        cmake.definitions["ENABLE_TESTING"] = "OFF"
        cmake.definitions["AUTORUN_UNIT_TESTS"] = "OFF"
        cmake.definitions["BUILD_SHARED_LIBS"] = "ON"
        cmake.configure(source_folder="aws-sdk-cpp-" + self.version)
        self.run("make -j4")
        cmake.install()


def package(self):
    pass


def package_info(self):
    self.cpp_info.libs = ["aws-sdk-cpp"]
