# https://learn.microsoft.com/en-us/vcpkg/users/triplets
set(VCPKG_TARGET_ARCHITECTURE arm64)
set(VCPKG_CRT_LINKAGE dynamic)
set(VCPKG_LIBRARY_LINKAGE dynamic)

# provide build options for vcpkg installed packages
if(PORT MATCHES "onnx")
    list(APPEND VCPKG_CMAKE_CONFIGURE_OPTIONS
        "-DONNX_DISABLE_STATIC_REGISTRATION=ON"
    )
endif()