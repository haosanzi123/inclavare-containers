%define centos_base_release 1
%define _debugsource_template %{nil}

%global PROJECT WAMR
%global LIB_DIR /usr/lib

Name: wamr-pal
Version: 0.5.0
Release: %{centos_base_release}%{?dist}
Summary: Platform Abstraction Layer of wamr enclave
Group: Development/Libraries
License: BSD License
URL: https://github.com/bytecodealliance/wasm-micro-runtime
Source0: https://github.com/bytecodealliance/wasm-micro-runtime/archive/WAMR-09-29-2020.tar.gz 

ExclusiveArch: x86_64

BuildRequires: automake
#AutoReqProv: no

%description
wamr-pal is xxx

%prep
%setup -q -n wasm-micro-runtime

%build
pushd product-mini/platforms/linux-sgx/
mkdir build && cd build && cmake .. && make
cd ../enclave-sample/ && make
/opt/intel/sgxsdk/bin/x64/sgx_sign sign -key Enclave/Enclave_private.pem -enclave enclave.so -out enclave.signed.so -config Enclave/Enclave.config.xml
g++ -shared -fPIC -o libwamr-pal.so App/*.o libvmlib_untrusted.a -L/opt/intel/sgxsdk/lib64 -lsgx_urts -lpthread -lssl -lcrypto
popd

%install
install -d -p %{buildroot}%{LIB_DIR}
install -p -m 755 product-mini/platforms/linux-sgx/enclave-sample/libwamr-pal.so %{buildroot}%{LIB_DIR}

%files
%{LIB_DIR}/libwamr-pal.so

%changelog
* Tue Jun 16 2020 Shirong Hao <shirong@linux.alibaba.com> - 0.5.0-1
- package init
