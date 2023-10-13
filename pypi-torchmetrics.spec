#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-torchmetrics
Version  : 1.2.0
Release  : 8
URL      : https://files.pythonhosted.org/packages/a5/a4/35e223fb9ade66bc3b6e759c1f95bad0a682b455cd7fbb5ad42a9dd5ba21/torchmetrics-1.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/a5/a4/35e223fb9ade66bc3b6e759c1f95bad0a682b455cd7fbb5ad42a9dd5ba21/torchmetrics-1.2.0.tar.gz
Summary  : PyTorch native Metrics
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-torchmetrics-license = %{version}-%{release}
Requires: pypi-torchmetrics-python = %{version}-%{release}
Requires: pypi-torchmetrics-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(lightning_utilities)
BuildRequires : pypi(numpy)
BuildRequires : pypi(torch)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<div align="center">
<img src="docs/source/_static/images/logo.png" width="400px">

%package license
Summary: license components for the pypi-torchmetrics package.
Group: Default

%description license
license components for the pypi-torchmetrics package.


%package python
Summary: python components for the pypi-torchmetrics package.
Group: Default
Requires: pypi-torchmetrics-python3 = %{version}-%{release}

%description python
python components for the pypi-torchmetrics package.


%package python3
Summary: python3 components for the pypi-torchmetrics package.
Group: Default
Requires: python3-core
Provides: pypi(torchmetrics)
Requires: pypi(lightning_utilities)
Requires: pypi(numpy)
Requires: pypi(torch)

%description python3
python3 components for the pypi-torchmetrics package.


%prep
%setup -q -n torchmetrics-1.2.0
cd %{_builddir}/torchmetrics-1.2.0
pushd ..
cp -a torchmetrics-1.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695395244
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-torchmetrics
cp %{_builddir}/torchmetrics-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-torchmetrics/d7fd67b8c4fff0cacef31a07a2ba24b008d49230 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-torchmetrics/d7fd67b8c4fff0cacef31a07a2ba24b008d49230

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
