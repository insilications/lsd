#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : lsd
Version  : 0.20.1
Release  : 3
URL      : file:///aot/build/clearlinux/packages/lsd/lsd-0.20.1.tar.gz
Source0  : file:///aot/build/clearlinux/packages/lsd/lsd-0.20.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: lsd-bin = %{version}-%{release}
Requires: lsd-data = %{version}-%{release}
BuildRequires : asciidoctor
BuildRequires : asciidoctor-bin
BuildRequires : asciidoctor-dev
BuildRequires : autoconf-archive-dev
BuildRequires : binutils-dev
BuildRequires : binutils-extras
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : ca-certs
BuildRequires : ca-certs-static
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : gcc-dev
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : glibc-staticdev
BuildRequires : googletest-dev
BuildRequires : grep
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libstdc++-dev
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : llvm12
BuildRequires : llvm12-abi
BuildRequires : llvm12-bin
BuildRequires : llvm12-data
BuildRequires : llvm12-dev
BuildRequires : llvm12-lib
BuildRequires : llvm12-libexec
BuildRequires : llvm12-man
BuildRequires : llvm12-staticdev
BuildRequires : ncurses-dev
BuildRequires : ninja
BuildRequires : openssl
BuildRequires : openssl-dev
BuildRequires : ruby
BuildRequires : rustc
BuildRequires : rustc-bin
BuildRequires : rustc-data
BuildRequires : rustc-dev
BuildRequires : rustc-staticdev
BuildRequires : termcolor
BuildRequires : time
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# LSD (LSDeluxe)
[![license](http://img.shields.io/badge/license-Apache%20v2-blue.svg)](https://raw.githubusercontent.com/Peltoche/lsd/master/LICENSE)
[![Latest version](https://img.shields.io/crates/v/lsd.svg)](https://crates.io/crates/lsd)
[![build](https://github.com/Peltoche/lsd/workflows/CICD/badge.svg)](https://github.com/Peltoche/lsd/actions)
[![codecov](https://codecov.io/gh/Peltoche/lsd/branch/master/graph/badge.svg)](https://codecov.io/gh/Peltoche/lsd)
[![versions](https://img.shields.io/repology/repositories/lsd)](https://repology.org/project/lsd/versions)

%package bin
Summary: bin components for the lsd package.
Group: Binaries
Requires: lsd-data = %{version}-%{release}

%description bin
bin components for the lsd package.


%package data
Summary: data components for the lsd package.
Group: Data

%description data
data components for the lsd package.


%prep
%setup -q -n lsd
cd %{_builddir}/lsd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
mkdir -p $HOME/.cargo
printf "[build]\nrustflags = [\"-Ctarget-cpu=native\", \"-Ztune-cpu=native\", \"-Cprefer-dynamic=no\", \"-Copt-level=3\", \"-Clto=fat\", \"-Clinker-plugin-lto=yes\", \"-Cembed-bitcode=yes\", \"-Clinker=clang-12\", \"-Clink-arg=-flto\", \"-Clink-arg=-fuse-ld=lld\", \"-Clink-arg=-Wl,--lto-O3\", \"-Clink-arg=-Wl,-O2\", \"-Clink-arg=-Wl,--hash-style=gnu\", \"-Clink-arg=-Wl,--enable-new-dtags\", \"-Clink-arg=-Wl,--build-id=sha1\", \"-Clink-arg=-fno-stack-protector\", \"-Clink-arg=-Wl,--as-needed\", \"-Clink-arg=-O3\", \"-Clink-arg=-march=native\", \"-Clink-arg=-mtune=native\", \"-Clink-arg=-falign-functions=32\", \"-Clink-arg=-fasynchronous-unwind-tables\", \"-Clink-arg=-funroll-loops\", \"-Clink-arg=-fvisibility-inlines-hidden\", \"-Clink-arg=-static-libstdc++\", \"-Clink-arg=-march=native\", \"-Clink-arg=-static-libgcc\", \"-Clink-arg=-pthread\", \"-Clink-arg=-lpthread\", \"-Clink-arg=-L.\"]\n[net]\ngit-fetch-with-cli = true\n" > $HOME/.cargo/config.toml
unset CFLAGS
unset CXXFLAGS
unset FCFLAGS
unset FFLAGS
unset CFFLAGS
unset LDFLAGS
export CARGO_NET_GIT_FETCH_WITH_CLI=true
export CARGO_PROFILE_RELEASE_LTO=true
export CARGO_PROFILE_RELEASE_OPT_LEVEL=3
export CARGO_TARGET_X86_64_UNKNOWN_LINUX_GNU_LINKER=clang-12
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export CARGO_HTTP_CAINFO=/var/cache/ca-certs/anchors/ca-certificates.crt
export CARGO_TARGET_DIR=target
cargo clean
cargo update --verbose

%install
mkdir -p $HOME/.cargo
printf "[build]\nrustflags = [\"-Ctarget-cpu=native\", \"-Ztune-cpu=native\", \"-Cprefer-dynamic=no\", \"-Copt-level=3\", \"-Clto=fat\", \"-Clinker-plugin-lto=yes\", \"-Cembed-bitcode=yes\", \"-Clinker=clang-12\", \"-Clink-arg=-flto\", \"-Clink-arg=-fuse-ld=lld\", \"-Clink-arg=-Wl,--lto-O3\", \"-Clink-arg=-Wl,-O2\", \"-Clink-arg=-Wl,--hash-style=gnu\", \"-Clink-arg=-Wl,--enable-new-dtags\", \"-Clink-arg=-Wl,--build-id=sha1\", \"-Clink-arg=-fno-stack-protector\", \"-Clink-arg=-Wl,--as-needed\", \"-Clink-arg=-O3\", \"-Clink-arg=-march=native\", \"-Clink-arg=-mtune=native\", \"-Clink-arg=-falign-functions=32\", \"-Clink-arg=-fasynchronous-unwind-tables\", \"-Clink-arg=-funroll-loops\", \"-Clink-arg=-fvisibility-inlines-hidden\", \"-Clink-arg=-static-libstdc++\", \"-Clink-arg=-march=native\", \"-Clink-arg=-static-libgcc\", \"-Clink-arg=-pthread\", \"-Clink-arg=-lpthread\", \"-Clink-arg=-L.\"]\n[net]\ngit-fetch-with-cli = true\n" > $HOME/.cargo/config.toml
unset CFLAGS
unset CXXFLAGS
unset FCFLAGS
unset FFLAGS
unset CFFLAGS
unset LDFLAGS
export CARGO_NET_GIT_FETCH_WITH_CLI=true
export CARGO_PROFILE_RELEASE_LTO=true
export CARGO_PROFILE_RELEASE_OPT_LEVEL=3
export CARGO_TARGET_X86_64_UNKNOWN_LINUX_GNU_LINKER=clang-12
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export CARGO_HTTP_CAINFO=/var/cache/ca-certs/anchors/ca-certificates.crt
export CARGO_TARGET_DIR=target
cargo install %{?_smp_mflags} --target-dir target --target x86_64-unknown-linux-gnu --all-features --verbose --path . --root %{buildroot}/usr/
## Cargo install assets
install -dm 0755 %{buildroot}/usr/share/bash-completion/completions/
install -m0644 /builddir/build/BUILD/lsd/target/x86_64-unknown-linux-gnu/release/build/lsd-dd83cf13cf532ce4/out/lsd.bash %{buildroot}/usr/share/bash-completion/completions/lsd
install -dm 0755 %{buildroot}/usr/share/fish/completions/
install -m0644 /builddir/build/BUILD/lsd/target/x86_64-unknown-linux-gnu/release/build/lsd-dd83cf13cf532ce4/out/lsd.fish %{buildroot}/usr/share/fish/completions/lsd.fish
install -dm 0755 %{buildroot}/usr/share/zsh/site-functions/
install -m0644 /builddir/build/BUILD/lsd/target/x86_64-unknown-linux-gnu/release/build/lsd-dd83cf13cf532ce4/out/_lsd %{buildroot}/usr/share/zsh/site-functions/_lsd
rm %{buildroot}/usr/.crates*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lsd

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/lsd
/usr/share/fish/completions/lsd.fish
/usr/share/zsh/site-functions/_lsd
